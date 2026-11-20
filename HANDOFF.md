# Liberator Deck Planner — handoff

## Goal
A simple web app for planning which Star Citizen ships and vehicles go where on an Anvil Liberator. It covers **every ship that fits**, whether or not the user owns it. The app should make clear what each pad or garage supports.

## Current state (v2, single-file HTML)
- Published as a claude.ai artifact (private): https://claude.ai/artifact/Xva8DoJRNPJwRxNwm4X3Nq
- `index.html` is the built page. `tpl.html` is the same page with a `__DATA__` placeholder, and `build.py` fills that placeholder from the spreadsheet.
- Rebuild with `python build.py STAR_CITIZEN_SHIP_FITTING_LIST.xlsx` (needs `openpyxl`).
- Features:
  - **External / Internal tabs.** External shows the front pad and upper pads 1 and 2. Internal shows garages 1 and 2. While a ship is selected, each tab shows a dot for whether that ship fits anywhere in that view.
  - **One ship per slot.** An empty slot has a **+ Add ship** button that opens a searchable picker. The picker lists only ships that fit that slot, good fits first. Tapping a placed ship opens the picker again to swap it out.
  - **Ship list on the side**, with search, filters (All / Ships / Ground / Fits inside / Front pad only) and Deck/Garage fit badges.
  - **Drag and drop** from the list with a mouse, or by the ⠿ handle on touch. Hovering over a tab while dragging switches to that view. You can also tap a ship and then tap a slot, or use the bottom bar's per-slot buttons, which are built for phones.
  - **Slot highlighting** while a ship is selected: green means fits, orange means needs tricks, dimmed means doesn't fit.
  - Undo, Clear, Copy plan. The plan and the last-used tab are saved in localStorage.

## Data source
- `STAR_CITIZEN_SHIP_FITTING_LIST.xlsx`: the Pegaxsus "Ship Fit List", LIVE 4.10.3, last update Nov 16, 2026. Public sheet: https://docs.google.com/spreadsheets/d/15wiwmRnwqzBDpFF0B02ifxHH3OqNe0CLAtL8NU3hefc/htmlview
- Tab `COMBINED SHEET`:
  - Row 2 holds the carrier names and row 3 the sub-headers. The Liberator is column M (`Ext.`) and column N (`Int.`).
  - Each row is a ship. Column A is the maker and column B the ship. Ground vehicles start at the row where column A is `GROUND`, and rows from `OTHER` onward are excluded.
- **Cell colors carry meaning that a CSV export loses**, so read the xlsx and not a CSV:
  - `✔` on green `93C47D` = good fit. `X` = doesn't fit.
  - `F` = Liberator external front pad (may need to be parked reversed).
  - Orange `FF9900` = "Needs tricks / barely fit" in the legend. **Assumption:** the slightly different orange `E69138` means the same thing.
  - Pink `D5A6BD` = "No info / not tested". Purple `8E7CC3` = "Fits but bugged".
- 97 entries fit somewhere on the Liberator. Rows that are X in both columns are dropped.

## Layout decisions and sources
- **Pads.** The Liberator has three landing pads: one front pad and two upper pads. The official Q&A covers this, along with size classes: the upper pads take "XS" ships, and the garages and front pad take "XXS" ships plus ground vehicles up to the Nova/Ballista.
  - Q&A comm-link 18365: https://api.star-citizen.wiki/api/comm-links/18365
  - Wiki page: https://starcitizen.tools/index.php?title=Liberator
- **Two garages is an assumption.** The Q&A says "garages" (plural), and the ship is sold as carrying "three ships and two vehicles." Verify this.
- **Fit rules:**
  - An Ext ✔ ship can use either upper pad, and the app also allows it on the front pad. That second part is an assumption.
  - An `F` ship can use only the front pad.
  - An Int value decides fit for the garages.
- **Not to scale.** No pad, garage or ship measurements have been sourced yet. One third-party ranking lists the Liberator at 119m, which isn't an official figure.

## Requested next (in the user's priority)
1. **A thumbnail for every ship in the list.**
2. **Top-down images of each ship from the wiki**, cut out from their backgrounds, used on the pads and in drag and drop.
   - starcitizen.tools has a MediaWiki API, and its media host is `media.starcitizen.tools`.
   - The artifact host can't load remote images, so bundle the images locally or as data URIs, or run the app outside the artifact host.
3. **True-to-scale layout:**
   - Source the pad and garage dimensions, and each ship's length and beam (ship matrix or wiki).
   - Scale the hull and footprints.
   - Warn when a footprint overlaps or overflows its slot.
4. Re-confirm the garage count and whether Ext ✔ ships really fit on the front pad.

## User notes
- Sam is the user. He wants concise replies and doesn't want unsourced numbers stated. If a figure isn't sourced, say so rather than estimating it.
- He keeps a tight eye on token and quota use, so prefer cheap, batched work.

