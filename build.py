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
    json.dump(out, open("data.json", "w"), ensure_ascii=False, indent=1)
    assets = json.load(open("assets.json", encoding="utf-8")) if os.path.exists("assets.json") else {}
    page, split = [], []
    forced = json.load(open("tools/split_groups.json", encoding="utf-8")) if os.path.exists("tools/split_groups.json") else {}
    aliases = json.load(open("tools/aliases.json", encoding="utf-8"))
    load = json.load(open("loadouts.json", encoding="utf-8")) if os.path.exists("loadouts.json") else {"items": [], "ships": {}}
    if os.path.exists("wiki_dims.json"):  # curated wiki sizes override padded game-data boxes
        for n, w in json.load(open("wiki_dims.json", encoding="utf-8")).items():
            s = load["ships"].get(n)
            if s:
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
