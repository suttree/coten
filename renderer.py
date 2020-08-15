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
  font = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
  #font = "/home/pi/.fonts/Roboto-Bold.ttf"

  #font = "/home/pi/.fonts/Bitter-Regular.otf"
  #font = "/home/pi/.fonts/ufonts.com_rockwell.ttf"
  #font = "/home/pi/.fonts/Bookerly/Bookerly-Regular.ttf"
  #font = "/home/pi/.fonts/static/PlayfairDisplay-Regular.ttf"
  #font = "/home/pi/.fonts/PlayfairDisplay-VariableFont_wght.ttf"
  font = "/home/pi/.fonts/FredokaOne-Regular.ttf"
  #font = "/home/pi/.fonts/AmaticSC-Regular.ttf"

  img = ImageText((400, 300), background=(255, 255, 255))

  img.fill_text_box((20, 20), text, box_width=340, box_height=250, font_filename=font)

  meta_line = author + ', ' + title
  #img.write_text( (10, inky_display.HEIGHT - 20), meta_line, font_filename=font)
  #img.fill_text_box((30, inky_display.HEIGHT - 40), meta_line, box_width=320, box_height=30, font_filename=font)
  img.write_text_box((30, inky_display.HEIGHT - 30), meta_line, box_width=320, font_filename=font, font_size=12, place='right')

  filename = '/home/pi/src/coten/images/coten.png'
  img.save(filename)

  img = Image.open(filename)
  img = img.quantize()

  inky_display.set_image(img)
  inky_display.set_border(inky_display.WHITE)
  inky_display.show()

# Adapted from the Pimoroni inkyWhat examples: https://github.com/pimoroni/inky
def create_pimoroni(quote):
	import argparse
	import random
	import sys

	from inky import InkyWHAT

	from PIL import Image, ImageFont, ImageDraw
	from font_source_serif_pro import SourceSerifProSemibold
	from font_source_sans_pro import SourceSansProSemibold
	
	# Set up the correct display and scaling factors
	inky_display = InkyWHAT('black')
	inky_display.set_border(inky_display.WHITE)
	# inky_display.set_rotation(180)

	w = inky_display.WIDTH
	h = inky_display.HEIGHT

	# Create a new canvas to draw on
	img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
	draw = ImageDraw.Draw(img)

	# Load the fonts
	font_size = 24
	author_font_size = 18

	quote_font = ImageFont.truetype(SourceSansProSemibold, font_size)
	author_font = ImageFont.truetype(SourceSerifProSemibold, author_font_size)

	# The amount of padding around the quote. Note that
	# a value of 30 means 15 pixels padding left and 15
	# pixels padding right.
	#
	# Also define the max width and height for the quote.

	padding = 50
	max_width = w - padding
	max_height = h - padding - author_font.getsize("ABCD ")[1]

	below_max_length = False

	# Only pick a quote that will fit in our defined area
	# once rendered in the font and size defined.

	while not below_max_length:
			reflowed = reflow_quote(quote, max_width, quote_font)
			p_w, p_h = quote_font.getsize(reflowed)  # Width and height of quote
			p_h = p_h * (reflowed.count("\n") + 1)   # Multiply through by number of lines

			if p_h < max_height:
					below_max_length = True              # The quote fits! Break out of the loop.

			else:
					font_size = font_size - 1
					author_font_size = author_font_size - 1

					quote_font = ImageFont.truetype(SourceSansProSemibold, font_size)
					author_font = ImageFont.truetype(SourceSerifProSemibold, author_font_size)

					continue

	# x- and y-coordinates for the top left of the quote
	quote_x = (w - max_width) / 2
	quote_y = ((h - max_height) + (max_height - p_h - author_font.getsize("ABCD ")[1])) / 2

	# x- and y-coordinates for the top left of the author
	author_x = quote_x
	author_y = quote_y + p_h

	author = [ '— ' + quote[1] + ', ' + quote[2] ]
	reflowed_author = reflow_quote(author, max_width, author_font)

	# Write our quote and author to the canvas
	draw.multiline_text((quote_x, quote_y), reflowed, fill=inky_display.BLACK, font=quote_font, align="left")
	draw.multiline_text((author_x, author_y), reflowed_author, fill=inky_display.BLACK, font=author_font, align="right")

	print(reflowed + "\n" + reflowed_author + "\n")

	# Display the completed canvas on Inky wHAT
	inky_display.set_image(img)
	inky_display.show()

# This function will take a quote as a string, a width to fit
# it into, and a font (one that's been loaded) and then reflow
# that quote with newlines to fit into the space required.
def reflow_quote(quote, width, font):
	words = quote[0].split(" ")
	reflowed = ''
	line_length = 0

	for i in range(len(words)):
			word = words[i] + " "
			word_length = font.getsize(word)[0]
			line_length += word_length

			if line_length < width:
					reflowed += word
			else:
					line_length = word_length
					reflowed = reflowed[:-1] + "\n" + word

	reflowed = reflowed.rstrip() + ''

	return reflowed
