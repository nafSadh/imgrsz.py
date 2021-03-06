# imgrsz.py -- IMaGe ReSiZe script in Python                                   #
#                                                                              #
# Free software by nafSadh-khan (http://nafSadh.com)                           #
#                                                                              #
# This is free and unencumbered software released into the public domain.      #
#                                                                              #
# Anyone is free to copy, modify, publish, use, compile, sell, or distribute   #
# this software, either in source code form or as a compiled binary, for any   #
# purpose, commercial or non-commercial, and by any means.                     #
#                                                                              #
# In jurisdictions that recognize copyright laws, the author or authors of this#
# software dedicate any and all copyright interest in the software to the      #
# public domain.  We make this dedication for the benefit of the public at     #
# large and to the detriment of our heirs and successors.  We intend this      #
# dedication to be an overt act of relinquishment in perpetuity of all present #
# and future rights to this software under copyright law.                      #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTBILITY,      #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT, IN NO EVENT SHALL THE  #
# AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN  #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION #
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.              #
#                                                                              #
# For more information, please refer to <http://unlicense.org/>                #
#                                                                              #
# ! README:                                                                    #
# ! this script requires the new Python Image Library (Pillow)                 #
# ! you can pip install Pillow using following command                         #
# !> pip install Pillow                                                        #
#                                                                              #

def image_resize(input, output, width, height, scale):
  import PIL
  from PIL import Image
  img = Image.open(input)
  w,h = img.size
  if scale < 0.0:
    if width>0: scale = float(width)/w
    if height>0: scale = float(height)/h
  if width<0: width = int(w*scale)
  if height<0: height = int(h*scale)
  img = img.resize((width, height), PIL.Image.ANTIALIAS)
  img.save(output)
  return (width, height, w, h)


def printEntireFile(filename):
  with open(filename, "rU") as file:
    print file.read()
  #for line in lines[1:]:
  #  print line


def usage():
  printEntireFile("USAGE")


def main():
  import getopt, sys
  try:
    options, args = getopt.getopt(sys.argv[1:], 'i:o:h:w:s:r?qdv', ['help', 'input=', 'output=', 'height=', 'width=', 'scale=', 'replace', 'quiet', 'verbose'])
  except getopt.GetoptError as err:
    # print help information and exit:
    print(err) # will print something like 'option -a not recognized'
    usage()
    sys.exit(2)
  if len(options) < 1: usage(); sys.exit()

  # defaults
  input, output = '',''
  width, height = -1,-1
  scale = -1.0
  replace = False
  quiet = False
  dir = False
  verbose = False

  # read args
  for opt, arg in options:
    if opt in ('-i', '--input'):
      input = arg
    elif opt in ('-o', '--output'):
      output = arg
    elif opt in ('-w', '--width'):
      width = int(arg)
    elif opt in ('-h', '--height'):
      height = int(arg)
    elif opt in ('-s', '--scale'):
      scale = float(arg)
    elif opt in ('-r', '--replace'):
      replace = True
    elif opt in ('-?', '--help'):
      usage()
      sys.exit()
    elif opt in ('-q', '--quiet'):
      quiet = True
    elif opt in ('-d', '--dir'):
      dir = True
    elif opt in ('-v', '--verbose'):
      verbose = True
    else:
      assert False, 'unhandled option'

  if verbose:
      print 'input:\t', input
      print 'output:\t', output
      print 'width:\t', width
      print 'height:\t', height
      print 'scale:\t', scale
      print 'replace:', replace
      print 'quiet:\t', quiet

  if input == '':
    if not quiet: print '[!] pass an input image file to resize [-i, --input]'
    sys.exit()
  if replace:
    output = input
    if not quiet: print 'replacing input image with output file'
  if output == '':
    if not quiet:
      print '[!] pass an output file-name to write the resized image to [-o, --output]'
      print '    to replace original file with resized image, use [-r, --replace]'
    sys.exit()
  if width <0 and height<0 and scale<0.0:
    if not quiet:
      print '[!] pass atleast one of height, width or scale values:'
      print '    -w, --width: width of resized image'
      print '    -h, --height: height of resized image'
      print '    -s, --scale: scale ratio for resized image'
      print '    if one passed, others are duly calculated'
    sys.exit()
  # ...
  if dir:
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(input) if isfile(join(input, f))]
    if output==input:
      output = join(output+"out/")
    for file in onlyfiles:
      r_width, r_height, r_w, r_h = image_resize(join(input, file), join(output, file), width, height, scale)
      if not quiet: print 'resized', input,'(',r_w,'X',r_h,')', 'to', output, '(',r_width,'X',r_height,')'

  else :
    width, height, w, h = image_resize(input, output, width, height, scale)
    if not quiet: print 'resized', input,'(',w,'X',h,')', 'to', output, '(',width,'X',height,')'
  return

if __name__ == '__main__':
  main()
