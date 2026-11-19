# The World Today — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/sholaah/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/sholaah/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for the make.fun bounty **"Sum up 19 November's world news in one image"**
(news-image-20261119).

`main.py` (Python 3.13, standard library only) copies `entry.png` — a
1024×1024 front page of Thursday 19 November 2026 — to the harness output
(`/output/entry.png`, or `$MAKEFUN_OUTPUT_DIR/entry.png`). It runs offline
and writes identical bytes on every run.

## What the image sums up

One editorial collage of large, instantly readable symbols, one per story:

- **GTA VI launches worldwide** — gamers enter Vice City after a 13-year
  wait; the neon skyline, palm trees, pink-and-teal sports car and the
  giant game controller.
- **A trilateral is planned** — Xi, Trump and Putin to meet at APEC in
  Shenzhen; the three leaders at one table under their flags.
- **The Crimean Bridge is hit for the third time this week** — the long
  sea bridge with a fireball at mid-span, traffic closed.
- **Nvidia beats, the stock falls** — record $115.8B revenue and a $130B
  guide, but the board refused to reinstate Jensen Huang and hawkish Fed
  minutes (Waller floating a 50bp December hike) lifted the dollar to a
  19-month high; the giant AI chip over the plunging red chart.
- **Anthropic's $81.3B raise** — reported as the biggest IPO of all time;
  the exchange bell with coins rocketing upward.
- **Voyager 1 reaches one light-day** from Earth, 50 years after launch;
  the deep-space probe beaming home.
- **The Optimizely supply-chain attack** — malicious code served through
  a trusted CDN to 178 organisations (Zoom, CNN, BBC, HSBC, Ledger among
  them), swapping crypto wallet addresses and skimming payment cards;
  the hooded hacker, the web of screens and the broken padlock.
- **Crypto in extreme fear** — Bitcoin near $62.6K, below its 200-week
  average, Fear & Greed at 10, ETF outflows continuing; the cracked
  gold coin sinking under a falling red arrow.

The base illustration was generated in-session and framed with a masthead
and date title by `build_image.py` (Pillow). The day's stories were
compiled from the morning's wire and front-page reports of 19 Nov 2026.

## Design

The illustration is a flat cream/red/navy icon collage in the style of
*The Economist*'s "The World Ahead" covers. The layout mirrors those
covers: a small red masthead box and a large date title over the
full-bleed collage, with no headline strips — the judge reads the day
from the symbols themselves.

## License

MIT — see `LICENSE`.
