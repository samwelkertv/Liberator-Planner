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

## v6 update: Liberator hull drawn to scale (Nov 20, 2026)
- **Outline source:** both views now draw the Liberator outline to scale, bow on the left. Sam found a community top-down on Google; the outline and pad positions are traced from it, made symmetric and scaled to the game-data 119 × 67 m. It's marked as approximate in the app, and the image itself isn't in the repo.
- **Coordinates:** the `LIB` constant in `tpl.html`, in metres, measured along from the bow and across from the centreline.
  - Front pad: 7.8–34.3 m
  - Ramp: 34.3–50 m
  - Upper pad 1: 50–84 m
  - Upper pad 2: 85–115.9 m
  - Centre channel: ±12.5 m wide
- **Garages:** placing them under the upper pads (same footprints) is an assumption. The concept cutaway shows one central vehicle bay running from the forward ramp to the rear ramp.
- **Drawing:** ships appear in their real pad positions, nose toward the bow. Pads in the drawing are tap and drop targets. The slot cards (controls) sit below the drawing.
- **Removed:** the per-slot dashed "largest confirmed fit" boxes. The oversize flag still uses that size.

## v7 update: free placement on the real top-down (Nov 20, 2026)
- **Hull image:** the drawing now uses the scorg.tools Liberator top-down (`https://scorg.tools/media/ships/224-top-1000.webp`, saved as `img/liberator-top.webp`).
  - It's 1000 × 563 px, which matches the game-data 119 × 67 m (8.4 px per metre), so it's used at true scale with the bow on the left.
  - The internal view shows it dimmed, with an approximate vehicle-bay outline over the centre channel (9–116 m along, ±11.7 m across).
- **Placement model:** the plan is a list of placements `{n, v: external|internal, x, y (metres), r (degrees), f: loadout}` saved in localStorage `libplan3`. Old `libplan2`/`libfit` plans migrate automatically. There are no slots and no one-per-pad limit.
- **Adding ships:** one **+ Add ship** button per tab. You can also drag a ship from the list onto the drawing, tap a list ship and then tap the drawing, or use the bottom bar ("Add to external" / "Add to internal"). New ships go to a free pad centre when one is open.
- **Arranging:** drag ships on the drawing. A selected ship can be turned 15° or 90° (R or Shift+R), nudged with the arrow keys (Shift for 2 m) and removed (Delete).
- **Warnings:**
  - Overlap with another ship in the same view (rotated-rectangle test).
  - A ship that doesn't fit that view per the sheet.
  - An F ship placed behind the front pad (more than 50 m from the bow).
  - A ship outside the approximate bay outline on the internal view.
- **Source:** `tools/plan_block.js` is the source of the plan script; it was spliced into `tpl.html`, so edit `tpl.html` directly from now on.

## v8 update (Nov 20, 2026)
- **Orientation:** the drawing is vertical with the bow at the top (the model is wrapped in `rotate(90)`). Internally, coordinates are still `x` = metres from the bow and `y` = metres across. `svgPt()` converts from screen, and the arrow keys are remapped to match.
- **Ship sizes:**
  - Each placement uses the game-data size of its chosen variant. `loadouts.json` ships now carry L/B/H; grouped rows default to their first variant.
  - Drawn size uses the top-down image's own proportions, with the longest side set to max(L, B) of the variant. Several game-data boxes are padded or square: the M80 is listed as 11.5 × 11 m but is long and narrow.
  - The old "largest variant" group size made the Hornet Ghost Mk II draw as the 28.3 × 25.5 m Mk I.
- **Clipper:** drawn wings-folded, as when landed. Its image is cropped to the fuselage and engine pods via `"crop"` in `tools/topdown_fix.json`; the crop fraction is kept in `cf` so the scale still comes from the full wingspan.
- **Touch dragging:** a touch that starts on a placed ship no longer scrolls the page, so ships can be dragged on phones and tablets.
- `tools/plan_block.js` is removed; the plan script lives in `tpl.html`.

