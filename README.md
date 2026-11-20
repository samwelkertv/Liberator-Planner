# Liberator-Planner

A planner for packing Star Citizen ships and vehicles onto the Anvil Liberator: the top deck pads and the internal vehicle bay, all to scale. It also covers loadouts, RRR restock planning and plan totals.

The whole app is one file, `index.html`. All images and data are built into it, so it runs offline and can be hosted anywhere as a static page.

## Hosting it on GitHub Pages

1. Get `index.html` onto the branch you want to publish. Usually that means merging this work into `main`.
2. On GitHub, open **Settings → Pages**.
3. Under **Build and deployment**, pick **Deploy from a branch**, then select the branch (e.g. `main`) and the folder `/ (root)`. Save.
4. After a minute the site is live at `https://<user>.github.io/Liberator-Planner/`.

GitHub Pages on a **private** repository needs a paid GitHub plan. On the free plan, make the repository public first (Settings → General → Danger Zone → Change visibility).

## Where data is saved

- **Plans, loadouts, saved ship setups, RRR stock, theme and other settings** are stored in each visitor's own browser (localStorage), on their own machine. Nothing is sent to a server.
- A new visitor starts with an empty plan.
- **Loadouts → Export loadouts** saves them to a `.json` file, and **Import loadouts** loads such a file on another browser or device. Use this to move your setups from the Claude-hosted copy to the GitHub Pages copy.
- When the same page is opened inside claude.ai as an artifact, it uses Claude's artifact storage instead, so loadouts there follow your Claude account.

## Rebuilding

See `HANDOFF.md`. In short:

1. `python tools/fetch_assets.py`
2. `python tools/find_topdown.py`
3. `python tools/topdown.py`
4. `python tools/fetch_loadouts.py`
5. `python tools/fetch_wiki_dims.py`
6. `python build.py STAR_CITIZEN_SHIP_FITTING_LIST.xlsx`

## Sources

- Fit data: Pegaxsus Ship Fit List (LIVE 4.10.3).
- Ship sizes, images and the Liberator size (122 × 68 m): starcitizen.tools.
- Loadouts, mass and in-game prices: api.star-citizen.wiki (game data, UEX prices).
- Liberator top-down: scorg.tools.
