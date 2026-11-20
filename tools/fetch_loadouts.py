"""Fetch default loadouts, ship stats and a component catalog (game data).

Usage: python tools/fetch_loadouts.py
Source: api.star-citizen.wiki /api/v2/vehicles and /api/v2/items (values
extracted from the game files, LIVE 4.10.3).
Writes loadouts.json: {"items": [...], "ships": {variant name: {...}}}.
Items are referenced by index into "items".
"""
import json, os, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.star-citizen.wiki/api/v2"
UA = {"User-Agent": "liberator-planner/1.0 (loadouts)"}
TYPES = ["WeaponGun", "Shield", "PowerPlant", "Cooler", "QuantumDrive", "Missile", "WeaponDefensive"]
BAD = ("placeholder", "template", "_test", "_npc", "_ai_", "display", "_fake", "_dummy", "_unmanned")


def get(url):
    for n in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return json.loads(r.read())
        except Exception:  # noqa: BLE001
            if n == 4:
                raise
            time.sleep(2 ** n)


def pages(path):
    out, p = [], 1
    while True:
        j = get(f"{API}/{path}{'&' if '?' in path else '?'}page%5Bsize%5D=50&page%5Bnumber%5D={p}")
        out += j["data"]
        if p >= j["meta"]["last_page"]:
            return out
        p += 1


def compact(x):
    t, r = x.get("type"), {"n": x["name"], "s": x.get("size"), "t": x.get("type")}
    if t == "WeaponGun":
        w, a = x.get("vehicle_weapon") or {}, x.get("ammunition") or {}
        modes = w.get("modes") or [{}]
        r.update(k=w.get("type"), dps=round(modes[0].get("damage_per_second") or 0, 1),
                 a=round(w.get("damage_per_shot") or 0, 1))
        if w.get("regeneration") is None and (a.get("capacity") or w.get("capacity")):
            r["am"] = a.get("capacity") or w.get("capacity")  # ballistic: finite ammo, restocked by RRR
    elif t == "Shield":
        s = x.get("shield") or {}
        r.update(hp=s.get("max_health"), rg=s.get("regen_rate"))
    elif t == "PowerPlant":
        r["pw"] = (x.get("power_plant") or {}).get("power_segment_generation")
    elif t == "Cooler":
        r["cl"] = (x.get("cooler") or {}).get("coolant_segment_generation")
    elif t == "QuantumDrive":
        q = x.get("quantum_drive") or {}
        r.update(sp=(q.get("standard_jump") or {}).get("drive_speed"), fr=q.get("quantum_fuel_requirement"))
    elif t == "Missile":
        m = x.get("missile") or {}
        r.update(dmg=m.get("damage_total"), sig=m.get("signal_type"))
    elif t == "WeaponDefensive":
        r["am"] = (x.get("vehicle_weapon") or {}).get("capacity")
    return r


def main():
    aliases = json.load(open(os.path.join(ROOT, "tools", "aliases.json"), encoding="utf-8"))
    want = {n for v in aliases.values() for n in v}
    items, index = [], {}

    def ref(x):
        u = x["uuid"]
        if u not in index:
            index[u] = len(items)
            items.append(compact(x))
        return index[u]

    for t in TYPES:
        for x in pages(f"items?filter%5Btype%5D={t}"):
            cn = (x.get("class_name") or "").lower()
            if any(b in cn or b in x["name"].lower() for b in BAD):
                continue
            ref(x)
    vehicles = {}
    for v in pages("vehicles"):
        if v["name"] in want and ("display" not in v["class_name"].lower() or v["name"] not in vehicles):
            vehicles[v["name"]] = v
    for n, v in list(vehicles.items()):  # list endpoint omits nested ports; fetch full records
        vehicles[n] = get(f"{API}/vehicles/{urllib.parse.quote(v['slug'])}")["data"]
    ships = {}
    missing_items = set()

    def item_for(e):
        if not e:
            return None
        if e["uuid"] in index:
            return index[e["uuid"]]
        missing_items.add(e["uuid"])
        return e["uuid"]

    for name, v in vehicles.items():
        slots = []

        def walk(ports, path):
            for p in ports or []:
                e, t, pid = p.get("equipped_item"), p.get("type"), path + [p["name"]]
                et = (e or {}).get("type")
                if et == "MissileLauncher":
                    ms = [c for c in (p.get("ports") or []) if (c.get("equipped_item") or {}).get("type") == "Missile"
                          or c.get("type") == "Missile"]
                    if ms:
                        c0 = ms[0]
                        slots.append({"id": "/".join(pid), "t": "Missile", "s": (c0.get("sizes") or {}).get("max"),
                                      "n": len(ms), "d": item_for(c0.get("equipped_item")), "rk": e["name"]})
                    continue
                if et in ("WeaponGun", "Shield", "PowerPlant", "Cooler", "QuantumDrive", "WeaponDefensive") or \
                        (t in ("WeaponGun", "Shield", "PowerPlant", "Cooler", "QuantumDrive") and not e):
                    slots.append({"id": "/".join(pid), "t": et or t, "s": (e or {}).get("size") or (p.get("sizes") or {}).get("max"),
                                  "d": item_for(e), "ed": bool(p.get("editable", True))})
                    if et == "WeaponGun":
                        continue
                walk(p.get("ports"), pid)

        walk(v.get("ports"), [])
        fuel, q = v.get("fuel") or {}, v.get("quantum") or {}
        ships[name] = {
            "L": (v.get("sizes") or {}).get("length"), "B": (v.get("sizes") or {}).get("beam"),
            "H": (v.get("sizes") or {}).get("height"),
            "mass": v.get("mass_total") or v.get("mass"),
            "price": min([x["price_buy"] for x in ((v.get("uex_prices") or {}).get("purchase") or []) if x.get("price_buy")] or [None], key=lambda z: z or 1e18),
            "role": v.get("role"), "crew": [(v.get("crew") or {}).get("min"), (v.get("crew") or {}).get("max")],
            "scm": (v.get("speed") or {}).get("scm"), "vmax": (v.get("speed") or {}).get("max"),
            "hull": v.get("health"), "cargo": v.get("cargo_capacity"),
            "fuel": fuel.get("capacity"), "qfuel": q.get("quantum_fuel_capacity"),
            "slots": slots,
        }
    # resolve equipped items that the catalog filter dropped
    for u in sorted(missing_items):
        try:
            x = get(f"{API}/items/{u}")["data"]
            ref(x)
        except Exception as ex:  # noqa: BLE001
            print("item fetch failed", u, ex)
    for s in ships.values():
        for sl in s["slots"]:
            if isinstance(sl["d"], str):
                sl["d"] = index.get(sl["d"])
    json.dump({"items": items, "ships": ships}, open(os.path.join(ROOT, "loadouts.json"), "w", encoding="utf-8"),
              ensure_ascii=False, separators=(",", ":"))
    print(len(items), "items;", len(ships), "ships; not found:", sorted(want - set(ships)))


if __name__ == "__main__":
    main()