## v9 update: app layout (Nov 20, 2026)
- **Full-screen layout:** the page no longer scrolls. A header bar holds the External/Internal tabs and the buttons + Add ship, Ships, Placed (count), RRR, Undo, Copy, Clear and ⓘ. The drawing fills the rest of the screen.
- **Pop-out panels:** the ship list, placed ships, the RRR list and About/sources (`#p-list`, `#p-placed`, `#p-rrr`, `#p-info`).
  - The Placed panel sits on the left and can stay open alongside a right-hand panel on wide screens; right-hand panels replace each other.
  - On narrow screens only one panel is open at a time.
  - Escape closes the open panel.
  - Starting a drag from the Ships panel closes it on screens narrower than 900 px, so you can drop onto the drawing.
- **Floating controls:** the selected-ship toolbar floats at the bottom of the drawing, and messages float at the top.
- **Arrow:** drawn with its outer wing panels folded (`"crop": [0.237, 0.759]` in `tools/topdown_fix.json`). The fold line is estimated from the panel seams in the top-down.
- **Off-ship warning:** external ships whose centre is off the hull get an "Off the ship" warning.

## v10 update (Nov 20, 2026)
- **Ship sizes from the wiki:** sizes now come from the starcitizen.tools infoboxes.
  - `tools/fetch_wiki_dims.py` writes `wiki_dims.json`, and `build.py` applies it over the game data. A page is used only when its infobox uuid matches the game-data vehicle; that covers 121 of 168 variants, and the rest fall back to the API.
  - The wiki corrects padded game-data boxes. Examples: the M80 is 32 × 17.3 m (store figures; an editor note says the API is "way off"), the Hornet Ghost Mk II 22.5 × 15, Cyclone 6 × 4, Nova 16 × 7, Mule 4.2 × 3.
- **Drawing:** each ship's footprint is its length × width, and the top-down image is fitted inside it, keeping its own proportions. Cropped (wings-folded) ships use width × crop fraction. The v8 rule that sized ships from image proportions is gone.
- **No scrolling while dragging:** the body is fixed in place with no overscroll, the drawing area ignores touch scrolling, and pointermove calls `preventDefault` while dragging. Dragging a ship never scrolls the page.
- **Internal view:** ships can't go on the front pad; they're clamped to the door at 34 m from the bow, the start of the vehicle bay. The front pad is shaded red as "outside".
- **Export image:** a PNG with the external view on the left and the internal view on the right. Each SVG is cloned with its styles inlined, then drawn to a canvas. A dialog shows the image with a Download link, and right-click or long-press also saves it.

## v11 update (Nov 20, 2026)
- **Placed panel:** lists both views at once, grouped under External and Internal headings. Clicking a ship from the other view switches tabs and selects it. The header count is now the total across both views. The RRR list already covered every placed ship in both views.
- **Pitbull top-down:** the wiki's "3D model - Above" image sits on a dark grid that the cutout can't separate from the dark hull. It now uses a plain rectangular crop (new `"box"` option in `tools/topdown_fix.json`, with fractions of the raw image). A `"tol"` override for the background tolerance was added too.
- **Pitbull size:** stays about 6 × 6 m; the wiki (5.93 × 6.13), the game data and the RSI ship matrix all agree.

## v12 update (Nov 20, 2026)
- **Cargo and ramps on the internal view:**
  - Three cargo bays, drawn with their game-data grid sizes (192, 128 and 80 SCU).
  - They sit on the starboard side of the garage at 52–80 m from the bow. The wiki says starboard; the mid-ship position is an estimate from the concept cutaway.
  - Dashed edges mark the doors into the garage.
  - The ramps are highlighted: forward ramp/door at 34 m, rear ramp at 116 m. Per the wiki, vehicles load from the rear ramp and unload over the forward ramp and pad. Constants: `CARGO` in `tpl.html`.
- **Export:** each view's image now lists its ships underneath: name, variant, size, every custom part change, and any warnings in red.
- **Loadouts:**
  - The button is renamed "Loadout" (on the placed cards and the selection bar); the dialog title is "loadout & stats".
  - New "Save as my <ship> setup" saves the variant and part changes per ship name in localStorage `libmy`. Every new ship of that name starts with it. "Use my setup" and "Forget my setup" also appear.
- **Folded-wing ships:** the Clipper and Arrow show their landed width plus the full wingspan in their size text.
- **Pitbull cutout (v12.1):** new `"texture"` option in `tools/topdown_fix.json` cuts the ship out by surface texture, colour and brightness, ignoring the background grid lines. The Pitbull uses `{"texture": 25}` in place of the rectangle crop.

