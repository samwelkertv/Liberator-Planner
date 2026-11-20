"""Audit every ship size against all sources.

Usage: python tools/audit_sizes.py
Compares, for each variant in tools/aliases.json:
  planner  - the size the app uses (wiki, or tools/dim_overrides.json)
  wiki     - starcitizen.tools infobox (wiki_dims.json)
  game     - api.star-citizen.wiki game data (loadouts.json raw values)
  matrix   - RSI ship matrix
  scorg    - scorg.tools ship-information page
Writes docs/size-audit.md and prints the flagged variants.
"""
import json, os, re, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "liberator-planner/1.0 (size audit)"}


def get(url, as_json=False):
    for n in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                b = r.read()
                return json.loads(b) if as_json else b.decode("utf-8", "ignore")
        except Exception:  # noqa: BLE001
            if n == 2:
                return None
            time.sleep(2)


def norm(s):
    s = s.lower().replace("’", "'")
    s = re.sub(r"^(aegis|anvil|argo|aopoa|crusader|drake|esperia|gatac|grey's|greycat|kruger|mirai|misc|origin|rsi|tumbril|consolidated outland|c\.o\.|cnou|banu|vanduul|hm6|roberts space industries) ", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def main():
    aliases = json.load(open(os.path.join(ROOT, "tools", "aliases.json"), encoding="utf-8"))
    variants = sorted({n for v in aliases.values() for n in v})
    wiki = json.load(open(os.path.join(ROOT, "wiki_dims.json"), encoding="utf-8"))
    over = json.load(open(os.path.join(ROOT, "tools", "dim_overrides.json"), encoding="utf-8"))
    load = json.load(open(os.path.join(ROOT, "loadouts.json"), encoding="utf-8"))["ships"]
    sm = get("https://robertsspaceindustries.com/ship-matrix/index", True) or {"data": []}
    matrix = {norm(x["name"]): x for x in sm["data"]}
    lst = get("https://scorg.tools/ship-information") or ""
    scorg_ids = {}
    for sid, slug in re.findall(r'/ship-information/(\d+)/([^"\'<> ]+)', lst):
        scorg_ids.setdefault(norm(urllib.parse.unquote_plus(slug)), (sid, slug))
    rows, flagged = [], []
    for n in variants:
        k = norm(n)
        g = load.get(n, {})
        game = (g.get("L"), g.get("B"))
        w = wiki.get(n, {})
        x = matrix.get(k)
        mat = (float(x["length"] or 0), float(x["beam"] or 0)) if x and x.get("length") else None
        sc = None
        if k in scorg_ids:
            sid, slug = scorg_ids[k]
            t = get(f"https://scorg.tools/ship-information/{sid}/{slug}") or ""
            t = re.sub(r"<[^>]+>", " ", t)
            L = re.search(r"Length:\s*([0-9.]+)\s*m", t)
            B = re.search(r"Beam:\s*([0-9.]+)\s*m", t)
            if L and B:
                sc = (float(L.group(1)), float(B.group(1)))
            time.sleep(0.3)
        cur = (over[n]["L"], over[n]["B"]) if n in over else (w.get("L"), w.get("B"))
        src = {"wiki": (w.get("L"), w.get("B")), "game": game, "matrix": mat, "scorg": sc}
        vals = [v for v in src.values() if v and v[0]]
        # agreement: sources within 10% of the planner size (length and width, either orientation)
        def close(a, b):
            if not a or not b or not a[0] or not b[0]:
                return False
            ok = lambda p, q: abs(p - q) <= max(1.0, 0.1 * max(p, q))
            return (ok(a[0], b[0]) and ok(a[1], b[1])) or (ok(a[0], b[1]) and ok(a[1], b[0]))
        agree = [s for s, v in src.items() if close(cur, v)]
        disagree = [s for s, v in src.items() if v and v[0] and not close(cur, v)]
        flag = len(disagree) >= 2 or (len(agree) <= 1 and len(vals) >= 3)
        rows.append((n, cur, src, agree, disagree, flag, "override" if n in over else "wiki"))
        if flag:
            flagged.append(n)
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    f = lambda v: f"{v[0]:g} × {v[1]:g}" if v and v[0] else "—"
    out = ["# Ship size audit", "", "Length × width in metres. **Planner** is what the app draws. A row is flagged when two or more sources disagree with it by more than 10% (and 1 m).", "",
           "| Variant | Planner | From | Wiki | Game data | RSI matrix | scorg.tools | Flag |", "|---|---|---|---|---|---|---|---|"]
    for n, cur, src, agree, dis, flag, frm in rows:
        out.append(f"| {n} | {f(cur)} | {frm} | {f(src['wiki'])} | {f(src['game'])} | {f(src['matrix'])} | {f(src['scorg'])} | {'⚠ ' + ', '.join(dis) if flag else ''} |")
    open(os.path.join(ROOT, "docs", "size-audit.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(len(rows), "variants audited;", len(flagged), "flagged")
    for n, cur, src, agree, dis, flag, frm in rows:
        if flag:
            print(f"{n:30} planner {f(cur):13} ({frm}) | wiki {f(src['wiki']):13} game {f(src['game']):13} matrix {f(src['matrix']):13} scorg {f(src['scorg'])}")


if __name__ == "__main__":
    main()
