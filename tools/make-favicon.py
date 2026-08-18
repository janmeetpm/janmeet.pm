#!/usr/bin/env python3
"""Rebuilds favicon.ico — the block cursor from the masthead, on the dark
surface, inside a hairline window edge. Run from the repo root:

    python3 tools/make-favicon.py

Not part of the build; favicon.ico is committed. Every rectangle is drawn on
integer pixel boundaries with no antialiasing, because the design bans
soft edges and because a 16px tab icon with a blurred edge reads as dirt.
Colours are the site's --bg / --line / --amber, dark theme: a favicon has no
media query, and the dark mark works on both browser chromes.
"""
import io

from PIL import Image, ImageDraw

BG, LINE, AMBER = (17, 16, 16), (46, 42, 39), (240, 169, 59)
SIZES = [16, 32, 48, 64, 128, 256]

def icon(s):
    im = Image.new('RGB', (s, s), BG)
    d = ImageDraw.Draw(im)
    edge = max(1, s // 32)
    d.rectangle([0, 0, s - 1, s - 1], outline=LINE, width=edge)
    # the caret: same proportions as .cursor in index.html (width .5em, height 1em)
    w = max(3, round(s * 0.28))
    h = max(6, round(s * 0.50))
    x = (s - w) // 2
    y = (s - h) // 2
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=AMBER)
    return im

# The ICO container is assembled by hand. Pillow's ICO writer takes one image
# and *resamples* it down to the other sizes, which reintroduces the soft edges
# this mark exists without; drawing each size separately and packing them keeps
# every entry pixel-exact. Entries are PNG-in-ICO, which every current browser
# reads.
import struct

pngs = []
for s in SIZES:
    buf = io.BytesIO()
    icon(s).save(buf, format='PNG', optimize=True)
    pngs.append(buf.getvalue())

out = io.BytesIO()
out.write(struct.pack('<HHH', 0, 1, len(SIZES)))          # reserved, type=icon, count
offset = 6 + 16 * len(SIZES)
for s, data in zip(SIZES, pngs):
    dim = 0 if s >= 256 else s                            # 0 means 256 in the spec
    out.write(struct.pack('<BBBBHHII', dim, dim, 0, 0, 1, 32, len(data), offset))
    offset += len(data)
for data in pngs:
    out.write(data)

with open('favicon.ico', 'wb') as f:
    f.write(out.getvalue())
print('favicon.ico written, sizes', SIZES, '-', len(out.getvalue()), 'bytes')
