import random
import os
import board
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960
import time
import subprocess
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from adafruit_rgb_display.rgb import color565
from adafruit_bus_device.i2c_device import I2CDevice
from struct import pack, unpack
import smbus
import sxtwl
import adafruit_mpr121
from zhdate import ZhDate
import datetime

bus = smbus.SMBus(1)


# import smbus
# bus = smbus.SMBus(1)
# for address in range(0x08, 0x78):
#     try:
#         # Try to read a byte from the current address
#         bus.read_byte(address)
#         print(f"Device found at address: 0x{hex(address)}")
#     except:
#         pass
    
i2c = busio.I2C(board.SCL, board.SDA)

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

# apds9960 configuration
apds = APDS9960(i2c)
apds.enable_gesture = True
apds.enable_proximity = True

# owicc button config
o_button_STATUS = 0x03 # reguster for button status
o_button_AVAILIBLE = 0x1
o_button_BEEN_CLICKED = 0x2
o_button_IS_PRESSED = 0x4
o_button = I2CDevice(i2c, 0x6f)
def write_register(dev, register, value, n_bytes=1):
    # Write a wregister number and value
    buf = bytearray(1 + n_bytes)
    buf[0] = register
    buf[1:] = value.to_bytes(n_bytes, 'little')
    with dev:
        dev.write(buf)
def read_register(dev, register, n_bytes=1):
    # write a register number then read back the value
    reg = register.to_bytes(1, 'little')
    buf = bytearray(n_bytes)
    with dev:
        dev.write_then_readinto(reg, buf)
    return int.from_bytes(buf, 'little')
write_register(o_button, 0x1A, 1)
write_register(o_button, 0x1B, 0, 2)
write_register(o_button, 0x19, 0)

global bus_data, X, Y    
# qwiicjoystick = qwiicjoystick()
def qwiicjoystick():
    global bus_data, X, Y
    bus_data = bus.read_i2c_block_data(0x20, 0x03, 5)
    X = (bus_data[0]<<8 | bus_data[1])>>6
    Y = (bus_data[2]<<8 | bus_data[3])>>6
    
    if X < 450:
        direction = 'right'
    elif 575 < X:
        direction = 'left'
    if Y< 450:
        direction = 'down'
    elif 575 < Y:
        direction = 'up'
    return direction


# mpr121 touch
mpr121 = adafruit_mpr121.MPR121(i2c,0x5a)

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
directions_map = {0x01:'up',0x02:"down",0x03:"left",0x04:'right'}
directions_map2 = {0x01: 10,0x02: -10, 0x03:-1, 0x04:+1}
directions_map3 = {'up':'rising',"down": 'dive deeper',"left":'look around','right':'look back'}


# resize img
def img_ratio(back_image):
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
    return back_image
# draw default_background with fill_color
def default_display(loc = (0, 0, width, height), outline=0, fill=(0, 0, 0)):
    draw.rectangle(loc, outline=outline, fill=fill)

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

def disp_image(file_path = "default.jpg"):
    image = Image.open(file_path)
    image = img_ratio(image)
    disp.image(image, rotation)
    return image
# def default_draw(image = image):
#     return ImageDraw.Draw(default_image())

image = disp_image()
draw = ImageDraw.Draw(image)
# draw = default_draw()
# i = random.randint(0, 4)
def display_text(draw_xy = (0, 0), text = "d", font = font, fill=(0, 0, 0)):
    cp = image.copy()
    draw = ImageDraw.Draw(cp)
    draw.text(draw_xy, text, font=font, fill=fill)
    disp.image(cp, rotation)
 
def display_text_multiline(draw_xy = [(0, 0)], text = ["d"], font = font, fill=(0, 0, 0)):
    cp = image.copy()
    draw = ImageDraw.Draw(cp)
    for i in range(len(draw_xy)):
        draw.text(draw_xy[i], text[i], font=font, fill=fill)
    disp.image(cp, rotation)
 
twelve = {
    1: ['乾', [1, 1, 1]],
    2: ['兑', [0, 1, 1]],
    3: ['离', [1, 0, 1]],
    4: ['震', [0, 0, 1]],
    5: ['巽', [1, 1, 0]],
    6: ['坎', [0, 1, 0]],
    7: ['艮', [1, 0, 0]],
    8: ['坤', [0, 0, 0]],
}
dict_move = {
    str([1, 1, 1]): '乾',
    str([0, 1, 1]): '兑',
    str([1, 0, 1]): '离',
    str([0, 0, 1]): '震',
    str([1, 1, 0]): '巽',
    str([0, 1, 0]): '坎',
    str([1, 0, 0]): '艮',
    str([0, 0, 0]): '坤'
}
# 先天八卦数：乾 1 兑 2 离 3 震 4 巽 5 坎 6 艮 7 坤 8 
def format_time():
    tiangan = (year - 3) % 10
    dizhi = (year - 3) % 12
    if time >= 23 or time < 1:
        shichen = 1
    elif 1 <= time < 3:
        shichen = 2
    elif 3 <= time < 5:
        shichen = 3
    elif 5 <= time < 7:
        shichen = 4
    elif 7 <= time < 9:
        shichen = 5
    elif 9 <= time < 11:
        shichen = 6
    elif 11 <= time < 13:
        shichen = 7
    elif 13 <= time < 15:
        shichen = 8
    elif 15 <= time < 17:
        shichen = 9
    elif 17 <= time < 19:
        shichen = 10
    elif 19 <= time < 21:
        shichen = 11
    else:
        shichen = 12
    get_num(dizhi, shichen)
