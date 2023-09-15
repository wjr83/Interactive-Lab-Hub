import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from adafruit_rgb_display.rgb import color565
import random
import os

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
font_size = 24
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Button configuration
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# static infomation
suggestions = {'morning' : ['Good Morning~~~~~','        (°∀°)ﾉ',
                                    'Time for a coffee!','        \ (•◡•) /',
                                    'Do some morning mediation!','        ᕙ(⇀‸↼‶)ᕗ',
                                    'Stretching Time.',
                                    'Do some light exercises.','        ☼.☼',
                                    "Plan for the day ahead.",'        (>人<)'],
                       'noon': ['Stay hydrated!',"        (ง'̀-'́)ง",
                                "Grab a snack to keep up energy.",'        (ღ˘⌣˘ღ)',
                                'Check your emails',
                                'Prioritize tasks.',
                                "Take a short break :D",
                                "Do a mindfulness exercise.",
                                'Get some fresh air.'],
                       "afternoon": ["Wind down and review your day's progress.",'        ƪ(˘⌣˘)ʃ',
                                    "Spend time with family or friends.",
                                    "Have a relaxing evening routine.",
                                    "Take a walk for a mental break.",
                                    'Time for some exercise!','        (°∀°)ﾉ',
                                    'Live in the moment.'] ,
                       'night' : ['Goodnight~~~~~','            ヾ(o◕∀◕)ﾉ',
                                  "Limit screen time for better sleep.",'            ʕ•ᴥ•ʔ',
                                  "Practice deep breathing to unwind.",'            _(:3」∠)____',
                                  "Reflect on the positive moments.",'            (° ͡ ͜ ͡ʖ ͡ °)',
                                  "Prepare for tomorrow and set goals.",'            ƪ(˘⌣˘)ʃ']  }
texts = {'morning' : ['GOOD DAY'],
         'noon' : ['SMILE'],
         'afternoon': ['TEA TIME'],
         'night': ['REST','SLEEP','NIGHT'],
         'spring':['Bloosom'],
         'summer':['Beach Time'],
         'fall':['Chill','Warm','AUTUMN'],
         'winter':['Snow Season']}
background_color_map = {'morning':color565(0,102,0),
                        'noon':color565(0,51,102),
                        'afternoon':color565(204,102,0),
                        'night':color565(32,32,32)}
text_color_map = {'morning':color565(255,0,0),
                'noon':color565(255,128,0),
                'afternoon':color565(127,0,255),
                'night':"#0000FF"}
# helper functions for random returns
def randomColor():
    j1 = random.randint(0, 255)       
    j2 = random.randint(0, 255)  
    j3 = random.randint(0, 255)  
    return color565(j1, j2, j3)
def randomImg(d, s):
    if random.randint(0, 1) == 0:
        t = 'background/time'
        k = d
    else:
        t = 'background/date'
        k = s
    time_files = os.listdir(t)
    time_files = [f for f in time_files if f.split("_")[0] == k]
    img_path = t+'/'+time_files[random.randint(0, len(time_files)-1)]
    
    img_text = texts[k][random.randint(0, len(texts[k])-1)]
    return img_path, img_text

# i = random.randint(0, 4)
while True:
    hour = int(strftime("%H"))
    month = int(strftime("%m"))
    if hour < 5 or hour >= 21:
        d = 'night'
    elif hour < 10:
        d = 'morning'
    elif hour < 14:
        d = 'noon'
    elif hour < 18:
        d = 'afternoon'
    else:
        d = 'night'
    
    if month < 3 or month >= 12:
        s = 'winter'
    elif month < 6:
        s = 'spring'
    elif month < 9:
        s = 'summer'
    else:
        s = 'fall'
        
    # Default Display -- background color change by time
    # Draw a black filled box to clear the image.
    background_color = background_color_map[d]
    text_color = text_color_map[d]
    draw.rectangle((0, 0, width, height), outline=0, fill=background_color)
    
    date_text = strftime("%m/%d/%Y")   
    time_text =  strftime("%H:%M:%S") 
    draw.text((52, 40), date_text, font=font, fill=text_color)
    draw.text((68, 64), time_text, font=font, fill=text_color)
    
    
        
    y = top
    
    a_scroll_position = 0
    b_scroll_position = 0
    
    if buttonB.value and not buttonA.value:  # just button A pressed
        suggestion = suggestions[d]                
        i = random.randint(0, len(suggestion)-1)     
        while buttonB.value and not buttonA.value:   
            draw.rectangle((0, 0, width, height), outline=0, fill=0)       
            draw.text((10 - a_scroll_position, 54), suggestion[i], font=font, fill=randomColor())
            # y+=18
            a_scroll_position = (a_scroll_position + 15) % 200
            disp.image(image, rotation)
            time.sleep(0.1)
    # if buttonA.value and not buttonB.value:  # just button B pressed to be done
        # while buttonA.value and not buttonB.value:
            # disp.fill(color565(255, 255, 255))  # set the screen to white
    while not buttonA.value and not buttonB.value:  # both pressed
        img_path, img_text = randomImg(d, s)
        back_image = Image.open(img_path)
        # while not buttonB.value:
        # Scale the image to the smaller screen dimension
        image_ratio = back_image.width / back_image.height
        screen_ratio = width / height
        if screen_ratio < image_ratio:
            scaled_width = back_image.width * height // back_image.height
            scaled_height = height
        else:
            scaled_width = width
            scaled_height = back_image.height * width // back_image.width
        back_image = back_image.resize((scaled_width, scaled_height), Image.BICUBIC)
        # Crop and center the image
        x = scaled_width // 2 - width // 2
        y = scaled_height // 2 - height // 2
        back_image = back_image.crop((x, y, x + width, y + height))
        image.paste(back_image, (0,0))
        image.paste(back_image, (0,0))
        image.paste(back_image, (0,0))
        
        draw.text((88, 54), img_text, font=font, fill="#FFFFFF")
            # disp.image(back_image, rotation)
            # time.sleep(0.5)

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.15)
    
    # print([f for f in os.listdir('background/time') if f.split("_")[0] == 'noon'])
    

