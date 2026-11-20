# Ship size audit

Length × width in metres. The planner uses **game data > RSI store page > wiki**. Ships whose wings fold when landed use a measured landed width (see `tools/dim_overrides.json`).

## Store page vs game data conflicts (63)

| Variant | Game data (used) | RSI store page | Wiki |
|---|---|---|---|
| 85X Limited | 14 × 13.5 | 13 × 10 | 13 × 10 |
| ATLS | 3.2 × 1.6 | 1.8 × 2 | 1.8 × 2 |
| ATLS GEO | 3.2 × 1.6 | 1.8 × 2 | 1.8 × 2 |
| Aurora Mk II | 27.7 × 27.4 | 27.5 × 10.5 | 24.5 × 28 |
| Avenger Stalker | 20 × 15 | 22.5 × 16.5 | 20 × 15 |
| Avenger Titan | 20 × 15 | 22.5 × 16.5 | 20 × 15 |
| Avenger Titan Renegade | 20 × 15 | 22.5 × 16.5 | 20 × 15 |
| Avenger Warlock | 20 × 15 | 22.5 × 16.5 | 20 × 15 |
| Blade | 20.5 × 16.5 | 21 × 21 | 24 × 20 |
| C8 Pisces | 16 × 12 | 12 × 10 | 13 × 10 |
| C8X Pisces Expedition | 16 × 12 | 13 × 10 | 13 × 10 |
| CSV-SM | 8.75 × 6 | 5.4 × 4.1 | 5.44 × 4.13 |
| Clipper | 26.5 × 21 | 26.5 × 18 | 26.5 × 50 |
| Cutlass Black | 37.5 × 26.5 | 29 × 26.5 | 37.5 × 26.5 |
| Cutter | 20 × 16 | 20 × 13 | 20 × 13 |
| Cutter Rambler | 20 × 16 | 20 × 13 | 20 × 13 |
| Cutter Scout | 20 × 16 | 20 × 13 | 20 × 16 |
| Cyclone | 8.75 × 6 | 6 × 4 | 6 × 4 |
| Cyclone AA | 8.75 × 6 | 6 × 4 | 6 × 4 |
| Cyclone MT | 8.75 × 6 | 6 × 4 | 6 × 4 |
| Cyclone RC | 8.75 × 6 | 6 × 4 | 6 × 4 |
| Cyclone RN | 8.75 × 6 | 6 × 4 | 6 × 4 |
| Cyclone TR | 8.75 × 6 | 6 × 4 | 6 × 4 |
| Defender | 24.5 × 24.5 | 25.5 × 20 | 24.5 × 24.5 |
| Eclipse | 24.5 × 24.5 | 20.5 × 36.6 | 24.5 × 24.5 |
| F7A Hornet Mk I | 28.25 × 25.5 | 22.5 × 21 | 22.5 × 22 |
| F7C Hornet Mk I | 28.25 × 25.5 | 22.5 × 21.5 | 22.5 × 21.5 |
| F7C-M Super Hornet Mk II | 24 × 24 | 24 × 19 | 24 × 24 |
| F7C-R Hornet Tracker Mk II | 22.5 × 22 | 22.5 × 15 | 22.5 × 21 |
| F7C-S Hornet Ghost Mk II | 22.5 × 22 | 22.5 × 15 | 22.5 × 15 |
| Glaive | 33 × 24 | 31 × 20 | 27 × 20.1 |
| Golem OX | 15.5 × 7 | 15.5 × 10 | 15.5 × 7 |
| Guardian MX | 26 × 17 | 25 × 20 | 25 × 16.5 |
| HoverQuad | 5.15 × 1.45 | 4.5 × 2.5 | 4.5 × 2.5 |
| Hurricane | 24 × 18.5 | 22 × 14.5 | 22 × 18.2 |
| M80 | 11.5 × 11 | 32 × 17.3 | 32 × 17.3 |
| MDC | 8.75 × 6 | 7 × 5.5 | 8.75 × 6 |
| MISC Hull A | 30 × 12.5 | 24 × 10 | 24 × 10 |
| MISC Hull B | 71 × 16.7 | 46 × 17 | 71 × 17 |
| MPUV Cargo | 10.5 × 9 | 9 × 8.5 | 9.5 × 8.5 |
| MPUV Personnel | 10.5 × 9 | 9 × 6.5 | 9.25 × 8.5 |
| MPUV Tractor | 10.5 × 9 | 9 × 8.5 | 9 × 8.5 |
| MTC | 8.75 × 6 | 7 × 5.5 | 8.75 × 6 |
| Mule | 8.75 × 6 | 4.2 × 3 | 4.2 × 3 |
| Mustang Omega | 21.5 × 18 | 17.5 × 15.5 | 21.5 × 18 |
| Nova | 20 × 12 | 16 × 7 | 16 × 7 |
| Pitbull | 6 × 6 | 3.9 × 5.9 | 5.93 × 6.13 |
| Pulse | 3.5 × 2.5 | 3.1 × 0.9 | 3.15 × 0.9 |
| Pulse LX | 3.5 × 2.5 | 3.1 × 0.9 | 3.5 × 2.5 |
| S-65 Stingray | 20.447 × 15.1 | 24.5 × 16.4 | 22.15 × 24.3 |
| STV | 8.75 × 6 | 4.2 × 2.8 | 4.2 × 2.8 |
| Sabre Firebird | 24.5 × 24.5 | 26 × 30 | 26 × 30 |
| Sabre Raven | 24.5 × 24.5 | 24 × 20.5 | 24.5 × 24.5 |
| Skylark | 7 × 6.5 | 6.5 × 4 | 7 × 6.5 |
| Talon | 24 × 15 | 26 × 23.5 | 26 × 23.3 |
| Talon Shrike | 24 × 15 | 26 × 23.5 | 24 × 15 |
| Terrapin | 20 × 16.5 | 19.5 × 14.5 | 19.5 × 14.5 |
| Ursa | 8.75 × 6 | 7.6 × 5.5 | 7.75 × 5.7 |
| Ursa Fortuna | 8.75 × 6 | 7.6 × 5.5 | 7.75 × 5.7 |
| Vanguard Harbinger | 48 × 40 | 38.5 × 40 | 38.5 × 40 |
| Vanguard Hoplite | 48 × 40 | 38.5 × 40 | 38.5 × 40 |
| Vanguard Sentinel | 48 × 40 | 38.5 × 40 | 38.5 × 40 |
| Vanguard Warden | 48 × 40 | 38.5 × 40 | 38.5 × 40 |

