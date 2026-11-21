#!/usr/bin/env python3
"""Entry for make.fun news-image-20261121.

Draws the front page for Saturday 21 November 2026 (see build_image.py)
and writes it to the output directory. Standard library only, plus
Pillow for drawing: no network, no randomness, no clock, so two runs
write identical bytes.
"""

import os
import sys

import build_image


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    img = build_image.render()
    img.save(target, format="PNG", optimize=True)
    size = os.path.getsize(target)
    print("wrote %s (%dx%d, %d bytes)" % (target, build_image.PAGE_W,
                                          build_image.PAGE_H, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
