"""Write docs/size-audit.md: game data vs RSI store page vs wiki, per variant.

Usage: python tools/size_report.py   (after fetch_loadouts / fetch_store_dims / fetch_wiki_dims)
Rule used by the planner: game data > RSI store page > wiki. Landed overrides
(tools/dim_overrides.json) win for ships whose wings fold when landed.
A conflict is flagged when the store page and game data differ by more than
10% and 1 m in length or width (either orientation).
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda f: json.load(open(os.path.join(ROOT, f), encoding="utf-8")) if os.path.exists(os.path.join(ROOT, f)) else {}


def close(a, b):
    ok = lambda p, q: abs(p - q) <= max(1.0, 0.1 * max(p, q))
    return (ok(a[0], b[0]) and ok(a[1], b[1])) or (ok(a[0], b[1]) and ok(a[1], b[0]))


def main():
    aliases = J("tools/aliases.json")
    game = J("loadouts.json").get("ships", {})
    store, wiki, over = J("store_dims.json"), J("wiki_dims.json"), J("tools/dim_overrides.json")
    f = lambda d: f"{d['L']:g} × {d['B']:g}" if d and d.get("L") else "—"
    rows, conflicts = [], []
    for n in sorted({n for v in aliases.values() for n in v}):
        g = game.get(n, {}) if game.get(n, {}).get("L") else {}
        s, w, o = store.get(n), wiki.get(n), over.get(n)
        used = o or g or s or w
        frm = "override" if o else "game data" if g else "store page" if s else "wiki"
        conflict = bool(g and s and not close((g["L"], g["B"]), (s["L"], s["B"])))
        rows.append((n, f(used), frm, f(g), f(s), f(w), conflict))
        if conflict:
            conflicts.append(rows[-1])
    out = ["# Ship size audit", "",
           "Length × width in metres. The planner uses **game data > RSI store page > wiki**. Ships whose wings fold when landed use a measured landed width (see `tools/dim_overrides.json`).",
           "", f"## Store page vs game data conflicts ({len(conflicts)})", "",
           "| Variant | Game data (used) | RSI store page | Wiki |", "|---|---|---|---|"]
    out += [f"| {r[0]} | {r[3]} | {r[4]} | {r[5]} |" for r in conflicts]
    out += ["", f"## All variants ({len(rows)})", "", "| Variant | Planner | From | Game data | RSI store page | Wiki | Conflict |", "|---|---|---|---|---|---|---|"]
    out += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {'⚠' if r[6] else ''} |" for r in rows]
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    open(os.path.join(ROOT, "docs", "size-audit.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(len(rows), "variants;", len(conflicts), "store vs game conflicts")
    for r in conflicts:
        print(f"  {r[0]:30} game {r[3]:14} store {r[4]:14} wiki {r[5]}")


if __name__ == "__main__":
    main()
