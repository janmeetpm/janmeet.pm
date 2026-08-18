#!/usr/bin/env python3
"""Prepares a photograph for use as the site backdrop (bg-grey.jpg).

NOT part of the build. The site has no build step; this is a manual tool you
run once when changing the backdrop, and it writes bg-grey.jpg into the
current directory. Run it from the repo root:

    python3 tools/prepare-backdrop.py ~/Downloads/beach.jpg --aspect 1.5 --anchor 0.62

The shipped image was made with exactly that command. See DESIGN.md ->
Backdrop before replacing it: the grey band below is load-bearing for text
contrast, not a stylistic choice.

Writes bg-grey.jpg. Does four things, all of which the rest of index.html
depends on:

  1. greyscale — the whole design has one accent colour; a colour cast in
     the backdrop would be a second one;
  2. flattens the tonal range into LO..HI, the same band the generated
     image occupies, so the translucent pane composites predictably. A
     photo straight off the camera has real blacks and real whites; drop
     either behind the reading pane and text contrast goes with it;
  3. resizes to WIDTH and strips metadata (a phone photo is 3-6MB and
     carries GPS — neither belongs in a page background);
  4. optionally crops to a landscape aspect around a chosen line, because
     the layer is `background-size:cover` — hand it a portrait frame and
     every landscape viewport center-crops it for you, usually through
     the worst part. --anchor 0.62 means "the crop is centred 62% of the
     way down the original", so you choose what survives;
  5. reports the extrema so you can re-check contrast if you widen LO..HI.

Composition note: the layer is `background-size:cover`, centred, and
`position:fixed`, so the photo is cropped to the viewport's aspect ratio
and never scrolls. A subject near an edge will be cut on some screens;
subjects in the middle sit behind the text column, where the pane is most
opaque. Empty, high-key frames survive this treatment best — which is why
the generated stand-in is mostly sky.
"""
import sys, os
from PIL import Image, ImageOps

WIDTH = 1800
LO, HI = 62, 206      # the band index.html's pane ramp is tuned against

args = sys.argv[1:]
if not args:
    sys.exit('usage: python3 tools/prepare-backdrop.py <photo> [--aspect W/H] [--anchor 0..1]')
src = os.path.expanduser(args[0])
aspect = anchor = None
for i, a in enumerate(args):
    if a == '--aspect': aspect = eval(args[i + 1])       # accepts 1.5 or 3/2
    if a == '--anchor': anchor = float(args[i + 1])

im = Image.open(src)
im = ImageOps.exif_transpose(im)          # honour rotation, then drop the EXIF
im = im.convert('L')

if aspect:
    # crop to the requested aspect, as tall as the frame allows, centred on
    # anchor (default: the middle) and clamped inside the original
    target_h = min(im.height, round(im.width / aspect))
    target_w = min(im.width, round(target_h * aspect))
    centre = (anchor if anchor is not None else 0.5) * im.height
    top = round(min(max(centre - target_h / 2, 0), im.height - target_h))
    left = (im.width - target_w) // 2
    im = im.crop((left, top, left + target_w, top + target_h))
    print('cropped to %dx%d from y=%d' % (target_w, target_h, top))

if im.width > WIDTH:
    im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)

im = ImageOps.autocontrast(im, cutoff=(0.5, 0.5))   # normalise, ignoring outliers
im = im.point(lambda v: LO + v * (HI - LO) // 255)  # then park it in the band

clean = Image.new('L', im.size)
clean.putdata(list(im.getdata()))         # new image => no metadata carried over
clean.save('bg-grey.jpg', quality=72, optimize=True, progressive=True)

kb = os.path.getsize('bg-grey.jpg') / 1024
print('bg-grey.jpg  %dx%d  %.0fKB  range %s' % (*clean.size, kb, clean.getextrema()))
print('band target was %d..%d — if JPEG pushed it wider, re-check contrast.' % (LO, HI))
