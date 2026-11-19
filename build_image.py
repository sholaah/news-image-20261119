"""Compose the 19 November 2026 cover for the make.fun daily news-image bounty.

Design: a full-bleed Economist-style collage (generated artwork, kept in
assets/) fills the square canvas under a cream masthead band that carries a
red nameplate, the date as a huge black title, and a one-line gray tagline.

The eight stories the artwork has to carry, all from 19 November 2026:
  * GTA VI begins its global rollout; players finally enter Vice City
  * Xi, Trump and Putin plan a trilateral meeting at APEC Shenzhen
  * The Crimean Bridge is struck for the third time this week
  * Nvidia beats on earnings ($115.8B revenue) yet the stock falls
  * Anthropic's $81.3B raise, reported as the biggest IPO of all time
  * Voyager 1 reaches one light-day from Earth
  * Optimizely supply-chain attack hits 178 organisations
  * Bitcoin in extreme fear near $62.6K, below its 200-week average

Deterministic: the same artwork in, the same entry.png out, byte for byte.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SOURCE_ART = ROOT / "assets" / (
    "media-generation-media-generation-world-19nov-e-0-"
    "eac811b7-4d0c-46d4-9dcd-475224d14192.png"
)
TARGET = ROOT / "entry.png"

CANVAS = 1024          # the bounty caps the image at 1024x1024
BAND = 190             # masthead band height; the artwork starts below it
PAPER = (247, 244, 235)
NAMEPLATE_RED = (227, 18, 11)
INK = (17, 17, 17)
MUTE = (110, 110, 110)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
SERIF_BOLD = str(FONT_DIR / "DejaVuSerif-Bold.ttf")
SANS = str(FONT_DIR / "DejaVuSans.ttf")
SANS_BOLD = str(FONT_DIR / "DejaVuSans-Bold.ttf")


def load_font(path, size):
    return ImageFont.truetype(path, size)


def fit_font(path, text, start_size, max_width, draw):
    """Largest size at or below start_size whose text fits max_width."""
    size = start_size
    while size > 10:
        font = load_font(path, size)
        box = draw.textbbox((0, 0), text, font=font)
        if box[2] - box[0] <= max_width:
            return font
        size -= 2
    return load_font(path, size)


def centered(draw, cx, y, text, font, fill):
    """Draw text horizontally centered on cx; return its bottom edge."""
    box = draw.textbbox((0, 0), text, font=font)
    w = box[2] - box[0]
    draw.text((cx - w / 2 - box[0], y), text, font=font, fill=fill)
    return y + (box[3] - box[1])


def artwork_panel():
    """The generated collage, downscaled to fill everything below the band."""
    art = Image.open(SOURCE_ART).convert("RGB")
    return art.resize((CANVAS, CANVAS - BAND), Image.LANCZOS)


def paint_masthead(page):
    draw = ImageDraw.Draw(page)
    half = CANVAS // 2

    # Red nameplate with the paper's name in white serif caps.
    plate_font = load_font(SERIF_BOLD, 30)
    label = "THE WORLD TODAY"
    box = draw.textbbox((0, 0), label, font=plate_font)
    tw, th = box[2] - box[0], box[3] - box[1]
    pad_x, pad_y = 26, 9
    x0, y0 = half - tw / 2 - pad_x, 14
    x1, y1 = half + tw / 2 + pad_x, y0 + th + 2 * pad_y
    draw.rectangle([x0, y0, x1, y1], fill=NAMEPLATE_RED)
    draw.text((half - tw / 2 - box[0], y0 + pad_y - box[1]),
              label, font=plate_font, fill=(255, 255, 255))

    # The date, set huge; then the tagline under it in quiet gray.
    # Fit the date to the band width so the title never touches the edges.
    date_font = fit_font(SERIF_BOLD, "19 NOVEMBER 2026", 84, CANVAS - 32, draw)
    bottom = centered(draw, half, 64, "19 NOVEMBER 2026", date_font, INK)
    tag_font = load_font(SANS, 20)
    centered(draw, half, bottom + 14,
             "THURSDAY · THE DAY IN ONE IMAGE", tag_font, MUTE)


def build_cover():
    page = Image.new("RGB", (CANVAS, CANVAS), PAPER)
    page.paste(artwork_panel(), (0, BAND))
    paint_masthead(page)
    # Adaptive palette keeps the flat illustration crisp and the file
    # comfortably under the bounty's 1 MiB cap.
    page = page.quantize(colors=256, method=Image.MEDIANCUT)
    page.save(TARGET, format="PNG", optimize=True)
    return TARGET


if __name__ == "__main__":
    out = build_cover()
    print(f"wrote {out} ({out.stat().st_size} bytes)")