def get_num(dizhi, shichen):
    up = (dizhi + mouth + day) % 8 if (dizhi + mouth + day) % 8 else 8
    down = (dizhi + mouth + day + shichen) % 8 if (dizhi + mouth + day + shichen) % 8 else 8
    move = (dizhi + mouth + day + shichen) % 6 if (dizhi + mouth + day + shichen) % 6 else 6
    show(up, down, move)
def show(up, down, move):
    result = twelve[up] + twelve[down]
    all_num = result[1] + result[3]
    # 初卦
    result1 = result[0] + result[2]
    # 互卦
    hu_up = str(all_num[1:4])
    hu_down = str(all_num[2:5])
    result2 = dict_move[hu_up] + dict_move[hu_down]
    # 变卦
    all_num[move - 1] = abs(all_num[move - 1] - 1)
    move_up = str(all_num[:3])
    move_down = str(all_num[3:])
    result3 = dict_move[move_up] + dict_move[move_down]

    if move < 4:
        use = '。'
    else:
        use = '  ' + '。'
    print(result1)
    print(result2)
    print(result3)
 
t0 = -1  
while True:
    try:
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
        
        # background_color = background_color_map[d]
        # default_display(fill = background_color)
        text_color = text_color_map[d]

        date_text, time_text = strftime("%m/%d/%Y"), strftime("%H:%M:%S")  
        display_text_multiline([(52, 40), (68, 64)], [date_text,time_text], fill=(255,255,255))   
        
        y = top
        
        a_scroll_position = 0
        b_scroll_position = 0
        
        # # strftime("%m/%d/%Y"), strftime("%H:%M:%S") 
        # for i in range(12):
        #     if mpr121[i].value:
        #         while True:
                    
                #     now = str(datetime.datetime.today())
                #     year = int(now[:4])
                #     mouth = int(now[5:7])
                #     day = int(now[8:10])
                #     time = int(now[11:13])
                #     # print(int(strftime("%y")), int(strftime("%m")), int(strftime("%d")))
                #     # lunar_day = ZhDate.today()
                #     # lunar_yr,lunar_mon, lunar_d = lunar_day[2:6],lunar_day[2:6]
                #     # print(lunar_yr, lunar_mon, lunar_d)
                #     format_time()
                # # elif i == 12:
                #     while True:
                #         print('s')
                    
                    
                    
                
        if buttonB.value and not buttonA.value:
            suggestion = suggestions[d]                
            i = random.randint(0, len(suggestion)-1)     
            while buttonB.value and not buttonA.value:  
                display_text((10 - a_scroll_position, 54), suggestion[i], fill=randomColor())    
                # y+=18
                a_scroll_position = (a_scroll_position + 15) % 200
                time.sleep(0.1)
        if buttonA.value and not buttonB.value:
            t0 = time.time()
            image = disp_image('default_b.jpg')
            
            display_text(text='Marine Tour Begins',fill = (255,255,255))
            time.sleep(3)
            min_h, max_h = -100, 60
            aqua_files = os.listdir('aqua')
            h = 0
            v = 1
                    
            while True:
                gesture = apds.gesture()
                current_h_files = [f for f in aqua_files if f.split("_")[0] == str(h)]
                min_v, max_v = 1, max([int(f.split("_")[1][0]) for f in current_h_files])
                img_path = 'aqua/'+str(h)+'_'+str(v)+'.jpg'
                image = disp_image(img_path)
                if gesture in directions_map:
                    direction = directions_map[gesture]
                    move = directions_map2[gesture]
                    if h + move > min_h and h+move < max_h:
                        display_text(text=directions_map3[direction], fill = (255,255,255))
                        if abs(move) == 1:
                            v += move
                            v = max(min_v, v)
                            v = min(max_v, v)
                            img_path = 'aqua/'+str(h)+'_'+str(v)+'.jpg'
                            image = disp_image(img_path)
                        else:
                            h += move
                            v = 1
                            img_path = 'aqua/'+str(h)+'_'+str(v)+'.jpg'
                            image = disp_image(img_path)
                    else:
                        display_text(text='Back to Human World', fill = (255,255,255))
                        image = disp_image()
                        t1 = time.time()
                        break
                
                if buttonB.value and not buttonA.value: 
                    image = disp_image()
                    t1 = time.time()
                    break
                time.sleep(1)
        if not buttonA.value and not buttonB.value:  # both pressed
            while True:
                img_path, img_text = randomImg(d, s)
                back_image = Image.open(img_path)
                back_image = img_ratio(back_image)
                
                image.paste(back_image, (0,0))
                
                draw.text((88, 54), img_text, font=font, fill="#FFFFFF")
                    # disp.image(back_image, rotation)
                print(-111)
                
                if (buttonB.value and not buttonA.value): 
                    break
        while t0 != -1:
            if buttonB.value and not buttonA.value:
                t0 =-1
            if t0 == -1:
                break
            time_p = t1-t0
            ani_died = time_p * 0.0316887385
            k = random.randint(100,255)
            display_text_multiline(draw_xy = [(-2, 40),(14, 64)], text = ['% .4f' % ani_died + 'Animial Died', 'During your Visit'], font = font, fill=(255,k,k))
        
            prox = apds.proximity
            if prox != 0:
                # t0 = -1
                break
            print(prox)
        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
        
        # print([f for f in os.listdir('background/time') if f.split("_")[0] == 'noon'])
        

    except KeyboardInterrupt:
        # on control-c do...something? try commenting this out and running again? What might this do
        # write_register(o_button, o_button_STATUS, 0)
        break
