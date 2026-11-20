"""Fetch ship dimensions and thumbnails for every entry in data.json.

Usage: python tools/fetch_assets.py
Needs network access to api.star-citizen.wiki, starcitizen.tools and
media.starcitizen.tools, plus Pillow.

Sources
- Dimensions: api.star-citizen.wiki /api/v2/vehicles (values extracted from the
  game files). Grouped sheet rows ("/ Variants") use the largest length and
  beam among the variants listed in tools/aliases.json.
- Thumbnails: the starcitizen.tools page image for the first variant listed.

Writes assets.json (dims, sources) and img/<slug>.webp (thumbnails).
"""
import io, json, os, re, sys, time, urllib.parse, urllib.request
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.star-citizen.wiki/api/v2/vehicles"
WIKI = "https://starcitizen.tools/api.php"
UA = {"User-Agent": "liberator-planner/1.0 (asset fetch)"}
TW, TH = 192, 120  # thumbnail size


def get(url):
    for n in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            if n == 3:
                raise
            time.sleep(2 ** n)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def all_vehicles():
    out, page = {}, 1
    while True:
        j = json.loads(get(f"{API}?page%5Bsize%5D=50&page%5Bnumber%5D={page}"))
        for v in j["data"]:
            disp = "display" in v["class_name"].lower()
            if v["name"] not in out or not disp:
                out[v["name"]] = v
        if page >= j["meta"]["last_page"]:
            return out
        page += 1


def page_images(titles):
    res = {}
    for i in range(0, len(titles), 40):
        q = urllib.parse.urlencode({"action": "query", "titles": "|".join(titles[i:i + 40]), "prop": "pageimages",
                                    "pithumbsize": 400, "redirects": 1, "format": "json"})
        j = json.loads(get(f"{WIKI}?{q}"))["query"]
        alias = {}
        for k in ("normalized", "redirects"):
            for r in j.get(k, []):
                alias[r["to"]] = alias.get(r["from"], r["from"])
        for p in j["pages"].values():
            t = p.get("title")
            if "thumbnail" in p:
                src = alias.get(t, t)
                res[src] = (p["thumbnail"]["source"], t)
                res[t] = (p["thumbnail"]["source"], t)
    return res


def thumb(url, path):
    im = Image.open(io.BytesIO(get(url))).convert("RGB")
    r = max(TW / im.width, TH / im.height)
    im = im.resize((max(TW, round(im.width * r)), max(TH, round(im.height * r))), Image.LANCZOS)
    x, y = (im.width - TW) // 2, (im.height - TH) // 2
    im.crop((x, y, x + TW, y + TH)).save(path, "WEBP", quality=68, method=6)


def main():
    data = json.load(open(os.path.join(ROOT, "data.json"), encoding="utf-8"))
    aliases = json.load(open(os.path.join(ROOT, "tools", "aliases.json"), encoding="utf-8"))
    extra = json.load(open(os.path.join(ROOT, "tools", "manual_dims.json"), encoding="utf-8"))
    veh = all_vehicles()
    want = []
    for d in data:
        al = aliases.get(d["n"]) or []
        want += al[:1] + [extra[d["n"]]["wiki"]] if d["n"] in extra else al[:1]
    imgs = page_images(sorted(set(want)))
    os.makedirs(os.path.join(ROOT, "img"), exist_ok=True)
    out, missing = {}, []
    for d in data:
        al = aliases.get(d["n"]) or []
        rec = {"variants": al}
        dims = [veh[n]["sizes"] for n in al if n in veh and veh[n].get("sizes", {}).get("length")]
        if dims:
            big = max(dims, key=lambda s: s["length"] * s["beam"])
            rec.update(L=max(s["length"] for s in dims), B=max(s["beam"] for s in dims), H=big["height"],
                       dsrc="game data via api.star-citizen.wiki")
        elif d["n"] in extra and extra[d["n"]].get("L"):
            e = extra[d["n"]]
            rec.update(L=e["L"], B=e["B"], H=e.get("H"), dsrc=e["src"])
        title = (al[:1] or [None])[0]
        hit = imgs.get(title) if title else None
        if not hit and d["n"] in extra:
            hit = imgs.get(extra[d["n"]]["wiki"])
        if hit:
            fn = slug(d["n"]) + ".webp"
            p = os.path.join(ROOT, "img", fn)
            if not os.path.exists(p):
                thumb(hit[0], p)
            rec.update(img="img/" + fn, page="https://starcitizen.tools/" + urllib.parse.quote(hit[1].replace(" ", "_")))
        if "L" not in rec or "img" not in rec:
            missing.append((d["n"], "dims" if "L" not in rec else "", "img" if "img" not in rec else ""))
        out[d["n"]] = rec
    json.dump(out, open(os.path.join(ROOT, "assets.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    lib = veh.get("Liberator", {}).get("sizes")
    print("Liberator", lib)
    print(len(out), "entries;", "missing:", missing or "none")


if __name__ == "__main__":
    sys.exit(main())