## v13 update (Nov 20, 2026)
- **Loadouts:** a new Loadouts panel. Each loadout is saved to the artifact database (the `db` capability), collection `loadouts`, one document per loadout: `{name, plan, my, stock, extra, updatedAt, isDefault}`.
  - The panel offers Save (overwrite the current loadout, with an "unsaved changes" flag), Save as new, Load, Make default, Rename (inline) and Delete (click twice).
  - On first load with an empty database, the browser's current plan is saved as "Default".
  - A browser with no plan, such as a new device, opens the default loadout.
  - The current loadout id is kept in localStorage `libcur`.
- **RRR stock planning:** each ammo, missile, countermeasure and fuel row has an "On board" input and shows "Refills" (stock ÷ full load: green at 1× or more, red below).
  - "Other supplies on board" is a free list of name and quantity, for items like repair materials.
  - Stock is saved in localStorage `libstock`/`libextra`, and in each loadout.
- **Zoom and pan (zoom in only, 1–6×):** two-finger pinch on touch, trackpad pinch or mouse wheel on desktop. When zoomed in, drag the background to pan; a two-finger pinch also pans. A "Reset zoom" button appears while zoomed. The export always uses the full view.
- **Pitbull:** confirmed on the texture cutout (setting 25), the first of the three tried.

## v14 update (Nov 20, 2026)
- **Side-by-side views:** on wide landscape screens (min-width 900px and min-aspect-ratio 1/1), External and Internal show side by side, each labelled. The tabs hide there; phones keep them.
  - Interacting with a view (or clicking its label) makes it the active view, used for + Add ship and the Placed count.
  - The Add dialog has an External/Internal switch.
  - Zoom is shared by both views.
- **Theme fix:** the toggle now sets `data-lp-theme` on `<html>`, with `color-scheme: … !important` on `html` and `body`. The claude.ai viewer sets its own theme (`data-theme` / color-scheme), which overrode the old attribute, so Light did nothing.
- **v14.1:** the views are now toggled with an `.off` class instead of the `hidden` attribute. The claude.ai viewer appears to force `[hidden]{display:none!important}`, which blocked the side-by-side layout. The drawing is also scaled down 5% for padding: base viewBox `-37.9 -6.4 75.8 134.8`, in the HTML, in `VB0` and in the export.

## v15 update (Nov 20, 2026)
- **Outlines button:** toggles the dashed outlines around ships that have images. A selected ship keeps its outline. The setting is saved in localStorage `libbox` and the exported image follows it (`display` was added to the inlined export styles).
- **Ramp door on the external view:** the forward ramp door (34.3–48.8 m from the bow) is shaded blue under the ships, with a solid line where the ramp ends.
- **Labels:** the internal ramp label is shortened to "⇅ Forward ramp" so it no longer clips. The export says "1 ship" instead of "1 ships".

## v16 update (Nov 20, 2026)
- **10 m gap side by side:** in the side-by-side layout, JS (`layoutViews`) sizes each drawing to its content. It then sets the gap so the closest hull pixels of the two Liberators sit exactly 10 m apart (the scale-bar length), measured equal at 2000/1280/1000 px widths. It reruns on resize.
- **Stage toolbar:** Totals, Outlines, theme, ⓘ, Clear and Reset zoom moved from the header to a toolbar at the top-right of the drawing area.
- **Totals card (Σ Totals, saved in localStorage `libtot`):**
  - It shows ship count, mass (`mass_total`, default loadout), and ship cost: the lowest in-game UEX buy price via api.star-citizen.wiki. 136 of 168 variants have a price; missing ones are listed.
  - It also has an editable cargo-cost line (saved in `libcost` and in loadouts), the total, hydrogen and quantum fuel sums (game-data units), ships' own cargo SCU, crew range and gun DPS.
  - The export header shows the same totals.
  - `fetch_loadouts.py` now stores `mass` and `price` per variant.
  - The card starts hidden on narrow screens.
- **Ramp door overlay:** now shown on the internal view as well as the external one.

