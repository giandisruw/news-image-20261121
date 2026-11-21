# THE WORLD — Saturday 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/giandisruw/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/giandisruw/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Built for the [make.fun](https://make.fun/bounty/news-image-20261121) news-image-20261121 bounty.

A one-page newspaper front page that sums up the world's news of
Saturday 21 November 2026, drawn by a Python program. Built for the
make.fun bounty `news-image-20261121` ("Sum up 21 November's world news
in one image").

## The image

The front page leads with Russian missiles landing in Poland — two
missiles and a suspected drone came down in south-east Poland during a
huge overnight attack on Ukraine, which Warsaw called an intentional
provocation and NATO called a grave violation of Polish airspace.

The rest of the page covers the day's other big stories: Wall Street
slumping into correction as the AI sell-off deepens, Cyclone Akvan
coming ashore in Odisha, Denmark foiling an alleged Russian plot to kill
the rapper Kyivstoner, a tanker struck and set on fire in the Strait of
Hormuz, the UK and EU sealing their post-Brexit reset, a pancreatic
cancer pill shrinking tumours in an early trial, and the guilty verdict
in the Palisades Fire arson retrial. A dark ticker at the foot carries
Virginia's first measles death of 2026, the Saudi coalition's response
in Riyadh, and Trump's call with European allies.

Every fact on the page was checked against several independent sources
on the morning of 21 November 2026; see `NOTES.md` for the story-by-story
sources. Nothing in the image is dated before 20 November 2026.

## Stories at a glance

| Story | What happened |
|---|---|
| Russian missiles in Poland | Two missiles and a drone came down in south-east Poland; Tusk calls it an intentional provocation |
| Wall Street correction | S&P 500 −3.7%, Dow −1.9%, Nasdaq −5.3%; both S&P and Dow now 10%+ off their peaks |
| Cyclone Akvan | Landfall near Gopalpur, Odisha; ~370,000 evacuated; no major damage reported |
| Denmark foils plot | Alleged Russian plan to kill rapper Kyivstoner stopped; two Danes charged |
| Hormuz tanker | Tanker struck by an unknown projectile off Oman and caught fire; no casualties |
| UK–EU reset | Deals on food trade, carbon markets and youth mobility (100,000 a year) |
| Cancer pill | Erasca's ERAS-0015 shrank tumours in 44% of 25 pancreatic cancer patients in an early trial |
| Palisades verdict | Jonathan Rinderknecht found guilty of starting the fire that killed 12 people |

## How to run it

Requires Python 3.13 and Pillow, with the Liberation fonts installed
(the environment the bounty grader provides).

```sh
python3 main.py
```

That writes the front page to `/output/entry.png` (or to the directory
in `MAKEFUN_OUTPUT_DIR`). The image is a 1024×1024 PNG, well under the
1 MiB limit. The program uses no network, no clock and no randomness:
running it twice writes byte-identical output.

To render the image into this directory instead, run:

```sh
python3 build_image.py
```

## Files

- `main.py` — the entrypoint: draws the page and writes `/output/entry.png`
- `build_image.py` — the drawing code and all story text
- `entry.png` — the rendered front page
- `NOTES.md` — research notes: every story with its sources
- `README.md` — this file
- `LICENSE` — MIT licence
