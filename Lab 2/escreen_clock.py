import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

##################################################################
# Display Time as "Polar-Graph" Clock
##################################################################
import numpy as np
import matplotlib.pyplot as plt
import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# pylint: disable=line-too-long
# Create the display:
# disp = st7789.ST7789(spi, rotation=90,                            # 2.0" ST7789
# disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180,  # 1.3", 1.54" ST7789
# disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14" ST7789
# disp = hx8357.HX8357(spi, rotation=180,                           # 3.5" HX8357
# disp = st7735.ST7735R(spi, rotation=90,                           # 1.8" ST7735R
# disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3,   # 1.44" ST7735R
# disp = st7735.ST7735R(spi, rotation=90, bgr=True,                 # 0.96" MiniTFT ST7735R
# disp = ssd1351.SSD1351(spi, rotation=180,                         # 1.5" SSD1351
# disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
# disp = ssd1331.SSD1331(spi, rotation=180,                         # 0.96" SSD1331
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
# pylint: enable=line-too-long

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(255, 255, 255))
disp.image(image)


# setting the axes
# projection as polar
plt.axes(projection='polar')
  
# setting the length and number of petals
# a = 1
# n = 12

# # TODO: get current date & time
# date_time = strftime("%m/%d/%Y %H:%M:%S")
# month, day, year = date_time[:10].split("/")
# hour, minutes, seconds  = date_time[-8:].split(":")

################################################


# Instantiante sampling size of radians 
rads = np.arange(0, 2 * np.pi, 0.001) 

# Instantiante Amplitude of hours, minutes, seconds roses
a_hr = 15
a_min = 10
a_sec = 5


while True:
    # Get current date & time
    date_time = strftime("%m/%d/%Y %H:%M:%S")
    month, day, year = list(map(int,date_time[:10].split("/")))  # Cast items in list to numbers
    hours, minutes, seconds  = list(map(int,date_time[-8:].split(":"))) # Cast items in list to numbers
    
    # TODO: Verify parameters plot correct number of petals according to hours, minutes, seconds
    # Seconds
    # if seconds % 2 == 0 and seconds/2 % 2 == 0: # seconds are even
    #     # seconds = seconds/2
    #     ss = a_sec * np.sin(seconds*rads)
    #     # plt.polar(rads, ss, 'g.')
    # elif seconds % 2 == 0 and seconds/2 % 2 != 0:
    #     ss = a_sec * np.cos((seconds/2)*rads)
    #     # plt.polar(rads, ss, 'g.')
    #     ss = a_sec * np.cos((seconds/2)*rads)
    #     # plt.polar(rads, ss, 'g.')
    # else: # seconds are odd
    #     ss = a_sec * np.sin(seconds*rads)
    #     # plt.polar(rads, ss, 'g.')

    # # Minutes
    # if minutes % 2 == 0 and minutes/2 % 2 == 0: # minute is even
    #     # minutes = minutes/2
    #     mm = a_min * np.sin(minutes*rads)
    #     # plt.polar(rads, mm, 'r.')
    # elif minutes % 2 == 0 and minutes/2 % 2 != 0:
    #     mm = a_min * np.cos((minutes/2)*rads)
    #     # plt.polar(rads, mm, 'r.')
    #     mm = a_min * np.cos((minutes/2)*rads)
    #     # plt.polar(rads, mm, 'r.')
    # else: # hour is odd
    #     mm = a_min * np.sin(minutes*rads)
    #     # plt.polar(rads, mm, 'r.')

    # # Hours
    # if hours == 0:
    #     hours = 12
    # if hours > 12:
    #     hours = hours - 12
    # if hours % 2 == 0 and hours/2 % 2 == 0: # hour is even
    #     # hours = hours/2
    #     hh = a_hr * np.sin(hours*rads)
    #     # plt.polar(rads, hh, 'b.')
    # elif hours % 2 == 0 and hours/2 % 2 != 0:
    #     hh = a_hr * np.cos((hours/2)*rads)
    #     # plt.polar(rads, hh, 'b.')
    #     hh = a_hr * np.sin((hours/2)*rads)
    #     # plt.polar(rads, hh, 'b.')
    # else: # hour is odd
    #     hh = a_hr * np.sin(hours*rads)
    #     # plt.polar(rads, hh, 'b.')
    
    ss = a_sec * np.sin(seconds*rads)
    mm = a_min * np.sin(minutes*rads)
    hh = a_hr * np.sin(hours*rads)
    # plt.polar(rads, mm, 'g.')
    
    # plt.polar(rads, hh, 'b.')
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, subplot_kw=dict(projection='polar'))
    ax1.plot(rads, hh, color='r')
    ax2.plot(rads, mm, color='b',)
    ax3.plot(rads, ss, color='g')
    ax1.set_yticklabels([])
    ax1.set_theta_zero_location('N')
    ax2.set_yticklabels([])
    ax2.set_theta_zero_location('N')
    ax3.set_yticklabels([])
    ax3.set_theta_zero_location('N')
    ax1.title.set_text('Hours')
    ax2.title.set_text('Minutes')
    ax3.title.set_text('Seconds')

    # Save subplots as image 
    plt.savefig("time_output.jpg")
    
    plt.close() # close plot to save resources
    
   
    # Draw a white filled box to clear the image.
    # image = Image.new("RGB", (width, height))
    # draw = ImageDraw.Draw(image)
    # draw.rectangle((0, 0, width, height), outline=0, fill=(255, 255, 255))
    # disp.image(image)

    image = Image.open("time_output.jpg").rotate(90)  # Open saved subplots showing current time 

    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True

    # Scale the image to the smaller screen dimension
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image = image.crop((x, y, x + width, y + height))

    # Display image.
    disp.image(image)
    
  

    
# display the polar plot
# plt.show()

# while True:
#     # Draw a blueish-green filled box to clear the image.
#     draw.rectangle((0, 0, width, height), outline=0, fill=(0, 51, 51))  # Cornell Tech Color set -> fill=400

#     #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    
#     time_string = strftime("%m/%d/%Y %H:%M:%S")
#     y = top
#     draw.text((x, y), time_string, font=font, fill="#FFFFFF")
    
#     # Display image.
#     disp.image(image, rotation)
#     time.sleep(1)