## v17 update (Nov 20, 2026)
- **Wiki sizes for all 168 variants:** `fetch_wiki_dims.py` now has a second pass that reads the rendered infobox ("Length … m / Width … m / Height … m") when the page source has no dimensions. It also tries simpler page names (dropping prefixes like "MISC " or "HM6 ", or " Limited").
- **Drawing:** each ship's footprint is exactly its wiki length × width (× crop fraction for folded wings), and the top-down picture is stretched to fill that box (`preserveAspectRatio="none"`). The "natural width from image" rule tried in between was dropped; the user prefers the wiki boxes.
- **Cross-view drag:** dragging a placed ship onto the other view moves it there, if the sheet says it fits that view; the target view is highlighted while you drag. The selection bar also has "⇄ Other view" for phones.
- **Labels:** pad, ramp and cargo labels now draw underneath ships. The drawing is built in three layers: base, then labels, then ships.
- **Totals:** `loadouts.json` was re-fetched with `mass` and `price`.
- **v17.1:** dragging a ship no longer selects it; only a click without movement does. Sizing rule (final, after user feedback):
  - The length is always the wiki length.
  - If the top-down picture shows the placed variant itself (`d.iv` = first alias), the width comes from the picture's own proportions, so nothing is squished. The width is capped at max(L, B) to catch padded boxes such as the Eclipse.
  - Pictures borrowed from another variant (e.g. the Ghost uses the F7C Mk II picture) are fitted inside the wiki L × B box.
  - The Golem OX's side pods make it about 9.8 m wide, against the wiki's 7 m.
- **v17.2:** dragging across views is now live. As soon as the pointer enters the other view, the ship switches to it and keeps following the pointer, so there's no separate drop step. A ship the sheet says doesn't fit that view stays put, with a message.
- **v17.3:** a selected ship shows a rotation handle (line plus circle) beyond its nose. Dragging it rotates the ship freely (1° steps, Shift for 15°), and Undo reverts it. The selection bar gains "Reset rotation" (back to 0°, nose to the bow).

## v18 update (Nov 20, 2026)
- **Liberator size:** the hull now uses the wiki size, 122 × 68 × 24 m, instead of the game-data 119 × 67 × 25 (`LIBL`/`LIBW` in `tpl.html`). Image-measured geometry (pads, ramp, bay, cargo, labels) scales by SX = 122/119 and SY = 68/67. The base viewBox is now `-37.9 -6.6 75.8 141.1`.
- **Vehicle bay width:** set in the ⓘ panel and saved in localStorage `libbayw`. It defaults to the top-deck channel width (23.7 m) because no source gives the garage width; a friend of the user says the garage is narrower than the top. Ships are clamped and warned against it. The front-pad and ramp overlays keep the channel width (`CH`).
- **Local loadouts:** outside claude.ai there is no `window.claude`, so loadouts use a localStorage-backed store with the same API (`localDB()`, key `libloads`). Loadouts can be exported to and imported from a JSON file (`liberator-loadouts.json`). New visitors start empty.
- **Hosting:** see README for GitHub Pages. The repo is currently private, so Pages needs a paid plan or a public repo.

## v19 update (Nov 20, 2026, testing branch)
- **Marauder:** top-down supplied by the user (`tools/img_src/marauder-top.png`), cut out with the new `"bluebg"` method (blue-grid background) via `"file": "local:…"` in `tools/topdown_fix.json`. Size comes from the official dimension graphic, 21.0 × 20.4 × 7.0 m, in the new `tools/dim_overrides.json`. Override sizes beat the wiki, and the picture fills that exact box.
- **Variant rows:** `build.py` splits a sheet row into separate list items when its variants differ by 1.5 m or more in length or width. `tools/split_groups.json` forces splits where sizes match; currently ATLS vs ATLS GEO.
  - The build log lists every split.
  - Old plans and loadouts keep working: `fixName()` maps old group names to the new item, using the saved variant.
