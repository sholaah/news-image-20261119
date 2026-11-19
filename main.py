"""news-image-20261119 entry: writes the day's front-page image.

The repository holds entry.png, a 1024x1024 front page summing up the
world news of Thursday 19 November 2026: the GTA VI global launch, the
planned Xi-Trump-Putin trilateral, the third Crimean Bridge strike of
the week, Nvidia's record earnings and the hawkish Fed, Anthropic's
record IPO, Voyager 1 at one light-day, the Optimizely supply-chain
attack on 178 organisations, and Bitcoin's extreme-fear slide.

This program copies entry.png to the output location the harness asks
for (/output/entry.png, or $MAKEFUN_OUTPUT_DIR/entry.png outside the
grader). No network, no clock, no randomness: every run writes the
same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    written = os.path.getsize(target)
    assert written == os.path.getsize(SOURCE), "copied image differs in size"
    print(f"wrote {target} ({written} bytes)")


if __name__ == "__main__":
    main()
