from inky import InkyWHAT
from image_utils import ImageText
from datetime import datetime, timedelta, timezone

# For debugging
import pprint
pp = pprint.PrettyPrinter(indent=4)

def create(quote):
  inky_display = InkyWHAT("black")
  inky_display.set_border(inky_display.WHITE)

  # From https://gist.github.com/jasondilworth56/27764ae8ed2327a34ceebb06e75c30ea
  from PIL import ImageFont, ImageDraw, Image

  text = quote[0]
  author = quote[1]
  title = quote[2]

  #font = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"
  #font = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
  font = "/home/pi/.fonts/Roboto-Bold.ttf"

  img = ImageText((400, 300), background=(255, 255, 255, 255))

  img.fill_text_box((10, 10), text, box_width=380, box_height=260, font_filename=font)

  meta_line = author + ', ' + title
  #img.write_text( (10, inky_display.HEIGHT - 20), meta_line, font_filename=font)
  img.fill_text_box((10, inky_display.HEIGHT - 30), meta_line, box_width=380, box_height=30, font_filename=font)

  filename = '/home/pi/src/coten/images/coten-%s.png' %datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
  img.save(filename)

  img = Image.open(filename)
  img = img.quantize()


  inky_display.set_image(img)
  inky_display.set_border(inky_display.BLACK)
  inky_display.show()




def create_old(quote):
  # From https://stackoverflow.com/questions/4902198/pil-how-to-scale-text-size-in-relation-to-the-size-of-the-image
  from PIL import ImageFont, ImageDraw, Image

  image = Image.open('templates/coten.png')
  draw = ImageDraw.Draw(image)

  txt = quote[0]
  author = quote[1]
  title = quote[2]

  fontsize = 1  # starting font size

  import textwrap
  lines = textwrap.wrap(txt, width=20)

  # portion of image width you want text width to be
  img_fraction = 0.5

  font = ImageFont.truetype("/Library/Fonts/Arial.ttf", fontsize)
  while font.getsize(lines[0])[0] < img_fraction*image.size[0]:
      # iterate until the text size is just larger than the criteria
      fontsize += 1
      font = ImageFont.truetype("/Library/Fonts/Arial.ttf", fontsize)

  # de-increment to be sure it is less than criteria
  fontsize -= 1
  font = ImageFont.truetype("/Library/Fonts/Arial.ttf", fontsize)

  print('final font size', fontsize)

  text = textwrap.fill(txt, width=20)

  # draw.text((200, 200), text, font=font, fill="Black")
  # draw.text((10, 25), txt, font=font)

  "\n".join(textwrap.wrap(txt, width=40))
  draw.text((200, 200), txt, font=font, fill="Black")

  image.save('images/coten-%s.png' %datetime.now().strftime('%d-%m-%Y-%H-%M-%S')) # save it