- **Add ships:** now a side panel (`#p-add`) that stays open, so you can add several ships.
- **Floating controls:** open panels push the drawing-area toolbar and the Totals card aside (`--rpw` / `--lpw`).
- **Loadouts auto-save:** the Save button is gone. Changes are written to the current loadout about 0.7 s after they happen. If no loadout exists yet, one is created ("Default", or "Loadout N").
- **Overlays button:** toggles the pad, ramp, bay and cargo overlays and their labels (saved in localStorage `libov`). Exports follow it.
- **Owned ships:** a ☆/★ button on each ship card tags it as owned (saved in localStorage `libown`, and included in loadout export/import). The ★ Owned filter shows only owned ships, and the Add panel lists owned ships first.
- **v19.1:** landed widths are now measured from wiki images and stored as overrides (`landed` / `spread` in `tools/dim_overrides.json`):
  - **Arrow:** 16 × 11.1 m, from "Arrow in Selfland - Above" (wings tilt up but stay out; 12 m spread in flight). The old fold-line crop was removed.
  - **Clipper:** 26.5 × 16 m. Body and engine pods measure about 293 of 915 px in "Clipper in space - Front" (50 m span); the wings fold vertical beside the hull.
  - Override boxes are drawn exactly. Release rule: once everything the user has asked for is done and tested, push the testing branch to `main` (fast-forward) without waiting to be asked, unless the user says otherwise.
- **v19.2:** Hornet Ghost Mk II size override, 22.5 × 22 × 6.5 m. The game data, the RSI ship matrix and scorg.tools agree, and scorg's top view matches the F7C Mk II outline; the wiki's 15 m width is wrong. The Ghost now merges back into the main Hornet item. `fixName()` also maps names of removed split items by variant, and owned tags are migrated the same way. The Marauder stays at the official 21 × 20.4 × 7 m (every other source says 20 × 19 × 6 m).

## v20 update (Nov 20, 2026)
- **Size rule (from the user): game data > RSI store page > wiki.**
  - `tools/fetch_store_dims.py` reads the RSI store pages' structured specs into `store_dims.json` (157 of 168 variants). The store can differ from the ship-matrix JSON (M80: store 32 × 17.3 m, matrix 11.5 × 11).
  - `build.py` keeps the game data and falls back to store, then wiki, only when game data is missing.
  - `tools/dim_overrides.json` now holds only the measured landed widths for the Clipper and Arrow. The Ghost and Marauder overrides were removed, so they use game data: 22.5 × 22 m and 20 × 19 m.
  - `tools/size_report.py` writes `docs/size-audit.md`, listing every store-vs-game conflict (63) with the wiki value.
  - The older `tools/audit_sizes.py` also compares the RSI matrix and scorg.tools.
