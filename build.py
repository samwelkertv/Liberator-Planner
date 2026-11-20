"""Rebuild index.html from the Pegaxsus fit sheet.

Usage: python build.py STAR_CITIZEN_SHIP_FITTING_LIST.xlsx
Reads tab "COMBINED SHEET", Liberator Ext. (col M) / Int. (col N), rows 4-105.
Writes data.json and index.html (from tpl.html, replacing __DATA__).
If assets.json exists (from tools/fetch_assets.py), ship sizes and thumbnails
(img/*.webp, inlined as data URIs) are merged into the page.
"""
import base64, json, os, sys
import openpyxl

TRICKS = {"FFE69138", "FFFF9900"}   # orange shades -> "needs tricks / barely fit" (E69138 is an assumption)
UNTESTED = {"FFD5A6BD"}             # pink -> "no info / not tested"
BUGGED = {"FF8E7CC3"}               # purple -> "fits but bugged"

def status(cell):
    v, f = cell.value, cell.fill.fgColor.rgb
    if v == "X":
        return None
    if f in UNTESTED:
        return "untested"
    if v is None:
        return "fit_tricks" if f in TRICKS else None
    base = "front" if v == "F" else "fit"
    if f in TRICKS:
        return base + "_tricks"
    if f in BUGGED:
        return base + "_bugged"
    return base