## v3 update (Nov 20, 2026)
- **Thumbnails:** all 97 entries. Each is the starcitizen.tools page image, saved to `img/*.webp` (192×120) and inlined into `index.html` as a data URI.
- **Sizes:** game-data length, beam and height via `api.star-citizen.wiki/api/v2/vehicles`. Grouped rows use the largest variant listed in `tools/aliases.json`. The G12 isn't in game data, so its size comes from the wiki infobox (`tools/manual_dims.json`).
  - Several ground vehicles share an identical 8.75 × 6 m box (Mule, Cyclone, Ursa, STV and others). It looks like a size class rather than a hull measurement.
- **Top-down images:** the wiki has none for most ships, so the pads show to-scale footprint rectangles, nose up.
- **Scale:** every pad and garage uses one common metre scale.
  - No pad or garage dimensions are published anywhere I found. Each slot's dashed box is the largest ship rated a good fit there: front 51 × 40, upper 46 × 35, garage 32 × 27.4 m.
  - A ship bigger than its slot's box is flagged red.
  - Overlap between neighbouring pads can't be checked, because the pad positions aren't sourced.
- **Garages:** two is now sourced. The Q&A asks about "each of the garages", and the game data has ports `hardpoint_cargo_garage_a` and `_b`.
- **Front pad:** the Q&A rates it for XXS ships and ground vehicles. A ship rated only for the upper pads is allowed there but shown as "not tested".
- **Refresh assets:** run `python tools/fetch_assets.py`, then `python build.py STAR_CITIZEN_SHIP_FITTING_LIST.xlsx`. The fetch needs network access to starcitizen.tools, media.starcitizen.tools and api.star-citizen.wiki. The `liberator-planner` cloud environment allows these.

## v4 update (Sam's corrections, Nov 20, 2026)
- **The xlsx is the only fit source, and everything in it is tested in game.** An Ext ✔ ship fits all three external pads.
  - F on green fits the front pad only. F on orange worked there but was sketchy.
  - The Q&A-based "front pad not tested" rule from v3 is removed.
- **Height:** the front pad has better height support. For now the upper pads take ships with a centre of gravity at 5 m or lower, and taller ships are expected to fit later. This comes from Sam's in-game testing; there's no centre-of-gravity data to check it against, so the app shows height (L × B × H) but doesn't enforce it.
- **Top-down images:** most wiki ship pages have an "in space - Above" shot. `tools/find_topdown.py` lists them, then `tools/topdown.py` cuts each one out of its background and turns it nose up into `img/top/`.
  - Overrides and skips live in `tools/topdown_fix.json`.
  - 78 of 97 entries have one. The others show a plain footprint because the wiki has no usable top-down or the cutout failed: Command Module, Marauder, Pitbull, Hyun, Basher, S-65 Stingray, Reliant, Meteor, Skylark, Blade, Glaive, Khartu-al, Scythe, MDC, PTV, STV, UTV, G12, Nova.
- **Thumbnails:** done in v3, and lowest priority.
- **Rebuild order:** `tools/fetch_assets.py`, then `tools/find_topdown.py`, then `tools/topdown.py`, then `build.py`.

## v5 update: stats, loadouts, RRR (Nov 20, 2026)
- **Data:** `tools/fetch_loadouts.py` writes `loadouts.json` from api.star-citizen.wiki game data (4.10.3). It holds the stock loadout of every variant listed in `tools/aliases.json` (168 vehicles) and a catalog of 725 parts: guns, missiles, shields, power plants, coolers, quantum drives and countermeasures.
- **Stats dialog:** opens from the **Stats** button on a placed ship.
  - Shows role, crew, size, speed, hull, shields, gun DPS and alpha, missiles, power and cooling, quantum drive, fuel and cargo.
  - Grouped rows have a variant picker.
  - Each editable slot offers parts of the same type and size; stats update live; **Reset to stock** undoes changes.
  - Changes are saved per pad or garage in localStorage (`libfit`) and included in **Copy plan**.
- **RRR restock list:** a new section below the plan.
  - Totals for ballistic ammo by weapon, missiles by type, countermeasure charges, hydrogen and quantum fuel, and hull HP per ship, all with loadout changes applied.
  - **Copy restock list** button.
  - Per the wiki, RRR in 4.10.3 works in the internal garage through the landing services app, and pad RRR is planned for 5.0. The wiki doesn't document which cargo-bay supply items each refill uses.
- **Liberator top-down:** none exists on the wiki or RSI pages, external or internal. The closest are the isometric interior cutaways (`Anvil-liberator-interior-concept-01/02.png`), which aren't used.
- **Rebuild order:** `fetch_assets.py`, `find_topdown.py`, `topdown.py`, `fetch_loadouts.py`, then `build.py`.
