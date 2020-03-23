from image_utils import ImageText
from datetime import datetime, timedelta, timezone

# For debugging
import pprint
pp = pprint.PrettyPrinter(indent=4)

def create(quote):
  # From https://gist.github.com/jasondilworth56/27764ae8ed2327a34ceebb06e75c30ea
  from PIL import ImageFont, ImageDraw, Image

  text = quote[0]
  author = quote[1]
  title = quote[2]

  font = "/Library/Fonts/Arial.ttf"

  img = ImageText((800, 600), background=(255, 255, 255, 200))

  img.fill_text_box((100,100), text, box_width=600, box_height=400, font_filename=font)

  meta_line = author + ', ' + title
  img.write_text( (100, img.size[1] - 100), meta_line, font_filename=font, font_size=12)

  img.save('images/coten-%s.png' %datetime.now().strftime('%d-%m-%Y-%H-%M-%S'))

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
