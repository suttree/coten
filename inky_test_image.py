from inky import InkyWHAT

inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.open("images/test.png")
img = img.quantize()

inky_display.set_image(img)
inky_display.show()