def collision_shape(path, pad=10, grid=96):
    """Pixel collision shape for a nose-up top-down image: alpha mask grown by `pad` px
    (at the image's own resolution) on every side. Returns the padding as fractions of the
    image size, a coarse bit grid for collision tests and an outline ring (data URI) to draw."""
    import io
    import numpy as np
    from PIL import Image
    from scipy import ndimage
    im = Image.open(path).convert("RGBA")
    W, H = im.size
    a = np.asarray(im)[..., 3] > 40
    m = np.zeros((H + 2 * pad, W + 2 * pad), bool)
    m[pad:pad + H, pad:pad + W] = a
    yy, xx = np.mgrid[-pad:pad + 1, -pad:pad + 1]
    m = ndimage.binary_dilation(m, structure=(xx * xx + yy * yy) <= pad * pad)
    ring = m & ~ndimage.binary_erosion(m, iterations=3)
    rgba = np.zeros(m.shape + (4,), np.uint8)
    rgba[..., :3] = 255
    rgba[..., 3] = ring * 255
    buf = io.BytesIO()
    Image.fromarray(rgba, "RGBA").save(buf, "PNG", optimize=True)
    s = grid / max(m.shape)
    gw, gh = max(1, round(m.shape[1] * s)), max(1, round(m.shape[0] * s))
    small = np.asarray(Image.fromarray(m.astype(np.uint8) * 255).resize((gw, gh), Image.BOX)) > 0
    bits = np.packbits(small.flatten())
    return {"pw": round(pad / W, 5), "ph": round(pad / H, 5), "g": [gw, gh, base64.b64encode(bits.tobytes()).decode()],
            "ring": "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()}

def main(path):
    ws = openpyxl.load_workbook(path)["COMBINED SHEET"]
    out, maker, kind = [], None, "ship"
    for row in ws.iter_rows(min_row=4, max_row=105):
        a, b = row[0].value, row[1].value
        if a == "GROUND":
            kind = "ground"
            continue
        if a:
            maker = a
        if not b:
            continue
        e, i = status(row[12]), status(row[13])
        if e or i:
            out.append({"n": " ".join(str(b).split()), "m": " ".join(str(maker).split()),
                        "k": kind, "e": e, "i": i})
    if os.path.exists("tools/future.json"):  # ships not in the sheet that may fit the top pads in a future update
        for n, e in json.load(open("tools/future.json", encoding="utf-8")).items():
            out.append({"n": n, "m": e["m"], "k": e["k"], "e": "future", "i": None, "fut": True})
    json.dump(out, open("data.json", "w"), ensure_ascii=False, indent=1)
    assets = json.load(open("assets.json", encoding="utf-8")) if os.path.exists("assets.json") else {}
    page, split = [], []
    vimg = json.load(open("tools/variant_images.json", encoding="utf-8")) if os.path.exists("tools/variant_images.json") else {}
    forced = json.load(open("tools/split_groups.json", encoding="utf-8")) if os.path.exists("tools/split_groups.json") else {}
    aliases = json.load(open("tools/aliases.json", encoding="utf-8"))
    load = json.load(open("loadouts.json", encoding="utf-8")) if os.path.exists("loadouts.json") else {"items": [], "ships": {}}
    # Keep every source's size per variant so the page can switch between them (Source dropdown).
    _src = {"store": json.load(open("store_dims.json", encoding="utf-8")) if os.path.exists("store_dims.json") else {},
            "wiki": json.load(open("wiki_dims.json", encoding="utf-8")) if os.path.exists("wiki_dims.json") else {}}
    swaps = json.load(open("tools/dim_swaps.json", encoding="utf-8")) if os.path.exists("tools/dim_swaps.json") else {}
    for n, s in load["ships"].items():
        S = {}
        if s.get("L"):
            S["game"] = [s["L"], s["B"], s.get("H")]
        for k in ("store", "wiki"):
            w = _src[k].get(n)
            if w and w.get("L"):
                S[k] = [w["L"], w["B"], w.get("H")]
        for k, sw in swaps.get(n, {}).items():  # sources that list length and width the wrong way round
            if sw and k in S:
                S[k] = [S[k][1], S[k][0], S[k][2]]
        s["S"] = S
    # Size priority (user's rule): overrides > RSI store page > game data > wiki.
    # loadouts.json holds game data; the store page replaces it wherever it has specs.
    if os.path.exists("store_dims.json"):
        for n, w in json.load(open("store_dims.json", encoding="utf-8")).items():
            s = load["ships"].get(n)
            if s:
                s.update(L=w["L"], B=w["B"], ds="store", **({"H": w["H"]} if w.get("H") else {}))
    if os.path.exists("wiki_dims.json"):
        for n, w in json.load(open("wiki_dims.json", encoding="utf-8")).items():
            s = load["ships"].get(n)
            if s and s.get("ds") != "store":  # wiki beats game data when the store page has no size
                s.update(L=w["L"], B=w["B"], ds="wiki", **({"H": w["H"]} if w.get("H") else {}))
    if os.path.exists("tools/dim_overrides.json"):  # official figures that beat the wiki, e.g. from dimension graphics
        for n, w in json.load(open("tools/dim_overrides.json", encoding="utf-8")).items():
            s = load["ships"].get(n)
            if s:
                s.update(L=w["L"], B=w["B"], H=w.get("H", s.get("H")), ds="override", **{k: w[k] for k in ("landed", "spread") if k in w})
    for d in out:
        a, d = assets.get(d["n"], {}), dict(d)
        for k in ("L", "B", "H"):
            if a.get(k) is not None:
                d[k] = a[k]
        if a.get("img") and os.path.exists(a["img"]):
            d["t"] = "data:image/webp;base64," + base64.b64encode(open(a["img"], "rb").read()).decode()
        v0 = next((load["ships"][n] for n in aliases.get(d["n"], []) if n in load["ships"]), None)
        if v0 and v0.get("L"):
            d["L"], d["B"], d["H"] = v0["L"], v0["B"], v0["H"]
        if a.get("top") and os.path.exists(a["top"]):
            from PIL import Image
            w, h = Image.open(a["top"]).size
            d["ta"], d["cf"] = round(h / w, 4), a.get("cf", 1)
            d["td"] = "data:image/webp;base64," + base64.b64encode(open(a["top"], "rb").read()).decode()
            d["ck"] = collision_shape(a["top"])
        d["v"] = [n for n in aliases.get(d["n"], []) if n in load["ships"]]
        if aliases.get(d["n"]):
            d["iv"] = aliases[d["n"]][0]  # the variant the top-down image shows
        clusters = []  # variants whose size differs by 1.5 m or more get their own list item
        for n in d["v"]:
            sh = load["ships"][n]
            for c in clusters:
                r = load["ships"][c[0]]
                if abs((sh.get("L") or 0) - (r.get("L") or 0)) < 1.5 and abs((sh.get("B") or 0) - (r.get("B") or 0)) < 1.5:
                    c.append(n)
                    break
            else:
                clusters.append([n])
        if d["n"] in forced:  # split on request even when the sources give the same size
            clusters = [[n for n in grp if n in d["v"]] for grp in forced[d["n"]]]
        groups = {tuple(c): c for c in clusters if c}
        if len(groups) > 1:
            for names in groups.values():
                label = " / ".join(names) if len(names) <= 2 else f"{names[0]} (+{len(names) - 1} variants)"
                e = dict(d, n=label, g=d["n"], v=names)
                sh = load["ships"][names[0]]
                e["L"], e["B"], e["H"] = sh["L"], sh["B"], sh["H"]
                vi = vimg.get(names[0])
                if vi and os.path.exists(vi["img"]):  # this variant has its own top view
                    from PIL import Image
                    w, h = Image.open(vi["img"]).size
                    e.update(ta=round(h / w, 4), cf=1, iv=names[0],
                             td="data:image/webp;base64," + base64.b64encode(open(vi["img"], "rb").read()).decode())
                    e["ck"] = collision_shape(vi["img"])
                page.append(e)
            split.append((d["n"], [(" / ".join(nm), k) for k, nm in groups.items()]))
            continue
        page.append(d)
    libimg = ("data:image/webp;base64," + base64.b64encode(open("img/liberator-top.webp", "rb").read()).decode()) if os.path.exists("img/liberator-top.webp") else ""
    tpl = open("tpl.html", encoding="utf-8").read()
    open("index.html", "w", encoding="utf-8").write(
        tpl.replace("__DATA__", json.dumps(page, ensure_ascii=False, separators=(",", ":")))
        .replace("__LOAD__", json.dumps(load, ensure_ascii=False, separators=(",", ":")))
        .replace("__LIBIMG__", json.dumps(libimg)))
    print(len(out), "entries;", len(page), "list items")
    for g, parts in split:
        print("split", g, "->", parts)

if __name__ == "__main__":
    main(sys.argv[1])
