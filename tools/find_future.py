"""Pick 'future possible support' ships: not in the fit sheet, under 16 m tall and
no wider than the Liberator's top-deck channel (about 23.7 m), plus any named in
tools/future_force.json (e.g. MOTH, MOLE).

Usage: python tools/find_future.py
Sizes: RSI store page first, then game data. Writes tools/future.json:
{display name: {"m": maker, "k": "ship"|"ground", "v": [variant names]}}
and adds the same names to tools/aliases.json so the fetch scripts include them.
"""
import json, os, re, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "liberator-planner/1.0 (future)"}
MAX_H, MAX_W = 16.0, 23.74
SKIP = re.compile(r"Wikelo|PYAM|Best In Show|Executive Edition|CitizenCon|2951 BIS|Template|Emerald|Kitten|Cool Metal|Snowland|Orange Line|Akuma|Rad$", re.I)


def get(url, j=False):
    for n in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                b = r.read()
                return json.loads(b) if j else b.decode("utf-8", "ignore")
        except Exception:  # noqa: BLE001
            if n == 2:
                return None
            time.sleep(2)


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"^(misc|argo|hm6|anvil|drake|origin|rsi|aegis|crusader) ", "", s.lower()))


def main():
    aliases = json.load(open(os.path.join(ROOT, "tools", "aliases.json"), encoding="utf-8"))
    old = json.load(open(os.path.join(ROOT, "tools", "future.json"), encoding="utf-8")) if os.path.exists(os.path.join(ROOT, "tools", "future.json")) else {}
    for k in old:
        aliases.pop(k, None)
    have = {n for v in aliases.values() for n in v}
    force = json.load(open(os.path.join(ROOT, "tools", "future_force.json"), encoding="utf-8"))
    veh, p = {}, 1
    while True:
        j = get(f"https://api.star-citizen.wiki/api/v2/vehicles?page%5Bsize%5D=50&page%5Bnumber%5D={p}", True)
        for v in j["data"]:
            if "display" not in v["class_name"].lower():
                veh.setdefault(v["name"], v)
        if p >= j["meta"]["last_page"]:
            break
        p += 1
    sm = {norm(x["name"]): x for x in (get("https://robertsspaceindustries.com/ship-matrix/index", True) or {"data": []})["data"]}
    out = {}
    for n, v in sorted(veh.items()):
        if n in have or SKIP.search(n):
            continue
        g = v.get("sizes") or {}
        L, B, H = g.get("length") or 0, g.get("beam") or 0, g.get("height") or 0
        x = sm.get(norm(n))
        if x:
            h = get("https://robertsspaceindustries.com" + x["url"]) or ""
            vals = {m.group(1): float(m.group(2)) for m in re.finditer(r'"name":"(Length|Width|Height)","value":"([0-9.]+)"', h)}
            L, B, H = vals.get("Length", L), vals.get("Width", B), vals.get("Height", H)
            time.sleep(0.3)
        if n not in force and not (L and B and H and H < MAX_H and B <= MAX_W):
            continue
        maker = ((v.get("manufacturer") or {}).get("name") or "").split()[0] if v.get("manufacturer") else ""
        out[n] = {"m": maker, "k": "ground" if v.get("is_vehicle") and not v.get("is_spaceship") else "ship", "v": [n], "size": [L, B, H]}
    json.dump(out, open(os.path.join(ROOT, "tools", "future.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, e in out.items():
        aliases[k] = e["v"]
    json.dump(aliases, open(os.path.join(ROOT, "tools", "aliases.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(out), "future ships:")
    for k, e in out.items():
        print(f"  {k:32} {e['m']:10} {e['k']:6} {e['size']}")


if __name__ == "__main__":
    main()