## All variants (168)

| Variant | Planner | From | Game data | RSI store page | Wiki | Conflict |
|---|---|---|---|---|---|---|
| 100i | 19 × 12 | game data | 19 × 12 | 19.3 × 11 | 19 × 11 |  |
| 125a | 19 × 12 | game data | 19 × 12 | 19.3 × 11 | 19 × 11 |  |
| 135c | 19 × 12 | game data | 19 × 12 | 19.3 × 11 | 19 × 11 |  |
| 300i | 27 × 17 | game data | 27 × 17 | 27 × 17 | 27 × 17 |  |
| 315p | 27 × 17 | game data | 27 × 17 | 27 × 17 | 27 × 17 |  |
| 325a | 27.5 × 17 | game data | 27.5 × 17 | 27 × 17 | 27 × 17 |  |
| 350r | 27 × 17 | game data | 27 × 17 | 25 × 17 | 27 × 17 |  |
| 85X Limited | 14 × 13.5 | game data | 14 × 13.5 | 13 × 10 | 13 × 10 | ⚠ |
| ATLS | 3.2 × 1.6 | game data | 3.2 × 1.6 | 1.8 × 2 | 1.8 × 2 | ⚠ |
| ATLS GEO | 3.2 × 1.6 | game data | 3.2 × 1.6 | 1.8 × 2 | 1.8 × 2 | ⚠ |
| Ares Star Fighter Inferno | 30 × 27 | game data | 30 × 27 | — | 27 × 30 |  |
| Ares Star Fighter Ion | 30 × 27 | game data | 30 × 27 | — | 27 × 30 |  |
| Argo ATLS GEO IKTI | 3.2 × 1.6 | game data | 3.2 × 1.6 | — | 1.8 × 2 |  |
| Argo ATLS IKTI | 3.2 × 1.6 | game data | 3.2 × 1.6 | — | 1.8 × 2 |  |
| Arrow | 16 × 11.1 | override | 17.25 × 12.25 | 16 × 12 | 16 × 12 |  |
| Aurora Mk I CL | 19 × 8.75 | game data | 19 × 8.75 | 19 × 8 | 19 × 8.75 |  |
| Aurora Mk I ES | 19 × 8.75 | game data | 19 × 8.75 | 19 × 8.7 | 19 × 8.75 |  |
| Aurora Mk I LN | 19 × 8.75 | game data | 19 × 8.75 | 19 × 8.7 | 19 × 8.75 |  |
| Aurora Mk I LX | 19 × 8.75 | game data | 19 × 8.75 | 19 × 8.7 | 19 × 8.75 |  |
| Aurora Mk I MR | 19 × 8.75 | game data | 19 × 8.75 | 19 × 8.7 | 18 × 8 |  |
| Aurora Mk I SE | 19 × 8.75 | game data | 19 × 8.75 | 18.5 × 8.2 | 18.5 × 8.25 |  |
| Aurora Mk II | 27.7 × 27.4 | game data | 27.7 × 27.4 | 27.5 × 10.5 | 24.5 × 28 | ⚠ |
| Avenger Stalker | 20 × 15 | game data | 20 × 15 | 22.5 × 16.5 | 20 × 15 | ⚠ |
| Avenger Titan | 20 × 15 | game data | 20 × 15 | 22.5 × 16.5 | 20 × 15 | ⚠ |
| Avenger Titan Renegade | 20 × 15 | game data | 20 × 15 | 22.5 × 16.5 | 20 × 15 | ⚠ |
| Avenger Warlock | 20 × 15 | game data | 20 × 15 | 22.5 × 16.5 | 20 × 15 | ⚠ |
| Basher | 13.7 × 11.3 | game data | 13.7 × 11.3 | 13.7 × 11.3 | 13.7 × 11.3 |  |
| Blade | 20.5 × 16.5 | game data | 20.5 × 16.5 | 21 × 21 | 24 × 20 | ⚠ |
| Buccaneer | 16.75 × 15.25 | game data | 16.75 × 15.25 | 15 × 16 | 15 × 16 |  |
| C8 Pisces | 16 × 12 | game data | 16 × 12 | 12 × 10 | 13 × 10 | ⚠ |
| C8R Pisces Rescue | 16 × 12 | game data | 16 × 12 | — | 13 × 10 |  |
| C8X Pisces Expedition | 16 × 12 | game data | 16 × 12 | 13 × 10 | 13 × 10 | ⚠ |
| CSV-SM | 8.75 × 6 | game data | 8.75 × 6 | 5.4 × 4.1 | 5.44 × 4.13 | ⚠ |
| Clipper | 26.5 × 16 | override | 26.5 × 21 | 26.5 × 18 | 26.5 × 50 | ⚠ |
| Command Module | 20 × 16 | game data | 20 × 16 | — | 20 × 16 |  |
| Cutlass Black | 37.5 × 26.5 | game data | 37.5 × 26.5 | 29 × 26.5 | 37.5 × 26.5 | ⚠ |
| Cutlass Blue | 37.5 × 26.5 | game data | 37.5 × 26.5 | 36 × 26 | 37.5 × 26.5 |  |
| Cutlass Red | 37.5 × 26.5 | game data | 37.5 × 26.5 | 36 × 26 | 37.5 × 26.5 |  |
| Cutlass Steel | 37.5 × 26.5 | game data | 37.5 × 26.5 | 36 × 26.5 | 37.5 × 26.5 |  |
| Cutter | 20 × 16 | game data | 20 × 16 | 20 × 13 | 20 × 13 | ⚠ |
| Cutter Rambler | 20 × 16 | game data | 20 × 16 | 20 × 13 | 20 × 13 | ⚠ |
| Cutter Scout | 20 × 16 | game data | 20 × 16 | 20 × 13 | 20 × 16 | ⚠ |
| Cyclone | 8.75 × 6 | game data | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone AA | 8.75 × 6 | game data | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone MT | 8.75 × 6 | game data | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone RC | 8.75 × 6 | game data | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone RN | 8.75 × 6 | game data | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Cyclone TR | 8.75 × 6 | game data | 8.75 × 6 | 6 × 4 | 6 × 4 | ⚠ |
| Defender | 24.5 × 24.5 | game data | 24.5 × 24.5 | 25.5 × 20 | 24.5 × 24.5 | ⚠ |
| Dragonfly | 7 × 2.5 | game data | 7 × 2.5 | — | 6 × 2.5 |  |
| Dragonfly Yellowjacket | 7 × 2.5 | game data | 7 × 2.5 | 8 × 3 | 7 × 2.5 |  |
| Eclipse | 24.5 × 24.5 | game data | 24.5 × 24.5 | 20.5 × 36.6 | 24.5 × 24.5 | ⚠ |
| F7A Hornet Mk I | 28.25 × 25.5 | game data | 28.25 × 25.5 | 22.5 × 21 | 22.5 × 22 | ⚠ |
| F7A Hornet Mk II | 22.5 × 22 | game data | 22.5 × 22 | 22.5 × 22 | 22.5 × 21.75 |  |
| F7C Hornet Mk I | 28.25 × 25.5 | game data | 28.25 × 25.5 | 22.5 × 21.5 | 22.5 × 21.5 | ⚠ |
| F7C Hornet Mk II | 22.5 × 22 | game data | 22.5 × 22 | 22.2 × 22 | 22.5 × 21 |  |
| F7C-M Super Hornet Mk II | 24 × 24 | game data | 24 × 24 | 24 × 19 | 24 × 24 | ⚠ |
| F7C-R Hornet Tracker Mk II | 22.5 × 22 | game data | 22.5 × 22 | 22.5 × 15 | 22.5 × 21 | ⚠ |
| F7C-S Hornet Ghost Mk II | 22.5 × 22 | game data | 22.5 × 22 | 22.5 × 15 | 22.5 × 15 | ⚠ |
| F8A Lightning | 26 × 25 | game data | 26 × 25 | — | 26 × 24 |  |
| F8C Lightning | 26 × 25 | game data | 26 × 25 | 25 × 24 | 26 × 25 |  |
| Fury | 7 × 5.4 | game data | 7 × 5.4 | 7 × 5.4 | 8 × 5.4 |  |
| Fury LX | 7 × 5.4 | game data | 7 × 5.4 | 7 × 5.4 | 7 × 5.4 |  |
| Fury MX | 7 × 5.4 | game data | 7 × 5.4 | 7 × 5.4 | 7 × 5.4 |  |
| Gladiator | 22.75 × 21 | game data | 22.75 × 21 | 22.3 × 22 | 22.5 × 22.5 |  |
| Gladius | 21 × 17.5 | game data | 21 × 17.5 | 20 × 17 | 20 × 17 |  |
| Gladius Pirate | 21 × 17.5 | game data | 21 × 17.5 | — | 21 × 17.5 |  |
| Gladius Valiant | 21 × 17.5 | game data | 21 × 17.5 | 20 × 16 | 21 × 17.5 |  |
| Glaive | 33 × 24 | game data | 33 × 24 | 31 × 20 | 27 × 20.1 | ⚠ |
| Golem | 15.5 × 7 | game data | 15.5 × 7 | 15.5 × 7 | 15.5 × 7 |  |
| Golem OX | 15.5 × 7 | game data | 15.5 × 7 | 15.5 × 10 | 15.5 × 7 | ⚠ |
| Guardian | 24.3 × 16.3 | game data | 24.3 × 16.3 | 25 × 16.5 | 25 × 16.5 |  |
| Guardian MX | 26 × 17 | game data | 26 × 17 | 25 × 20 | 25 × 16.5 | ⚠ |
| Guardian QI | 24.3 × 16.3 | game data | 24.3 × 16.3 | 25 × 16.5 | 25 × 16.5 |  |
| HM6 Ballista | 17 × 7 | game data | 17 × 7 | 17 × 7 | 17 × 7 |  |
| HM6 Centurion | 17 × 7 | game data | 17 × 7 | 17 × 7 | 17 × 7 |  |
| HM6 Spartan | 17 × 7 | game data | 17 × 7 | 17 × 7 | 17 × 7 |  |
| Hawk | 23 × 17 | game data | 23 × 17 | 17 × 22 | 17 × 22 |  |
| Herald | 24.75 × 12.5 | game data | 24.75 × 12.5 | 23.5 × 12.5 | 23.5 × 12.5 |  |
| HoverQuad | 5.15 × 1.45 | game data | 5.15 × 1.45 | 4.5 × 2.5 | 4.5 × 2.5 | ⚠ |
| Hurricane | 24 × 18.5 | game data | 24 × 18.5 | 22 × 14.5 | 22 × 18.2 | ⚠ |
| Hyun | 36.8 × 31.9 | game data | 36.8 × 31.9 | — | 36.8 × 31.9 |  |
| Intrepid | 23.07 × 20.18 | game data | 23.07 × 20.18 | 23.2 × 20.3 | 23.2 × 20.3 |  |
| Khartu-al | 32 × 13.5 | game data | 32 × 13.5 | 30.5 × 13 | 15 × 21.5 |  |
| L-21 Wolf | 21.5 × 10.5 | game data | 21.5 × 10.5 | 21.5 × 10.5 | 21.5 × 10.5 |  |
| L-22 Alpha Wolf | 21.5 × 10.5 | game data | 21.5 × 10.5 | 21.5 × 10.5 | 21.5 × 10.5 |  |
| Lynx | 7.75 × 5.7 | game data | 7.75 × 5.7 | 7.7 × 5.7 | 7.75 × 5.7 |  |
| M50 Interceptor | 11.5 × 11 | game data | 11.5 × 11 | — | 11.5 × 11 |  |
| M80 | 11.5 × 11 | game data | 11.5 × 11 | 32 × 17.3 | 32 × 17.3 | ⚠ |
| MDC | 8.75 × 6 | game data | 8.75 × 6 | 7 × 5.5 | 8.75 × 6 | ⚠ |
| MISC Fortune | 26.5 × 16.5 | game data | 26.5 × 16.5 | 26 × 16 | 26 × 16 |  |
| MISC Freelancer | 38 × 23.5 | game data | 38 × 23.5 | 38 × 23.5 | 38 × 23.5 |  |
| MISC Freelancer DUR | 38 × 23.5 | game data | 38 × 23.5 | 38 × 23.5 | 38 × 23.5 |  |
| MISC Freelancer MIS | 38 × 23.5 | game data | 38 × 23.5 | 38 × 23.5 | 38 × 23.5 |  |
| MISC Hull A | 30 × 12.5 | game data | 30 × 12.5 | 24 × 10 | 24 × 10 | ⚠ |
| MISC Hull B | 46 × 17 | override | 71 × 16.7 | 46 × 17 | 71 × 17 | ⚠ |
| MISC Prospector | 26.5 × 16.5 | game data | 26.5 × 16.5 | 24 × 15 | 26 × 16 |  |
| MISC Reliant Kore | 28.5 × 14.75 | game data | 28.5 × 14.75 | 14.5 × 28.5 | 14.5 × 10.8 |  |
| MISC Reliant Mako | 28.5 × 14.75 | game data | 28.5 × 14.75 | 14.5 × 28.5 | 28.5 × 14.75 |  |
| MISC Reliant Sen | 28.5 × 14.75 | game data | 28.5 × 14.75 | 14.5 × 28.5 | 28.5 × 14.75 |  |
| MISC Reliant Tana | 28.5 × 14.75 | game data | 28.5 × 14.75 | 14.5 × 28.5 | 28.5 × 14.75 |  |
| MISC Starlite | 32 × 19.9 | game data | 32 × 19.9 | 32 × 19 | 32 × 19.9 |  |
| MPUV Cargo | 10.5 × 9 | game data | 10.5 × 9 | 9 × 8.5 | 9.5 × 8.5 | ⚠ |
| MPUV Personnel | 10.5 × 9 | game data | 10.5 × 9 | 9 × 6.5 | 9.25 × 8.5 | ⚠ |
| MPUV Tractor | 10.5 × 9 | game data | 10.5 × 9 | 9 × 8.5 | 9 × 8.5 | ⚠ |
| MTC | 8.75 × 6 | game data | 8.75 × 6 | 7 × 5.5 | 8.75 × 6 | ⚠ |
| Mantis | 30 × 17 | game data | 30 × 17 | 30 × 17 | 30 × 17 |  |
| Marauder | 20 × 19 | game data | 20 × 19 | 20.5 × 18.5 | 20 × 19 |  |
| Meteor | 30 × 17 | game data | 30 × 17 | 30 × 17 | 30 × 17 |  |
| Mule | 8.75 × 6 | game data | 8.75 × 6 | 4.2 × 3 | 4.2 × 3 | ⚠ |
| Mustang Alpha | 21.5 × 18 | game data | 21.5 × 18 | 21.5 × 18 | 21.5 × 18 |  |
| Mustang Beta | 21.5 × 18 | game data | 21.5 × 18 | 21.5 × 18 | 21.5 × 18 |  |
| Mustang Delta | 21.5 × 18 | game data | 21.5 × 18 | 21.5 × 18 | 21.5 × 18 |  |
| Mustang Gamma | 21.5 × 18 | game data | 21.5 × 18 | 21.5 × 18 | 21.5 × 18 |  |
| Mustang Omega | 21.5 × 18 | game data | 21.5 × 18 | 17.5 × 15.5 | 21.5 × 18 | ⚠ |
| Nomad | 27 × 19 | game data | 27 × 19 | 26.5 × 18.3 | 27 × 19 |  |
| Nova | 20 × 12 | game data | 20 × 12 | 16 × 7 | 16 × 7 | ⚠ |
| Nox | 5.15 × 1.45 | game data | 5.15 × 1.45 | 5.5 × 1.5 | 5.15 × 1.5 |  |
| Nox Kue | 5.15 × 1.45 | game data | 5.15 × 1.45 | 5.5 × 1.5 | 5.5 × 1.5 |  |
| P-52 Merlin | 12 × 7.75 | game data | 12 × 7.75 | 12 × 7.7 | 12 × 7.7 |  |
| P-72 Archimedes | 12 × 7.75 | game data | 12 × 7.75 | 12 × 7.7 | 12 × 7.7 |  |
| PTV | 3.5 × 2.5 | game data | 3.5 × 2.5 | 3 × 2 | 3.5 × 2.5 |  |
| Pitbull | 6 × 6 | game data | 6 × 6 | 3.9 × 5.9 | 5.93 × 6.13 | ⚠ |
| Prowler | 34 × 32 | game data | 34 × 32 | 34 × 32 | 34 × 32 |  |
| Prowler Utility | 34 × 32 | game data | 34 × 32 | 34 × 32 | 34 × 32 |  |
| Pulse | 3.5 × 2.5 | game data | 3.5 × 2.5 | 3.1 × 0.9 | 3.15 × 0.9 | ⚠ |
| Pulse LX | 3.5 × 2.5 | game data | 3.5 × 2.5 | 3.1 × 0.9 | 3.5 × 2.5 | ⚠ |
| ROC | 6 × 3.9 | game data | 6 × 3.9 | 5.1 × 3.8 | 6 × 3.9 |  |
| ROC-DS | 6.6 × 5 | game data | 6.6 × 5 | 6.6 × 5 | 6.6 × 5 |  |
| Razor | 12.5 × 9 | game data | 12.5 × 9 | 11.5 × 8.2 | 11.5 × 8.2 |  |
| Razor EX | 12.5 × 9 | game data | 12.5 × 9 | 11.5 × 8.2 | 12.5 × 9 |  |
| Razor LX | 12.5 × 9 | game data | 12.5 × 9 | 11.5 × 8.2 | 12.5 × 9 |  |
| Redeemer | 51 × 25 | game data | 51 × 25 | 51 × 23.5 | 51 × 25 |  |
| S-65 Stingray | 20.447 × 15.1 | game data | 20.447 × 15.1 | 24.5 × 16.4 | 22.15 × 24.3 | ⚠ |
| SRV | 31.5 × 21.5 | game data | 31.5 × 21.5 | 28.5 × 19.5 | 28.5 × 19.5 |  |
| STV | 8.75 × 6 | game data | 8.75 × 6 | 4.2 × 2.8 | 4.2 × 2.8 | ⚠ |
| Sabre | 24.5 × 24.5 | game data | 24.5 × 24.5 | 26 × 24 | 24 × 26 |  |
| Sabre Comet | 24.5 × 24.5 | game data | 24.5 × 24.5 | 24 × 26 | 24.5 × 24.5 |  |
| Sabre Firebird | 24.5 × 24.5 | game data | 24.5 × 24.5 | 26 × 30 | 26 × 30 | ⚠ |
| Sabre Peregrine | 24.5 × 24.5 | game data | 24.5 × 24.5 | 26 × 24 | 26 × 24 |  |
| Sabre Raven | 24.5 × 24.5 | game data | 24.5 × 24.5 | 24 × 20.5 | 24.5 × 24.5 | ⚠ |
| Salvation | 14.5 × 8.5 | game data | 14.5 × 8.5 | 14.5 × 8.5 | 14.5 × 8.5 |  |
| San'tok.yāi | 24 × 23 | game data | 24 × 23 | 24 × 23 | 22 × 23 |  |
| Scorpius | 32 × 24 | game data | 32 × 24 | 24 × 32 | 24 × 32 |  |
| Scorpius Antares | 32 × 24 | game data | 32 × 24 | 24 × 32 | 32 × 24 |  |
| Shiv | 37.5 × 26.5 | game data | 37.5 × 26.5 | 36 × 28 | 37.5 × 26.5 |  |
| Skylark | 7 × 6.5 | game data | 7 × 6.5 | 6.5 × 4 | 7 × 6.5 | ⚠ |
| Storm | 10.25 × 7.65 | game data | 10.25 × 7.65 | 10.5 × 7.5 | 10.5 × 7.5 |  |
| Storm AA | 10.25 × 7.65 | game data | 10.25 × 7.65 | 10.5 × 7.5 | 10.5 × 7.5 |  |
| Talon | 24 × 15 | game data | 24 × 15 | 26 × 23.5 | 26 × 23.3 | ⚠ |
| Talon Shrike | 24 × 15 | game data | 24 × 15 | 26 × 23.5 | 24 × 15 | ⚠ |
| Terrapin | 20 × 16.5 | game data | 20 × 16.5 | 19.5 × 14.5 | 19.5 × 14.5 | ⚠ |
| Terrapin Medic | 20 × 16.5 | game data | 20 × 16.5 | 19.5 × 16.7 | 20 × 16.5 |  |
| UTV | 4 × 2.6 | game data | 4 × 2.6 | 4 × 2.6 | 4 × 2.6 |  |
| Ursa | 8.75 × 6 | game data | 8.75 × 6 | 7.6 × 5.5 | 7.75 × 5.7 | ⚠ |
| Ursa Fortuna | 8.75 × 6 | game data | 8.75 × 6 | 7.6 × 5.5 | 7.75 × 5.7 | ⚠ |
| Ursa Medivac | 8.75 × 6 | game data | 8.75 × 6 | 8 × 5.5 | 8 × 5.5 |  |
| Vanduul Scythe | 33 × 24 | game data | 33 × 24 | 31 × 23 | 39 × 26.46 |  |
| Vanguard Harbinger | 48 × 40 | game data | 48 × 40 | 38.5 × 40 | 38.5 × 40 | ⚠ |
| Vanguard Hoplite | 48 × 40 | game data | 48 × 40 | 38.5 × 40 | 38.5 × 40 | ⚠ |
| Vanguard Sentinel | 48 × 40 | game data | 48 × 40 | 38.5 × 40 | 38.5 × 40 | ⚠ |
| Vanguard Warden | 48 × 40 | game data | 48 × 40 | 38.5 × 40 | 38.5 × 40 | ⚠ |
| Vulture | 34 × 16 | game data | 34 × 16 | 33 × 16 | 34 × 16 |  |
| X1 | 5.19 × 1.87 | game data | 5.19 × 1.87 | 5.5 × 1.3 | 5.5 × 1.3 |  |
| X1 Force | 5.19 × 1.87 | game data | 5.19 × 1.87 | 5.5 × 1.3 | 5.5 × 1.3 |  |
| X1 Velocity | 5.19 × 1.87 | game data | 5.19 × 1.87 | 5.5 × 1.3 | 5.5 × 1.3 |  |
| Zeus Mk II CL | 46 × 35 | game data | 46 × 35 | 45.7 × 34.3 | 45.69 × 34.3 |  |
| Zeus Mk II ES | 46 × 35 | game data | 46 × 35 | 45.7 × 34.3 | 45.7 × 34.3 |  |
