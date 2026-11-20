# Ship size audit

Length × width in metres. The planner uses **overrides > RSI store page > game data > wiki**. Overrides (`tools/dim_overrides.json`) are measured landed widths for folding-wing ships and sizes the user chose. Game data is api.star-citizen.wiki, extracted from the game files (often padded boxes, full wingspans or extended lengths).

## Store page vs game data conflicts (63)

| Variant | RSI store page (used) | Game data | Wiki |
|---|---|---|---|
| 85X Limited | 13 × 10 | 14 × 13.5 | 13 × 10 |
| ATLS | 1.8 × 2 | 3.2 × 1.6 | 1.8 × 2 |
| ATLS GEO | 1.8 × 2 | 3.2 × 1.6 | 1.8 × 2 |
| Aurora Mk II | 27.5 × 10.5 | 27.7 × 27.4 | 24.5 × 28 |
| Avenger Stalker | 22.5 × 16.5 | 20 × 15 | 20 × 15 |
| Avenger Titan | 22.5 × 16.5 | 20 × 15 | 20 × 15 |
| Avenger Titan Renegade | 22.5 × 16.5 | 20 × 15 | 20 × 15 |
| Avenger Warlock | 22.5 × 16.5 | 20 × 15 | 20 × 15 |
| Blade | 21 × 21 | 20.5 × 16.5 | 24 × 20 |
| C8 Pisces | 12 × 10 | 16 × 12 | 13 × 10 |
| C8X Pisces Expedition | 13 × 10 | 16 × 12 | 13 × 10 |
| CSV-SM | 5.4 × 4.1 | 8.75 × 6 | 5.44 × 4.13 |
| Clipper | 26.5 × 18 | 26.5 × 21 | 26.5 × 50 |
| Cutlass Black | 29 × 26.5 | 37.5 × 26.5 | 37.5 × 26.5 |
| Cutter | 20 × 13 | 20 × 16 | 20 × 13 |
| Cutter Rambler | 20 × 13 | 20 × 16 | 20 × 13 |
| Cutter Scout | 20 × 13 | 20 × 16 | 20 × 16 |
| Cyclone | 6 × 4 | 8.75 × 6 | 6 × 4 |
| Cyclone AA | 6 × 4 | 8.75 × 6 | 6 × 4 |
| Cyclone MT | 6 × 4 | 8.75 × 6 | 6 × 4 |
| Cyclone RC | 6 × 4 | 8.75 × 6 | 6 × 4 |
| Cyclone RN | 6 × 4 | 8.75 × 6 | 6 × 4 |
| Cyclone TR | 6 × 4 | 8.75 × 6 | 6 × 4 |
| Defender | 25.5 × 20 | 24.5 × 24.5 | 24.5 × 24.5 |
| Eclipse | 20.5 × 36.6 | 24.5 × 24.5 | 24.5 × 24.5 |
| F7A Hornet Mk I | 22.5 × 21 | 28.25 × 25.5 | 22.5 × 22 |
| F7C Hornet Mk I | 22.5 × 21.5 | 28.25 × 25.5 | 22.5 × 21.5 |
| F7C-M Super Hornet Mk II | 24 × 19 | 24 × 24 | 24 × 24 |
| F7C-R Hornet Tracker Mk II | 22.5 × 15 | 22.5 × 22 | 22.5 × 21 |
| F7C-S Hornet Ghost Mk II | 22.5 × 15 | 22.5 × 22 | 22.5 × 15 |
| Glaive | 31 × 20 | 33 × 24 | 27 × 20.1 |
| Golem OX | 15.5 × 10 | 15.5 × 7 | 15.5 × 7 |
| Guardian MX | 25 × 20 | 26 × 17 | 25 × 16.5 |
| HoverQuad | 4.5 × 2.5 | 5.15 × 1.45 | 4.5 × 2.5 |
| Hurricane | 22 × 14.5 | 24 × 18.5 | 22 × 18.2 |
| M80 | 32 × 17.3 | 11.5 × 11 | 32 × 17.3 |
| MDC | 7 × 5.5 | 8.75 × 6 | 8.75 × 6 |
| MISC Hull A | 24 × 10 | 30 × 12.5 | 24 × 10 |
| MISC Hull B | 46 × 17 | 71 × 16.7 | 71 × 17 |
| MPUV Cargo | 9 × 8.5 | 10.5 × 9 | 9.5 × 8.5 |
| MPUV Personnel | 9 × 6.5 | 10.5 × 9 | 9.25 × 8.5 |
| MPUV Tractor | 9 × 8.5 | 10.5 × 9 | 9 × 8.5 |
| MTC | 7 × 5.5 | 8.75 × 6 | 8.75 × 6 |
| Mule | 4.2 × 3 | 8.75 × 6 | 4.2 × 3 |
| Mustang Omega | 17.5 × 15.5 | 21.5 × 18 | 21.5 × 18 |
| Nova | 16 × 7 | 20 × 12 | 16 × 7 |
| Pitbull | 3.9 × 5.9 | 6 × 6 | 5.93 × 6.13 |
| Pulse | 3.1 × 0.9 | 3.5 × 2.5 | 3.15 × 0.9 |
| Pulse LX | 3.1 × 0.9 | 3.5 × 2.5 | 3.5 × 2.5 |
| S-65 Stingray | 24.5 × 16.4 | 20.447 × 15.1 | 22.15 × 24.3 |
| STV | 4.2 × 2.8 | 8.75 × 6 | 4.2 × 2.8 |
| Sabre Firebird | 26 × 30 | 24.5 × 24.5 | 26 × 30 |
| Sabre Raven | 24 × 20.5 | 24.5 × 24.5 | 24.5 × 24.5 |
| Skylark | 6.5 × 4 | 7 × 6.5 | 7 × 6.5 |
| Talon | 26 × 23.5 | 24 × 15 | 26 × 23.3 |
| Talon Shrike | 26 × 23.5 | 24 × 15 | 24 × 15 |
| Terrapin | 19.5 × 14.5 | 20 × 16.5 | 19.5 × 14.5 |
| Ursa | 7.6 × 5.5 | 8.75 × 6 | 7.75 × 5.7 |
| Ursa Fortuna | 7.6 × 5.5 | 8.75 × 6 | 7.75 × 5.7 |
| Vanguard Harbinger | 38.5 × 40 | 48 × 40 | 38.5 × 40 |
| Vanguard Hoplite | 38.5 × 40 | 48 × 40 | 38.5 × 40 |
| Vanguard Sentinel | 38.5 × 40 | 48 × 40 | 38.5 × 40 |
| Vanguard Warden | 38.5 × 40 | 48 × 40 | 38.5 × 40 |

