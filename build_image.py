"""Build entry.png for make.fun news-image-20261119.

The base illustration (assets/) was generated in-session as an editorial
collage of Thursday 19 November 2026's top stories, drawn as large,
instantly readable symbols:
  - Grand Theft Auto VI begins its global rollout: a neon Vice City
    skyline, palm trees, a pink-and-teal sports car and a giant game
    controller over the city
  - The planned Xi-Trump-Putin trilateral at APEC in Shenzhen: three
    leaders at one summit table under the US, Chinese and Russian flags
  - The Crimean Bridge hit for the third time this week: a long sea
    bridge with a fireball at mid-span, traffic closed while damage
    is assessed
  - Nvidia's record $115.8B quarter and $130B guide, yet the shares
    fell ~3% as the board refused to reinstate Jensen Huang and hawkish
    Fed minutes lifted the dollar: a giant AI chip over a plunging
    red stock chart
  - Anthropic's $81.3B raise, the biggest IPO of all time: a stock
    exchange bell with coins rocketing upward
  - NASA's Voyager 1 reaching one light-day from Earth, 50 years
    after launch: a deep-space probe beaming its signal home
  - The Optimizely supply-chain attack: malicious code served to 178
    organisations (Zoom, CNN, BBC, HSBC, Ledger among them) swapping
    crypto wallet addresses and skimming cards - a hooded hacker, a
    web of screens and a broken padlock
  - Crypto in extreme fear: Bitcoin near $62.6K, below its 200-week
    average, ETF outflows running - a cracked gold coin sinking in
    heavy seas under a falling red arrow
This script frames the collage as a magazine cover in the style of
The Economist's "The World Ahead": a small red masthead box and a
large date title above the full-bleed art, at most 1024x1024, 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "media-generation-media-generation-world-19nov-e-0-eac811b7-4d0c-46d4-9dcd-475224d14192.png")
OUT = os.path.join(HERE, "entry.png")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
NAVY = (9, 24, 43)
GOLD = (242, 193, 78)
WHITE = (245, 247, 250)

W, H = 1024, 1024
TOP_H, BOT_H = 190, 0


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def centered(draw, y, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text(((W - (box[2] - box[0])) // 2, y), text, font=fnt, fill=fill)


def main():
    art = Image.open(SRC).convert("RGB")
    art = art.resize((W, H - TOP_H - BOT_H), Image.LANCZOS)
    page = Image.new("RGB", (W, H), (247, 244, 235))
    page.paste(art, (0, TOP_H))
    draw = ImageDraw.Draw(page)

    draw.rectangle([312, 14, 712, 58], fill=(227, 18, 11))
    centered(draw, 22, "THE WORLD TODAY", font("DejaVuSans-Bold.ttf", 30), WHITE)
    centered(draw, 72, "19 NOVEMBER 2026", font("DejaVuSans-Bold.ttf", 84), (17, 17, 17))
    centered(draw, 164, "THURSDAY · THE DAY IN ONE IMAGE", font("DejaVuSans-Bold.ttf", 20), (90, 90, 90))

    headlines = [
        ((242, 193, 78), "GTA VI LAUNCHES WORLDWIDE: GAMERS ENTER VICE CITY"),
        ((231, 76, 60), "CRIMEAN BRIDGE HIT FOR THE THIRD TIME THIS WEEK"),
        ((230, 126, 34), "XI, TRUMP & PUTIN: TRILATERAL PLANNED AT APEC SHENZHEN"),
        ((93, 173, 226), "NVIDIA BEATS, STOCK FALLS · HAWKISH FED LIFTS DOLLAR"),
        ((46, 204, 113), "CYBER: OPTIMIZELY ATTACK TOUCHES 178 ORGANISATIONS"),
        ((175, 122, 197), "CRYPTO: BITCOIN NEAR $62.6K · FEAR & GREED AT 10"),
    ]
    fnt = font("DejaVuSans-Bold.ttf", 24)
    y = H - BOT_H + 10
    for color, text in headlines:
        draw.rectangle([28, y + 4, 44, y + 20], fill=color)
        draw.text((58, y), text, font=fnt, fill=WHITE)
        y += 34

    page.save(OUT, optimize=True)
    if os.path.getsize(OUT) > 1024 * 1024:
        page.quantize(colors=256, method=Image.MEDIANCUT).save(OUT, optimize=True)
    print("entry.png:", page.size, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
