# Create labels on Brother PT-2730 on Big Sur

Brother dropped support of older printers on Big Sur; this program lets you create and print labels on the PT-2730 anyway.

This program is set up for my environment and will probably need changes for yours - in particular, the print queue name (printed to `stdout`) 
may be different.

Requires __fclist-cffi__ and __PIL__ (or __pillow__).

````
usage: labels.py [-h] [--height HEIGHT] [--font FONT] [--size SIZE]
                 [--variation VARIATION [VARIATION ...]]
                 [text [text ...]]

Utility for printing on PT-2730

positional arguments:
  text

optional arguments:
  -h, --help            show this help message and exit
  --height HEIGHT       height in pixels of loaded tape
  --font FONT           name of truetype font
  --size SIZE
  --variation VARIATION [VARIATION ...]
````

Fontnames and variations are parsed by __fcmatch__ from the __fclist-cffi__ package.

The program creates `out.png`, which is the file to be sent to `lpr` to make the label;
the program writes the necessary command to `stdout` and you can pipe it into `sh` if you wish.