## All variants (168)

| Variant | Planner | From | Game data | RSI store page | Wiki | Conflict |
|---|---|---|---|---|---|---|
| 100i | 19.3 × 11 | store page | 19 × 12 | 19.3 × 11 | 19 × 11 |  |
| 125a | 19.3 × 11 | store page | 19 × 12 | 19.3 × 11 | 19 × 11 |  |
| 135c | 19.3 × 11 | store page | 19 × 12 | 19.3 × 11 | 19 × 11 |  |
| 300i | 27 × 17 | store page | 27 × 17 | 27 × 17 | 27 × 17 |  |
| 315p | 27 × 17 | store page | 27 × 17 | 27 × 17 | 27 × 17 |  |
| 325a | 27 × 17 | store page | 27.5 × 17 | 27 × 17 | 27 × 17 |  |
| 350r | 25 × 17 | store page | 27 × 17 | 25 × 17 | 27 × 17 |  |
| 85X Limited | 13 × 10 | store page | 14 × 13.5 | 13 × 10 | 13 × 10 | ⚠ |
| ATLS | 1.8 × 2 | store page | 3.2 × 1.6 | 1.8 × 2 | 1.8 × 2 | ⚠ |
| ATLS GEO | 1.8 × 2 | store page | 3.2 × 1.6 | 1.8 × 2 | 1.8 × 2 | ⚠ |
| Ares Star Fighter Inferno | 30 × 27 | game data | 30 × 27 | — | 27 × 30 |  |
| Ares Star Fighter Ion | 30 × 27 | game data | 30 × 27 | — | 27 × 30 |  |
| Argo ATLS GEO IKTI | 3.2 × 1.6 | game data | 3.2 × 1.6 | — | 1.8 × 2 |  |
| Argo ATLS IKTI | 3.2 × 1.6 | game data | 3.2 × 1.6 | — | 1.8 × 2 |  |
| Arrow | 16 × 11.1 | override | 17.25 × 12.25 | 16 × 12 | 16 × 12 |  |
| Aurora Mk I CL | 19 × 8 | store page | 19 × 8.75 | 19 × 8 | 19 × 8.75 |  |
| Aurora Mk I ES | 19 × 8.7 | store page | 19 × 8.75 | 19 × 8.7 | 19 × 8.75 |  |
| Aurora Mk I LN | 19 × 8.7 | store page | 19 × 8.75 | 19 × 8.7 | 19 × 8.75 |  |
| Aurora Mk I LX | 19 × 8.7 | store page | 19 × 8.75 | 19 × 8.7 | 19 × 8.75 |  |
| Aurora Mk I MR | 19 × 8.7 | store page | 19 × 8.75 | 19 × 8.7 | 18 × 8 |  |
| Aurora Mk I SE | 18.5 × 8.2 | store page | 19 × 8.75 | 18.5 × 8.2 | 18.5 × 8.25 |  |
| Aurora Mk II | 27.5 × 10.5 | store page | 27.7 × 27.4 | 27.5 × 10.5 | 24.5 × 28 | ⚠ |
| Avenger Stalker | 22.5 × 16.5 | store page | 20 × 15 | 22.5 × 16.5 | 20 × 15 | ⚠ |
| Avenger Titan | 22.5 × 16.5 | store page | 20 × 15 | 22.5 × 16.5 | 20 × 15 | ⚠ |
| Avenger Titan Renegade | 22.5 × 16.5 | store page | 20 × 15 | 22.5 × 16.5 | 20 × 15 | ⚠ |
| Avenger Warlock | 22.5 × 16.5 | store page | 20 × 15 | 22.5 × 16.5 | 20 × 15 | ⚠ |
| Basher | 13.7 × 11.3 | store page | 13.7 × 11.3 | 13.7 × 11.3 | 13.7 × 11.3 |  |
| Blade | 21 × 21 | store page | 20.5 × 16.5 | 21 × 21 | 24 × 20 | ⚠ |
| Buccaneer | 15 × 16 | store page | 16.75 × 15.25 | 15 × 16 | 15 × 16 |  |
| C8 Pisces | 12 × 10 | store page | 16 × 12 | 12 × 10 | 13 × 10 | ⚠ |
| C8R Pisces Rescue | 16 × 12 | game data | 16 × 12 | — | 13 × 10 |  |
| C8X Pisces Expedition | 13 × 10 | store page | 16 × 12 | 13 × 10 | 13 × 10 | ⚠ |
| CSV-SM | 5.4 × 4.1 | store page | 8.75 × 6 | 5.4 × 4.1 | 5.44 × 4.13 | ⚠ |
| Clipper | 26.5 × 16 | override | 26.5 × 21 | 26.5 × 18 | 26.5 × 50 | ⚠ |
| Command Module | 20 × 16 | game data | 20 × 16 | — | 20 × 16 |  |
| Cutlass Black | 29 × 26.5 | store page | 37.5 × 26.5 | 29 × 26.5 | 37.5 × 26.5 | ⚠ |
| Cutlass Blue | 36 × 26 | store page | 37.5 × 26.5 | 36 × 26 | 37.5 × 26.5 |  |
| Cutlass Red | 36 × 26 | store page | 37.5 × 26.5 | 36 × 26 | 37.5 × 26.5 |  |
| Cutlass Steel | 36 × 26.5 | store page | 37.5 × 26.5 | 36 × 26.5 | 37.5 × 26.5 |  |
| Cutter | 20 × 13 | store page | 20 × 16 | 20 × 13 | 20 × 13 | ⚠ |
| Cutter Rambler | 20 × 13 | store page | 20 × 16 | 20 × 13 | 20 × 13 | ⚠ |
| Cutter Scout | 20 × 13 | store page | 20 × 16 | 20 × 13 | 20 × 16 | ⚠ |
| Cyclone | 6 × 4 | store page | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone AA | 6 × 4 | store page | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone MT | 6 × 4 | store page | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone RC | 6 × 4 | store page | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone RN | 6 × 4 | store page | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone TR | 6 × 4 | store page | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Defender | 25.5 × 20 | store page | 24.5 × 24.5 | 25.5 × 20 | 24.5 × 24.5 | ⚠ |
| Dragonfly | 7 × 2.5 | game data | 7 × 2.5 | — | 6 × 2.5 |  |
| Dragonfly Yellowjacket | 8 × 3 | store page | 7 × 2.5 | 8 × 3 | 7 × 2.5 |  |
| Eclipse | 20.5 × 36.6 | store page | 24.5 × 24.5 | 20.5 × 36.6 | 24.5 × 24.5 | ⚠ |
| F7A Hornet Mk I | 22.5 × 21 | store page | 28.25 × 25.5 | 22.5 × 21 | 22.5 × 22 | ⚠ |
| F7A Hornet Mk II | 22.5 × 22 | store page | 22.5 × 22 | 22.5 × 22 | 22.5 × 21.75 |  |
| F7C Hornet Mk I | 22.5 × 21.5 | store page | 28.25 × 25.5 | 22.5 × 21.5 | 22.5 × 21.5 | ⚠ |
| F7C Hornet Mk II | 22.2 × 22 | store page | 22.5 × 22 | 22.2 × 22 | 22.5 × 21 |  |
| F7C-M Super Hornet Mk II | 24 × 19 | store page | 24 × 24 | 24 × 19 | 24 × 24 | ⚠ |
| F7C-R Hornet Tracker Mk II | 22.5 × 15 | store page | 22.5 × 22 | 22.5 × 15 | 22.5 × 21 | ⚠ |
| F7C-S Hornet Ghost Mk II | 22.5 × 15 | store page | 22.5 × 22 | 22.5 × 15 | 22.5 × 15 | ⚠ |
| F8A Lightning | 26 × 25 | game data | 26 × 25 | — | 26 × 24 |  |
| F8C Lightning | 25 × 24 | store page | 26 × 25 | 25 × 24 | 26 × 25 |  |
| Fury | 7 × 5.4 | store page | 7 × 5.4 | 7 × 5.4 | 8 × 5.4 |  |
| Fury LX | 7 × 5.4 | store page | 7 × 5.4 | 7 × 5.4 | 7 × 5.4 |  |
| Fury MX | 7 × 5.4 | store page | 7 × 5.4 | 7 × 5.4 | 7 × 5.4 |  |
| Gladiator | 22.3 × 22 | store page | 22.75 × 21 | 22.3 × 22 | 22.5 × 22.5 |  |
| Gladius | 20 × 17 | store page | 21 × 17.5 | 20 × 17 | 20 × 17 |  |
| Gladius Pirate | 21 × 17.5 | game data | 21 × 17.5 | — | 21 × 17.5 |  |
| Gladius Valiant | 20 × 16 | store page | 21 × 17.5 | 20 × 16 | 21 × 17.5 |  |
| Glaive | 31 × 20 | store page | 33 × 24 | 31 × 20 | 27 × 20.1 | ⚠ |
| Golem | 15.5 × 7 | store page | 15.5 × 7 | 15.5 × 7 | 15.5 × 7 |  |
| Golem OX | 15.5 × 10 | store page | 15.5 × 7 | 15.5 × 10 | 15.5 × 7 | ⚠ |
| Guardian | 25 × 16.5 | store page | 24.3 × 16.3 | 25 × 16.5 | 25 × 16.5 |  |
| Guardian MX | 25 × 20 | store page | 26 × 17 | 25 × 20 | 25 × 16.5 | ⚠ |
| Guardian QI | 25 × 16.5 | store page | 24.3 × 16.3 | 25 × 16.5 | 25 × 16.5 |  |
| HM6 Ballista | 17 × 7 | store page | 17 × 7 | 17 × 7 | 17 × 7 |  |
| HM6 Centurion | 17 × 7 | store page | 17 × 7 | 17 × 7 | 17 × 7 |  |
| HM6 Spartan | 17 × 7 | store page | 17 × 7 | 17 × 7 | 17 × 7 |  |
| Hawk | 17 × 22 | store page | 23 × 17 | 17 × 22 | 17 × 22 |  |
| Herald | 23.5 × 12.5 | store page | 24.75 × 12.5 | 23.5 × 12.5 | 23.5 × 12.5 |  |
| HoverQuad | 4.5 × 2.5 | store page | 5.15 × 1.45 | 4.5 × 2.5 | 4.5 × 2.5 | ⚠ |
| Hurricane | 22 × 14.5 | store page | 24 × 18.5 | 22 × 14.5 | 22 × 18.2 | ⚠ |
| Hyun | 36.8 × 31.9 | game data | 36.8 × 31.9 | — | 36.8 × 31.9 |  |
| Intrepid | 23.2 × 20.3 | store page | 23.07 × 20.18 | 23.2 × 20.3 | 23.2 × 20.3 |  |
| Khartu-al | 30.5 × 13 | store page | 32 × 13.5 | 30.5 × 13 | 15 × 21.5 |  |
| L-21 Wolf | 21.5 × 10.5 | store page | 21.5 × 10.5 | 21.5 × 10.5 | 21.5 × 10.5 |  |
| L-22 Alpha Wolf | 21.5 × 10.5 | store page | 21.5 × 10.5 | 21.5 × 10.5 | 21.5 × 10.5 |  |
| Lynx | 7.7 × 5.7 | store page | 7.75 × 5.7 | 7.7 × 5.7 | 7.75 × 5.7 |  |
| M50 Interceptor | 11.5 × 11 | game data | 11.5 × 11 | — | 11.5 × 11 |  |
| M80 | 32 × 17.3 | store page | 11.5 × 11 | 32 × 17.3 | 32 × 17.3 | ⚠ |
| MDC | 7 × 5.5 | store page | 8.75 × 6 | 7 × 5.5 | 8.75 × 6 | ⚠ |
| MISC Fortune | 26 × 16 | store page | 26.5 × 16.5 | 26 × 16 | 26 × 16 |  |
| MISC Freelancer | 38 × 23.5 | store page | 38 × 23.5 | 38 × 23.5 | 38 × 23.5 |  |
| MISC Freelancer DUR | 38 × 23.5 | store page | 38 × 23.5 | 38 × 23.5 | 38 × 23.5 |  |
| MISC Freelancer MIS | 38 × 23.5 | store page | 38 × 23.5 | 38 × 23.5 | 38 × 23.5 |  |
| MISC Hull A | 24 × 10 | store page | 30 × 12.5 | 24 × 10 | 24 × 10 | ⚠ |
| MISC Hull B | 46 × 17 | override | 71 × 16.7 | 46 × 17 | 71 × 17 | ⚠ |
| MISC Prospector | 24 × 15 | store page | 26.5 × 16.5 | 24 × 15 | 26 × 16 |  |
| MISC Reliant Kore | 14.5 × 28.5 | store page | 28.5 × 14.75 | 14.5 × 28.5 | 14.5 × 10.8 |  |
| MISC Reliant Mako | 14.5 × 28.5 | store page | 28.5 × 14.75 | 14.5 × 28.5 | 28.5 × 14.75 |  |
| MISC Reliant Sen | 14.5 × 28.5 | store page | 28.5 × 14.75 | 14.5 × 28.5 | 28.5 × 14.75 |  |
| MISC Reliant Tana | 14.5 × 28.5 | store page | 28.5 × 14.75 | 14.5 × 28.5 | 28.5 × 14.75 |  |
| MISC Starlite | 32 × 19 | store page | 32 × 19.9 | 32 × 19 | 32 × 19.9 |  |
| MPUV Cargo | 9 × 8.5 | store page | 10.5 × 9 | 9 × 8.5 | 9.5 × 8.5 | ⚠ |
| MPUV Personnel | 9 × 6.5 | store page | 10.5 × 9 | 9 × 6.5 | 9.25 × 8.5 | ⚠ |
| MPUV Tractor | 9 × 8.5 | store page | 10.5 × 9 | 9 × 8.5 | 9 × 8.5 | ⚠ |
| MTC | 7 × 5.5 | store page | 8.75 × 6 | 7 × 5.5 | 8.75 × 6 | ⚠ |
| Mantis | 30 × 17 | store page | 30 × 17 | 30 × 17 | 30 × 17 |  |
| Marauder | 20.5 × 18.5 | store page | 20 × 19 | 20.5 × 18.5 | 20 × 19 |  |
| Meteor | 30 × 17 | store page | 30 × 17 | 30 × 17 | 30 × 17 |  |
| Mule | 4.2 × 3 | store page | 8.75 × 6 | 4.2 × 3 | 4.2 × 3 | ⚠ |
| Mustang Alpha | 21.5 × 18 | store page | 21.5 × 18 | 21.5 × 18 | 21.5 × 18 |  |
| Mustang Beta | 21.5 × 18 | store page | 21.5 × 18 | 21.5 × 18 | 21.5 × 18 |  |
| Mustang Delta | 21.5 × 18 | store page | 21.5 × 18 | 21.5 × 18 | 21.5 × 18 |  |
| Mustang Gamma | 21.5 × 18 | store page | 21.5 × 18 | 21.5 × 18 | 21.5 × 18 |  |
| Mustang Omega | 17.5 × 15.5 | store page | 21.5 × 18 | 17.5 × 15.5 | 21.5 × 18 | ⚠ |
| Nomad | 26.5 × 18.3 | store page | 27 × 19 | 26.5 × 18.3 | 27 × 19 |  |
| Nova | 16 × 7 | store page | 20 × 12 | 16 × 7 | 16 × 7 | ⚠ |
| Nox | 5.5 × 1.5 | store page | 5.15 × 1.45 | 5.5 × 1.5 | 5.15 × 1.5 |  |
| Nox Kue | 5.5 × 1.5 | store page | 5.15 × 1.45 | 5.5 × 1.5 | 5.5 × 1.5 |  |
| P-52 Merlin | 12 × 7.7 | store page | 12 × 7.75 | 12 × 7.7 | 12 × 7.7 |  |
| P-72 Archimedes | 12 × 7.7 | store page | 12 × 7.75 | 12 × 7.7 | 12 × 7.7 |  |
| PTV | 3 × 2 | store page | 3.5 × 2.5 | 3 × 2 | 3.5 × 2.5 |  |
| Pitbull | 3.9 × 5.9 | store page | 6 × 6 | 3.9 × 5.9 | 5.93 × 6.13 | ⚠ |
| Prowler | 34 × 32 | store page | 34 × 32 | 34 × 32 | 34 × 32 |  |
| Prowler Utility | 34 × 32 | store page | 34 × 32 | 34 × 32 | 34 × 32 |  |
| Pulse | 3.1 × 0.9 | store page | 3.5 × 2.5 | 3.1 × 0.9 | 3.15 × 0.9 | ⚠ |
| Pulse LX | 3.1 × 0.9 | store page | 3.5 × 2.5 | 3.1 × 0.9 | 3.5 × 2.5 | ⚠ |
| ROC | 5.1 × 3.8 | store page | 6 × 3.9 | 5.1 × 3.8 | 6 × 3.9 |  |
| ROC-DS | 6.6 × 5 | store page | 6.6 × 5 | 6.6 × 5 | 6.6 × 5 |  |
| Razor | 11.5 × 8.2 | store page | 12.5 × 9 | 11.5 × 8.2 | 11.5 × 8.2 |  |
| Razor EX | 11.5 × 8.2 | store page | 12.5 × 9 | 11.5 × 8.2 | 12.5 × 9 |  |
| Razor LX | 11.5 × 8.2 | store page | 12.5 × 9 | 11.5 × 8.2 | 12.5 × 9 |  |
| Redeemer | 51 × 23.5 | store page | 51 × 25 | 51 × 23.5 | 51 × 25 |  |
| S-65 Stingray | 24.5 × 16.4 | store page | 20.447 × 15.1 | 24.5 × 16.4 | 22.15 × 24.3 | ⚠ |
| SRV | 28.5 × 19.5 | store page | 31.5 × 21.5 | 28.5 × 19.5 | 28.5 × 19.5 |  |
| STV | 4.2 × 2.8 | store page | 8.75 × 6 | 4.2 × 2.8 | 4.2 × 2.8 | ⚠ |
| Sabre | 26 × 24 | store page | 24.5 × 24.5 | 26 × 24 | 24 × 26 |  |
| Sabre Comet | 24 × 26 | store page | 24.5 × 24.5 | 24 × 26 | 24.5 × 24.5 |  |
| Sabre Firebird | 26 × 30 | store page | 24.5 × 24.5 | 26 × 30 | 26 × 30 | ⚠ |
| Sabre Peregrine | 26 × 24 | store page | 24.5 × 24.5 | 26 × 24 | 26 × 24 |  |
| Sabre Raven | 24 × 20.5 | store page | 24.5 × 24.5 | 24 × 20.5 | 24.5 × 24.5 | ⚠ |
| Salvation | 14.5 × 8.5 | store page | 14.5 × 8.5 | 14.5 × 8.5 | 14.5 × 8.5 |  |
| San'tok.yāi | 24 × 23 | store page | 24 × 23 | 24 × 23 | 22 × 23 |  |
| Scorpius | 24 × 32 | store page | 32 × 24 | 24 × 32 | 24 × 32 |  |
| Scorpius Antares | 24 × 32 | store page | 32 × 24 | 24 × 32 | 32 × 24 |  |
| Shiv | 36 × 28 | store page | 37.5 × 26.5 | 36 × 28 | 37.5 × 26.5 |  |
| Skylark | 6.5 × 4 | store page | 7 × 6.5 | 6.5 × 4 | 7 × 6.5 | ⚠ |
| Storm | 10.5 × 7.5 | store page | 10.25 × 7.65 | 10.5 × 7.5 | 10.5 × 7.5 |  |
| Storm AA | 10.5 × 7.5 | store page | 10.25 × 7.65 | 10.5 × 7.5 | 10.5 × 7.5 |  |
| Talon | 26 × 23.5 | store page | 24 × 15 | 26 × 23.5 | 26 × 23.3 | ⚠ |
| Talon Shrike | 26 × 23.5 | store page | 24 × 15 | 26 × 23.5 | 24 × 15 | ⚠ |
| Terrapin | 19.5 × 14.5 | store page | 20 × 16.5 | 19.5 × 14.5 | 19.5 × 14.5 | ⚠ |
| Terrapin Medic | 19.5 × 16.7 | store page | 20 × 16.5 | 19.5 × 16.7 | 20 × 16.5 |  |
| UTV | 4 × 2.6 | store page | 4 × 2.6 | 4 × 2.6 | 4 × 2.6 |  |
| Ursa | 7.6 × 5.5 | store page | 8.75 × 6 | 7.6 × 5.5 | 7.75 × 5.7 | ⚠ |
| Ursa Fortuna | 7.6 × 5.5 | store page | 8.75 × 6 | 7.6 × 5.5 | 7.75 × 5.7 | ⚠ |
| Ursa Medivac | 8 × 5.5 | store page | 8.75 × 6 | 8 × 5.5 | 8 × 5.5 |  |
| Vanduul Scythe | 31 × 23 | store page | 33 × 24 | 31 × 23 | 39 × 26.46 |  |
| Vanguard Harbinger | 38.5 × 40 | store page | 48 × 40 | 38.5 × 40 | 38.5 × 40 | ⚠ |
| Vanguard Hoplite | 38.5 × 40 | store page | 48 × 40 | 38.5 × 40 | 38.5 × 40 | ⚠ |
| Vanguard Sentinel | 38.5 × 40 | store page | 48 × 40 | 38.5 × 40 | 38.5 × 40 | ⚠ |
| Vanguard Warden | 38.5 × 40 | store page | 48 × 40 | 38.5 × 40 | 38.5 × 40 | ⚠ |
| Vulture | 33 × 16 | store page | 34 × 16 | 33 × 16 | 34 × 16 |  |
| X1 | 5.5 × 1.3 | store page | 5.19 × 1.87 | 5.5 × 1.3 | 5.5 × 1.3 |  |
| X1 Force | 5.5 × 1.3 | store page | 5.19 × 1.87 | 5.5 × 1.3 | 5.5 × 1.3 |  |
| X1 Velocity | 5.5 × 1.3 | store page | 5.19 × 1.87 | 5.5 × 1.3 | 5.5 × 1.3 |  |
| Zeus Mk II CL | 45.7 × 34.3 | store page | 46 × 35 | 45.7 × 34.3 | 45.69 × 34.3 |  |
| Zeus Mk II ES | 45.7 × 34.3 | store page | 46 × 35 | 45.7 × 34.3 | 45.7 × 34.3 |  |
