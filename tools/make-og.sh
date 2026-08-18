#!/bin/sh
# Rebuilds og.png (1200x630) from tools/og-template.html using headless Chrome,
# so the card renders in the site's actual webfonts. Run from the repo root:
#
#     sh tools/make-og.sh
#
# Not part of the build: og.png is committed. Chrome needs a moment to fetch the
# fonts from the same Google Fonts CDN the site uses, hence virtual-time-budget.
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=1 --window-size=1200,630 \
  --virtual-time-budget=6000 \
  --screenshot="$PWD/og.png" \
  "file://$PWD/tools/og-template.html" 2>/dev/null
# Chrome writes a 24-bit PNG; the card is near-monochrome plus one accent, so a
# 128-colour palette is visually identical (mean error 0.3/255) and drops it from
# ~490KB to ~280KB. Worth it: this file is fetched by every unfurl.
python3 - <<'PY'
from PIL import Image
im = Image.open('og.png').convert('RGB')
im.convert('P', palette=Image.ADAPTIVE, colors=128).save('og.png', optimize=True)
out = Image.open('og.png')
print('og.png rebuilt:', out.size, out.mode)
PY
