from __future__ import print_function
from PIL import Image

im = Image.open("C:/Users/rjilani/Documents/download-bkup/sample.tif")

print(im.format, im.size, im.mode)

im.show()