- **ATLS / ATLS GEO:** each has its own top view from scorg.tools (`tools/variant_images.json`; split items can carry a variant-specific image).
- **Ship lists merged:** one "+ Ships" panel. Each card has + Ext / + Int buttons (greyed out when the ship doesn't fit), plus the ★ owned toggle, filters and drag-and-drop. The separate Add panel is gone.
- **Garage width is still unverified.** The fit sheet rates ships as wide as about 18 m with fixed wings (Hurricane, Gladius) as fitting inside, and wider folding-wing ships too. Game-data widths are flight boxes, so they can't pin down the bay width.
- **v20.3: size rule changed by the user** to **overrides > RSI store page > game data > wiki**. "Game data" means api.star-citizen.wiki, extracted from the game files: often padded or shared boxes, full wingspans and extended lengths. The user found these wrong at the start. Overrides: Clipper and Arrow landed widths, and Hull B 46 × 17 m (closed; 71 m is extended). With the store first: M80 32 × 17.3, Ghost and Tracker 22.5 × 15, Marauder 20.5 × 18.5, ground vehicles at real sizes (Mule 4.2 × 3, Cyclone 6 × 4). Row splits regenerated (e.g. Cutlass Black vs Blue/Red/Steel, Mustang Omega, 350r, C8R, MPUV Personnel); old plans migrate.

## v21 update (Nov 20, 2026)
- **Sizes dropdown on the drawing toolbar:** RSI store page (default), Game data or Wiki, saved in localStorage `libsrc`.
  - `build.py` embeds every source per variant as `S:{store,game,wiki}` in `loadouts.json` ships; the page picks with `vsz()`. If the chosen source has no size, it falls back to the next one (store → game → wiki).
  - `tools/dim_overrides.json` (Clipper and Arrow landed widths, Hull B closed length) always applies, whichever source is picked.
  - The ⓘ panel explains each source, and the export header names the source used.
- **Swapped figures:** `tools/dim_swaps.json` swaps length and width for sources that list them the wrong way round. Currently the Pitbull store page lists 3.9 × 5.9 m.
- **Disclaimer:** small and discreet in the drawing area, and in the ⓘ panel.
- **v21.1:** ship pictures now fill their size box exactly (the picture's visible edges = length × width from the chosen source). The earlier keep-the-picture-proportions rule was dropped at the user's request.

## v22 update (Nov 20, 2026)
- **Future possible support:** `tools/find_future.py` picks ships that aren't in the sheet, are under 16 m tall and fit within the top-deck channel width (23.74 m), using the store page then game data. It also adds anything in `tools/future_force.json` (MOTH, MOLE).
  - Output goes to `tools/future.json`, and the names are added to `tools/aliases.json`.
  - `build.py` appends them as `e:"future"`. They show only under the "Future support" filter, can be placed outside with an "untested" warning, and can't go inside.
  - Run order after changing it: find_future → build → fetch_assets → find_topdown → topdown → fetch_loadouts → fetch_wiki_dims → fetch_store_dims → build.
- **Terrapin Medic:** red top view from scorg.tools (`tools/variant_images.json`); store size 19.5 × 16.7 m.
- **Loadout window:** wider (980 px).

## v23 update (Nov 20, 2026)
- **Overlays menu (checkboxes):** Pads, Doors & ramps, Cargo bays, Vehicle bay outline, and "Tint colliding ships red" (an SVG feColorMatrix filter `#tr-<view>` on colliding ships' images).
- **Outlines menu (radios):**
  - Outline shape: collision shape or size box.
  - Show on: all ships, colliding ships only, or none.
  - Collision test: ship outline + 10 px buffer, or size boxes.
  - Settings are saved in localStorage `libopt` (old `libov`/`libbox` settings migrate).
- **Pixel collision:** `build.py` `collision_shape()` takes each top-down image's alpha mask, grows it by 10 px (at the image's own ~360 px resolution, about 2.8% of ship length) on every side, and produces:
  - a 96-cell bit grid (`ck.g`) for collision tests;
  - padding fractions (`ck.pw`/`ck.ph`);
  - an outline ring PNG (`ck.ring`), drawn through an SVG mask and coloured by status.
- **Runtime collision test:** `collide()` first does a quick rotated-box check on the padded boxes, then samples ship A's grid cells against ship B's mask. Ships without a top-down use their size box grown by the same proportion.
- Exports follow all of these settings.
- **v23.2:** collision is always the ship outline (the collision-test and outline-shape options were removed at the user's request). Two buffers:
  - **3 px collision:** red, "Overlaps …" warning, red tint.
  - **10 px warning:** orange, "Close to …", orange tint and outline. It can be toggled under Overlays (`OPT.warn`).
  - The build emits `ck` (3 px) and `cw` (10 px) collision shapes per ship.
  - Fixed a bug where the shape lookup read ships nose-for-tail; ships point toward −u and their local +x maps to −w.
  - The Sizes source selector moved into the ⓘ panel.

**Release rule (current):** the user tests on the live site (liberatorplanner.xyz), so push each tested change to `main` (fast-forward) as soon as it is ready.
- **v24:**
  - **Buffers:** 5 px collision (red) and 15 px warning (orange).
  - **Collision Warning:** a single checkbox under Overlays controls both the tints and the warnings (`OPT.tint`, with `OPT.warn` following it).
  - **Clear:** opens a centred confirmation pop-up whose Clear button unlocks after a 3-second countdown.
  - **RRR stock:** now crates per item, as size × quantity entries (1/2/4/8/16/24/32 SCU), saved in `STOCK[key] = [{s, q}]`. The panel shows the SCU total against the 400 SCU cargo bays. Refills aren't calculated, because no source gives units per SCU. Old numeric stock values are dropped.
  - **Theme switch and Sizes selector:** both now live in the ⓘ panel.
- **v25:**
  - **Undo/redo:** Ctrl/Cmd+Z, Ctrl/Cmd+Shift+Z or Ctrl+Y, plus a Redo button. `hist` is a `Hist` array whose `push` clears the `REDO` stack.
  - **Copy/paste sections:** Copy outside/inside on the current plan (Loadouts panel → "Sections of the current plan") and on every saved loadout row. The clipboard is saved in localStorage `libclip` as `{v, ships, from}`. Paste replaces that view in the current plan, and Undo reverts it.
