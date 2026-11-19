"""Entry program for make.fun news-image-20261119 (19 November 2026).

The bounty asks for one program that writes exactly one image to
/output/entry.png. The finished cover already sits next to this file as
entry.png (build_image.py composes it from the generated artwork), so the
whole job here is a faithful copy plus a self-check: the bytes delivered
must be the bytes that were committed, and the picture must be a readable
PNG or JPEG within the size the bounty allows.

Standard library only; no network; safe to run any number of times.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COVER = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("ENTRY_OUT_DIR", "/output"))
OUT_FILE = OUT_DIR / "entry.png"

BYTE_LIMIT = 1024 * 1024          # bounty cap: 1 MiB
SIDE_LIMIT = 1024                 # bounty cap: 1024 x 1024


def png_dimensions(blob):
    """(width, height) from a PNG header, or None when it is not a PNG."""
    if not blob.startswith(b"\x89PNG\r\n\x1a\n"):
        return None
    return struct.unpack(">II", blob[16:24])


def jpeg_dimensions(blob):
    """(width, height) from the first JPEG SOF marker, else None."""
    if not blob.startswith(b"\xff\xd8"):
        return None
    pos = 2
    while pos + 4 <= len(blob):
        if blob[pos] != 0xFF:
            return None
        marker = blob[pos + 1]
        length = struct.unpack(">H", blob[pos + 2:pos + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", blob[pos + 5:pos + 9])
            return w, h
        pos += 2 + length
    return None


def image_dimensions(blob):
    return png_dimensions(blob) or jpeg_dimensions(blob)


def validate(blob):
    """Refuse anything the bounty would reject; return (w, h) when sound."""
    if len(blob) > BYTE_LIMIT:
        sys.exit(f"cover is {len(blob)} bytes, over the {BYTE_LIMIT} cap")
    dims = image_dimensions(blob)
    if dims is None:
        sys.exit("cover is neither PNG nor JPEG")
    if dims[0] > SIDE_LIMIT or dims[1] > SIDE_LIMIT:
        sys.exit(f"cover is {dims[0]}x{dims[1]}, over the {SIDE_LIMIT} cap")
    return dims


def deliver():
    blob = COVER.read_bytes()
    dims = validate(blob)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(COVER, OUT_FILE)

    placed = OUT_FILE.read_bytes()
    if hashlib.sha256(placed).digest() != hashlib.sha256(blob).digest():
        sys.exit("delivered file differs from the committed cover")
    print(f"delivered {OUT_FILE} ({len(placed)} bytes, {dims[0]}x{dims[1]})")


if __name__ == "__main__":
    deliver()
