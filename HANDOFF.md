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
