"""Cut out top-down ("Above") wiki images and save them nose-up.

Usage: python tools/topdown.py [montage.png]
Reads tools/topdown_candidates.json (from tools/find_topdown.py) and
tools/topdown_fix.json (manual overrides per sheet name:
  {"file": "File:...", "rot": 0|90|180|270, "skip": true}).
Writes img/top/<slug>.webp (transparent background, cropped to the hull,
long axis vertical) and adds "top" paths to assets.json.
Needs Pillow, numpy and scipy.
"""
import io, json, os, re, sys, urllib.parse, urllib.request
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "liberator-planner/1.0 (topdown)"}
CACHE = os.path.join(ROOT, "tools", ".cache")
OUT = 360  # longest side of saved image


def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def urls(titles):
    res = {}
    for i in range(0, len(titles), 40):
        q = urllib.parse.urlencode({"action": "query", "titles": "|".join(titles[i:i + 40]), "prop": "imageinfo",
                                    "iiprop": "url", "iiurlwidth": 900, "format": "json"})
        j = json.loads(get("https://starcitizen.tools/api.php?" + q))["query"]
        back = {n["to"]: n["from"] for n in j.get("normalized", [])}
        for p in j["pages"].values():
            if "imageinfo" in p:
                res[back.get(p["title"], p["title"])] = p["imageinfo"][0].get("thumburl") or p["imageinfo"][0]["url"]
    return res


def cutout(im):
    a = np.asarray(im.convert("RGBA")).astype(np.int16)
    rgb, alpha = a[..., :3], a[..., 3]
    if (alpha < 250).mean() > 0.05:  # already transparent
        fg = alpha > 40
    else:
        border = np.concatenate([rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]])
        bg = np.median(border, axis=0)
        spread = np.percentile(np.abs(border - bg).sum(1), 90)
        tol = max(45, min(110, spread * 1.6 + 20))
        near = np.abs(rgb - bg).sum(2) < tol
        lab, _ = ndimage.label(near)
        edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
        bgmask = np.isin(lab, edge[edge > 0])
        fg = ~bgmask
        fg = ndimage.binary_opening(fg, iterations=2)
    lab, n = ndimage.label(fg)
    if n == 0:
        return None
    sizes = ndimage.sum(fg, lab, range(1, n + 1))
    keep = [i + 1 for i, s in enumerate(sizes) if s >= sizes.max() * 0.04]
    fg = ndimage.binary_fill_holes(np.isin(lab, keep))
    if fg.mean() > 0.6 or fg.mean() < 0.01:  # background not separable
        return None
    ys, xs = np.where(fg)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    soft = ndimage.gaussian_filter(fg.astype(float), 0.8)
    out = np.dstack([a[..., :3], (soft * 255).clip(0, 255)]).astype(np.uint8)[y0:y1, x0:x1]
    return Image.fromarray(out, "RGBA")


def main(montage=None):
    cand = json.load(open(os.path.join(ROOT, "tools", "topdown_candidates.json"), encoding="utf-8"))
    fix = json.load(open(os.path.join(ROOT, "tools", "topdown_fix.json"), encoding="utf-8"))
    assets = json.load(open(os.path.join(ROOT, "assets.json"), encoding="utf-8"))
    pick = {}
    for k in assets:
        f = fix.get(k, {})
        if f.get("skip"):
            continue
        t = f.get("file") or (cand.get(k) or [None])[0]
        if t:
            pick[k] = t
    u = urls(sorted(set(pick.values())))
    os.makedirs(CACHE, exist_ok=True)
    os.makedirs(os.path.join(ROOT, "img", "top"), exist_ok=True)
    tiles, failed = [], []
    for k, t in pick.items():
        assets[k].pop("top", None)
        if t not in u:
            failed.append((k, "no url"))
            continue
        cp = os.path.join(CACHE, slug(t) + os.path.splitext(u[t].split("?")[0])[1])
        if not os.path.exists(cp):
            open(cp, "wb").write(get(u[t]))
        im = cutout(Image.open(cp))
        if im is None:
            failed.append((k, "cutout"))
            continue
        if "rot" in fix.get(k, {}):
            im = im.rotate(fix[k]["rot"], expand=True)
        elif re.search(r"(in space|selfland) - above", t.lower()):
            im = im.rotate(270, expand=True)  # these wiki shots face left; turn nose up
        elif im.width > im.height:
            im = im.rotate(270, expand=True)
        cf = 1
        if "crop" in fix.get(k, {}):  # e.g. wings folded when landed
            x0, x1 = fix[k]["crop"]
            im = im.crop((round(x0 * im.width), 0, round(x1 * im.width), im.height))
            cf = x1 - x0
        im.thumbnail((OUT, OUT), Image.LANCZOS)
        rel = "img/top/" + slug(k) + ".webp"
        im.save(os.path.join(ROOT, rel), "WEBP", quality=72, method=6)
        assets[k]["cf"] = cf
        assets[k]["top"], assets[k]["topsrc"] = rel, "https://starcitizen.tools/" + urllib.parse.quote(t.replace(" ", "_"))
        tiles.append((k, im))
    for k in assets:
        if k not in pick:
            assets[k].pop("top", None)
    json.dump(assets, open(os.path.join(ROOT, "assets.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(tiles), "top-down images; failed/none:", failed, [k for k in assets if k not in pick])
    if montage:
        W, H, c = 130, 170, 10
        m = Image.new("RGB", (W * c, H * ((len(tiles) + c - 1) // c)), (235, 235, 235))
        d = ImageDraw.Draw(m)
        for i, (k, im) in enumerate(tiles):
            t = im.copy()
            t.thumbnail((W - 10, H - 26))
            x, y = (i % c) * W, (i // c) * H
            m.paste(t, (x + 5, y + 20), t)
            d.text((x + 3, y + 3), f"{i}:{k[:18]}", fill=(0, 0, 0))
        m.save(montage)


if __name__ == "__main__":
    main(*sys.argv[1:])
