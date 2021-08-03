#!/usr/bin/env python
# coding: utf-8

# <H2> Code Breakdown </H2>
#"C:/Users/nnour/Desktop/!dev/threading/images/test.jpg"
infile_path = "8872.jpg"
#input("Enter the image file path : ")
# hello
# Constants
INPUT_IMAGE_FILE = infile_path
OUTPUT_IMAGE_FILE = infile_path + ".converted.png"
FONT_LOCATION = "calibrib.ttf"
FONT_SIZE = 80
H_SPACING = 70
V_SPACING = 90
FONT_OPACITY = 75
WATERMARK_TEXT = " COPYRIGHT @ TNB 2020 "

# Importing essential packages from PIL
from PIL import Image, ImageDraw, ImageFont

# opening image
im = Image.open(INPUT_IMAGE_FILE)
font = ImageFont.truetype(FONT_LOCATION, FONT_SIZE)
watermark_text = WATERMARK_TEXT
im_width, im_height = im.size  # gathering parent image size

# Creating editable image
drawing = ImageDraw.Draw(im)
text_width, text_height = drawing.textsize(watermark_text, font)  # gathering size of the text

# Initializing text watermark sub image
im_text = Image.new('RGBA', (text_width, text_height),
                    (255, 255, 255, 0))  # creating new transparent sub image for watermark text
drawing = ImageDraw.Draw(im_text)
drawing.text((0, 0), watermark_text, fill=(255, 255, 255, FONT_OPACITY),
             font=font)  # adding the text to the new sub-image

current_width = im_width
current_height = im_height

up_down = +1  # for interesting tiling pattern ( up down position difference )

# Looping for additional watermarks
new_position = (current_width - text_width) - H_SPACING, current_height + (up_down * (V_SPACING // 2))
#top ling
im.paste(im_text, (0, 0), im_text)  # pasting the watermark on the parent image
im.paste(im_text, (1600, 0), im_text)
im.paste(im_text, (3200, 0), im_text)
im.paste(im_text, (4800, 0), im_text)
im.paste(im_text, (6400, 0), im_text)

#middle line
im.paste(im_text, (0, 2000), im_text)  # pasting the watermark on the parent image
im.paste(im_text, (1600, 2000), im_text)
im.paste(im_text, (3200, 2000), im_text)
im.paste(im_text, (4800, 2000), im_text)
im.paste(im_text, (6400, 2000), im_text)


# bottom horizontal watermark line repeat
# while current_width > text_width + H_SPACING:
#     new_position = (current_width - text_width) - H_SPACING, current_height + (up_down * (V_SPACING // 2))
#     im.paste(im_text, new_position, im_text)  # pasting the watermark on the parent image
#     current_width, current_height = new_position
#
#     # Creating vertical repeat for each horizontal one in the bottom line
#
#     repeat_current_width, repeat_current_height = new_position
#
#     while repeat_current_height > text_height + V_SPACING:
#         repeat_new_position = repeat_current_width, (repeat_current_height - text_height - V_SPACING)
#         im.paste(im_text, repeat_new_position, im_text)  # pasting the watermark on the parent image
#         repeat_current_width, repeat_current_height = repeat_new_position
#
#     up_down *= -1

# saving output to outfile
im.save(OUTPUT_IMAGE_FILE)
