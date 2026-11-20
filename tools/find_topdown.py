"""List top-down ("Above") images on each ship's starcitizen.tools page.
Writes tools/topdown_candidates.json {sheet name: [file titles, best first]}."""
import json, os, re, urllib.parse, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "liberator-planner/1.0"}
def get(u):
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read())
A = json.load(open(os.path.join(ROOT, "assets.json"), encoding="utf-8"))
pages = {k: urllib.parse.unquote(v["page"].rsplit("/", 1)[1]).replace("_", " ") for k, v in A.items() if v.get("page")}
imgs = {}
titles = sorted(set(pages.values()))
for i in range(0, len(titles), 20):
    cont = {}
    while True:
        q = {"action": "query", "titles": "|".join(titles[i:i+20]), "prop": "images", "imlimit": 500, "format": "json", "redirects": 1, **cont}
        j = get("https://starcitizen.tools/api.php?" + urllib.parse.urlencode(q))
        for p in j["query"]["pages"].values():
            imgs.setdefault(p["title"], []).extend(x["title"] for x in p.get("images", []))
        if "continue" not in j: break
        cont = j["continue"]
def rank(t):
    l = t.lower()
    if not re.search(r"\babove\b|top ?view|topdown|top-down|[ -]top\b", l): return None
    if any(x in l for x in ("rear above", "front above", "above port", "above starboard", "on top")): return None
    return (0 if "in space - above" in l else 1 if "- above" in l else 2, l)
out = {}
for k, p in pages.items():
    c = sorted((t for t in imgs.get(p, []) if rank(t)), key=rank)
    out[k] = c
json.dump(out, open(os.path.join(ROOT, "tools", "topdown_candidates.json"), "w"), indent=1, ensure_ascii=False)
print("none:", [k for k, v in out.items() if not v])
