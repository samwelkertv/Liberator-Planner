"""Fetch ship dimensions from the RSI store (pledge) pages.

Usage: python tools/fetch_store_dims.py
The RSI store page for each ship carries structured data (schema.org
additionalProperty: Length / Width / Height). These can differ from the older
ship-matrix JSON (e.g. M80: store 32 x 17.3 m, matrix 11.5 x 11 m).
Variants are matched to store pages through the ship matrix (name -> url).
Writes store_dims.json {variant: {"L","B","H","src"}}.
"""
import json, os, re, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "liberator-planner/1.0 (store dims)"}


def get(url):
    for n in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception:  # noqa: BLE001
            if n == 2:
                return None
            time.sleep(2)


def norm(s):
    s = s.lower().replace("’", "'")
    s = re.sub(r"^(misc|hm6|vanduul|argo|anvil|drake|origin|rsi|aegis|crusader|kruger|mirai|esperia|tumbril) ", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def main():
    aliases = json.load(open(os.path.join(ROOT, "tools", "aliases.json"), encoding="utf-8"))
    variants = sorted({n for v in aliases.values() for n in v})
    sm = json.loads(get("https://robertsspaceindustries.com/ship-matrix/index") or '{"data":[]}')["data"]
    by = {norm(x["name"]): x for x in sm}
    extra = {"85xlimited": "85x", "f7chornetmkii": "f7chornetmkii"}
    out, missing = {}, []
    for n in variants:
        x = by.get(norm(n)) or by.get(extra.get(norm(n), ""))
        if not x:
            missing.append((n, "not in ship matrix"))
            continue
        url = "https://robertsspaceindustries.com" + x["url"]
        h = get(url) or ""
        vals = {m.group(1): float(m.group(2)) for m in re.finditer(r'"name":"(Length|Width|Beam|Height)","value":"([0-9.]+)"', h)}
        L, B = vals.get("Length"), vals.get("Width") or vals.get("Beam")
        if L and B:
            out[n] = {"L": L, "B": B, "H": vals.get("Height"), "src": url}
        else:
            missing.append((n, "no specs on page"))
        time.sleep(0.4)
    json.dump(out, open(os.path.join(ROOT, "store_dims.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(out), "variants with store dims; missing:", missing)


if __name__ == "__main__":
    main()
