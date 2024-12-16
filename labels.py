#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import sys
import argparse
from fclist import fcmatch

# Updated for Pillow 10; tries to antialias

parser = argparse.ArgumentParser(description="Utility for printing on PT-2730")
parser.add_argument('text', type=str, nargs='*')
parser.add_argument('--height', type=int, help="height in pixels of loaded tape", default=84)
parser.add_argument('--font', type=str, help="name of truetype font", default="Avenir Next Condensed")
parser.add_argument('--size', type=int, default=30)
parser.add_argument('--variation', action='append')
parser.add_argument('--printer', type=str, default='Brother_PT_2730')
args = parser.parse_args()

if len(args.text) == 0:
    text = 'H,?!q'
else:
    text = ' '.join(args.text)

# Get the font
fontsize = args.size if args.size else args.height
resize = 4
wanted = args.font
if args.variation:
    wanted += ':' + ':'.join(args.variation)
fontinfo = fcmatch(wanted)
print(fontinfo.file, fontinfo.index, file=sys.stderr)
font = ImageFont.truetype(fontinfo.file, index=fontinfo.index, size=fontsize * resize)
print(font, file=sys.stderr)

left, top, right, bottom = font.getbbox(text)
bigsize = (right - left, bottom)
size = (int(bigsize[0] / resize), int(bigsize[1] / resize))
print(f'size = {size}', file=sys.stderr)
bigimage = Image.new('RGB', bigsize, color=(255, 255, 255))
draw = ImageDraw.Draw(bigimage)
draw.text((0, 0), text, font=font, fill=(0, 0, 0))
image = bigimage.resize(size, Image.Resampling.LANCZOS)
image.save('out.png')
width = size[0]
print(size, file=sys.stderr)
print(f'lpr -P "{args.printer}" -o media=12mm -o PageSize=Custom.28x{width} out.png')
