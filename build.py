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
    page = []
    for d in out:
        a, d = assets.get(d["n"], {}), dict(d)
        for k in ("L", "B", "H"):
            if a.get(k) is not None:
                d[k] = a[k]
        if a.get("img") and os.path.exists(a["img"]):
            d["t"] = "data:image/webp;base64," + base64.b64encode(open(a["img"], "rb").read()).decode()
        if a.get("top") and os.path.exists(a["top"]):
            d["td"] = "data:image/webp;base64," + base64.b64encode(open(a["top"], "rb").read()).decode()
        page.append(d)
    tpl = open("tpl.html", encoding="utf-8").read()
    open("index.html", "w", encoding="utf-8").write(
        tpl.replace("__DATA__", json.dumps(page, ensure_ascii=False, separators=(",", ":"))))
    print(len(out), "entries")

if __name__ == "__main__":
    main(sys.argv[1])
