"""Fetch curated ship dimensions from starcitizen.tools infoboxes.

Usage: python tools/fetch_wiki_dims.py
For every variant in tools/aliases.json, reads the wiki page's Vehicle
infobox (length / width / height). A page is used only when its infobox
uuid matches the game-data vehicle uuid (api.star-citizen.wiki), so a
redirect to a different variant is never mixed in. The wiki sometimes
replaces padded game-data boxes with store-page figures (e.g. the M80).
Writes wiki_dims.json {variant: {"L","B","H","src"}}.
"""
import json, os, re, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "liberator-planner/1.0 (wiki dims)"}


def get(url):
    for n in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.loads(r.read())
        except Exception:  # noqa: BLE001
            if n == 3:
                raise
            time.sleep(2 ** n)


def num(t, k):
    m = re.search(r"\|\s*" + k + r"\s*=\s*([0-9.]+)", t)
    return float(m.group(1)) if m else None


def main():
    aliases = json.load(open(os.path.join(ROOT, "tools", "aliases.json"), encoding="utf-8"))
    want = sorted({n for v in aliases.values() for n in v})
    uuid, p = {}, 1
    while True:
        j = get(f"https://api.star-citizen.wiki/api/v2/vehicles?page%5Bsize%5D=50&page%5Bnumber%5D={p}")
        for v in j["data"]:
            if v["name"] in want and "display" not in v["class_name"].lower():
                uuid[v["name"]] = v["uuid"]
        if p >= j["meta"]["last_page"]:
            break
        p += 1
    text = {}
    for i in range(0, len(want), 40):
        q = {"action": "query", "titles": "|".join(want[i:i + 40]), "prop": "revisions", "rvprop": "content",
             "rvslots": "main", "redirects": 1, "format": "json"}
        j = get("https://starcitizen.tools/api.php?" + urllib.parse.urlencode(q))["query"]
        back = {}
        for k in ("normalized", "redirects"):
            for r in j.get(k, []):
                back[r["to"]] = back.get(r["from"], r["from"])
        for pg in j["pages"].values():
            if "revisions" in pg:
                text[back.get(pg["title"], pg["title"])] = (pg["title"], pg["revisions"][0]["slots"]["main"]["*"])
    out, skipped = {}, []
    for n in want:
        if n not in text:
            skipped.append((n, "no page"))
            continue
        title, t = text[n]
        m = re.search(r"\|\s*uuid\s*=\s*([0-9a-f-]{36})", t)
        if not m or m.group(1) != uuid.get(n):
            skipped.append((n, "uuid mismatch"))
            continue
        L, B, H = num(t, "length"), num(t, "width"), num(t, "height")
        if L and B:
            out[n] = {"L": L, "B": B, "H": H, "src": "https://starcitizen.tools/" + urllib.parse.quote(title.replace(" ", "_"))}
        else:
            skipped.append((n, "no dims"))
    json.dump(out, open(os.path.join(ROOT, "wiki_dims.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(out), "variants with wiki dims; skipped:", skipped)


if __name__ == "__main__":
    main()
