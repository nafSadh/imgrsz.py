imgrsz.py
=========
IMaGe ReSiZe script in Python

Usage
-----
Usage: imgrsz.py [OPTIONS]...

Resize input image into output image to a given target size
    target width and/or height or scaling factor

Description of arguments:
  Input/Output
  -i, --input      input image filename
                   * mandatory argument
  -o, --output     output filename
                   ! either -r or this is mandatory
  -r, --replace    replace input file with resized image
                   ! required only when replacing
  Sizing
  -w, --width      target width of resized image
  -h, --height     target height of resized image
  -s, --scale      scaling factor of resized image
                   `if you provide either of w,h this program will compute
                    other keeping the aspect ratio
                   `if you provide a scaling factor, the new image will keep
                    original aspect ratio
                   `if both w and h supplied, s will be ignored
  Other
  -q, --quiet      quiet mode
  -v, --verbose    verbose
