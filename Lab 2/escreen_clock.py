import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
import busio
from adafruit_bus_device.i2c_device import I2CDevice
from struct import pack, unpack
import RPi.GPIO as GPIO            # import RPi.GPIO module for buttons   
import subprocess
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import digitalio
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import

# Stop two scripts from trying to use the screen at once.
subprocess.call(["sudo", "systemctl", "stop", "mini-screen.service"])
sleep(2)

# Foods [Temperature, Cooking  in seconds (Minutes*60)]
food_temp_time = {
  'chicken' : ['Medium Heat', 20*60],
  'fish' : ['Med-High Heat', 10*60],
  'lamb' : ["High Heat", 15*60],
  'pork' : ["High Heat", 15*60], 
  'shrimp' : ["Med-High Heat", 6*60],
  'steak' : ["High Heat", 13*60], 
}

# TODO: Improve Display of Images to show entire images (including time plots & )
# Define filepaths of images to display:
img_filepaths = {
    'time_output' : "Images/time_output.jpg",
    'countdown_output' : "Images/countdown_output.jpg",
    'bon_appetit' : 'Images/bon_appetit.png',
    'grill_menu' : 'Images/grill_menu.png',
    'lets_cook' : 'Images/lets_cook.png',
    'chicken' : "Images/chicken.jpg",
    'lamb' : 'Images/lamb.jpg',
    'pork' : "Images/pork.jpg",
    'fish' : "Images/fish.jpg",
    'shrimp' : "Images/shrimp.jpg",
    'steak' : "Images/steak.jpg",
    'flip_protein' : "Images/flip_protein.png"
}

# Instantiante sampling size of radians 
rads = np.arange(0, 2 * np.pi, 0.001) 

# Instantiante Amplitude of hours, minutes, seconds roses
a_hr = 15
a_min = 10
a_sec = 5

# Returns name of current image shown
def get_food(image_filepath):
    return Path(image_filepath).name.split(".")[0]

# Returns temperature of food image shown
def get_cooking_temp(image_name):
    return food_temp_time[image_name][0]

# Returns cooking time of food image shown
def get_cooking_time(image_name):
    return food_temp_time[image_name][1]

# Display Image to Screen
def image_raspPi(image_filepath):
    # if image == "Images\\time_output.jpg":
    image = Image.open(Path(image_filepath)).rotate(90)
    # image = add_margin(image, 600, 100, 600, 100, (255, 255, 255))
    # else:
    #     image = Image.open(Path(image))
    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True

    # Width of Plot: 640px | Height of Plot: 480px
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

    return image
    # Display image.

def disp_out(image_filepath):
    t_image = image_raspPi(image_filepath)
    disp.image(t_image)

# Timer (Currently only works for mintues and seconds)
def timer(image_name):

    # Get cooking time of food
    t = get_cooking_time(image_name) # t = seconds (type: int)

    # Start Timer (TODO: Add functionality to stop, continue and reset timer)
    hour = 0
    while t:
        
        mins, secs = divmod(t, 60)      # Convert minute to minutes and seconds
        # hours, mins = divmod(mins, 60) 
        print(f"Time Remaining: {hour:02d}:{mins:02d}:{secs:02d} (hh:mm_ss)") # For troubleshooting
        # if hour != hours:
        #     hour = hours
        # if hour - hours ==1:
        #     mins = 60

        halftime = float(2*(mins*60 + secs))
        # print([mins, secs])
        # print(float(2*(mins*60 + secs))) 
        # print(float(get_cooking_time(image_name)))
        # Display Time to Flip Protein
        

        ss = a_sec * np.sin(secs*rads)
        mm = a_min * np.sin(mins*rads)
        hh = a_min * np.sin(hour*rads)

        # Plot countdown as a polar plot of sin()
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, subplot_kw=dict(projection='polar'))
        ax1.plot(rads, hh, color='r',)
        ax1.axis('off') # Remove Degree Labels on Polar Subplots
        ax2.plot(rads, mm, color='b',)
        ax2.axis('off') # Remove Degree Labels on Polar Subplots
        ax3.plot(rads, ss, color='g')
        ax3.axis('off') # Remove Degree Labels on Polar Subplots
        ax1.set_yticklabels([])
        ax1.set_theta_zero_location('N')
        ax2.set_yticklabels([])
        ax2.set_theta_zero_location('N')
        ax3.set_yticklabels([])
        ax3.set_theta_zero_location('N')
        
        # Set Title & Black Background Plots
        ax1.set_title('Hours', color='white')
        ax2.set_title('Cooking Time Left\nMinutes', color='white')
        ax3.set_title('Seconds', color='white')
        fig.set_facecolor('black')

        if halftime == float(get_cooking_time(image_name)):
                    disp_out(img_filepaths['flip_protein'])
                    sleep(5)
                    
        elif halftime == float(get_cooking_time(image_name))-1: # Accounts for odd cooking time
            disp_out(img_filepaths['flip_protein'])
            sleep(5)


        # Save subplots as image 
        plt.savefig(img_filepaths['countdown_output'])
        plt.close() # close plot to save resources

        disp_out(img_filepaths['countdown_output']) 
        # Subtract 1 second
        sleep(1)
        t -= 1
    sleep(1.5)

        
#Helper function to pad image background with white
def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

# Plot Time
def plot_time():
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
        
        # Generate function output for plotting time on a polar graph.
        ss = a_sec * np.sin(seconds*rads)
        mm = a_min * np.sin(minutes*rads)
        # Hours
        if hours == 0:
            hours = 12
        if hours > 12:
            hours = hours - 12
        hh = a_hr * np.sin(hours*rads)

        
        # Plot time as a polar plot of sin()
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, subplot_kw=dict(projection='polar'))
        ax1.plot(rads, hh, color='r', )
        ax1.axis('off') # Remove Degree Labels on Polar Subplots
        ax2.plot(rads, mm, color='b',)
        ax2.axis('off') # Remove Degree Labels on Polar Subplots
        ax3.plot(rads, ss, color='g')
        ax3.axis('off') # Remove Degree Labels on Polar Subplots
        ax1.set_yticklabels([])
        # ax1.set_theta_zero_location('N')
        ax2.set_yticklabels([])
        ax2.set_theta_zero_location('N')
        ax3.set_yticklabels([])
        ax3.set_theta_zero_location('N')
        ax1.title.set_text('Hours')
        ax2.title.set_text('Current Time\nMinutes')
        ax3.title.set_text('Seconds')
        
        

        # Save subplots as image 
        plt.savefig(img_filepaths['time_output'])
        
        plt.close() # close plot to save resources




# GPIO.setup(23, GPIO.OUT)           # set GPIO24 as an output   
# GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output   
# GPIO.output(23, 1)         # set GPIO24 to 1/GPIO.HIGH/True (Button A, upper) (0/GPIO.LOW/FALSE)
# GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True (BUtton B, lower) (0/GPIO.LOW/FALSE)

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
# setting the length and number of petals
# a = 1
# n = 12

# # TODO: get current date & time
# date_time = strftime("%m/%d/%Y %H:%M:%S")
# month, day, year = date_time[:10].split("/")
# hour, minutes, seconds  = date_time[-8:].split(":")

################################################
# TODO: Implement useful / reudable button logics 
def button_logic():
    while True:
        # Get current date & time

        plot_time()
        
        # image = Image.open("Images\\time_output.jpg").rotate(90)  # Open saved subplots showing current time 

        # Display Image
        

        # Add white margin to image
        # image = add_margin(image, 50, 100, 50, 100, (0, 255, 100)) # left, bottom, right, top
        # image.save('time_output.jpg', quality=100)
        # image = Image.open("time_output.jpg")

        #TODO: Incorporate button functionality into telling of time
        try:  
            print(GPIO.input(24))
            # sleep(0.5)                 # wait half a second  
            if GPIO.input(23) == 1:
                GPIO.output(23, 1)  
                print("Button B is unpressed")
                t_image = image_raspPi(img_filepaths['time_output'])
                disp.image(t_image)  

            # GPIO.output(24, 0)         # set GPIO24 to 0/GPIO.LOW/False  
            # sleep(0.5)                 # wait half a second  
                
            if GPIO.input(24) == 0:
                GPIO.output(24, 0)  
                print("Button was pressed") 
                image = image_raspPi(img_filepaths['flip_protein'])
                disp.image(image)
                

                

        except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
            GPIO.cleanup()    

        
        # Draw a white filled box to clear the image.
        # image = Image.new("RGB", (width, height))
        # draw = ImageDraw.Draw(image)
        # draw.rectangle((0, 0, width, height), outline=0, fill=(255, 255, 255))
        # disp.image(image)

    
    
  

    
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


GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  

def set_buttons_HIGH():
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def set_buttons_LOW():
    GPIO.setup(23, GPIO.OUT)           # set GPIO24 as an output   
    GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output   
    GPIO.output(23, 0)         # set GPIO24 to (0/GPIO.LOW/FALSE)
    GPIO.output(24, 0)         # set GPIO24 to (0/GPIO.LOW/FALSE)

# Main Function (TODO: Add functionality to return to main menu where the current time is displayed)    
def cook():
    #Display current time unless either button is pressed. 
    set_buttons_HIGH()
    while GPIO.input(23) == GPIO.HIGH:
        plot_time()
        disp_out(img_filepaths['time_output'])
        if GPIO.input(24) != GPIO.HIGH:
            continue


    # Display Welcome Screen
    sleep(1)
    set_buttons_HIGH()
    while GPIO.input(23) == GPIO.HIGH and GPIO.input(24) == GPIO.HIGH:
        disp_out(img_filepaths['grill_menu'])
        

    # Display Available Proteins
    # sleep(1)
    sleep(1)
    set_buttons_HIGH()
    sleep(0.1)
    flag = True
    for key, value in img_filepaths.items():
        if flag == True:
            if key in food_temp_time.keys():
                
                disp_out(value) # Display food item (value is the filepath of the current food item)
                
                # Wait for button response
                while True:
                    try: 
                        
                        # Check the state of the GPIO pin
                        if GPIO.input(23) == GPIO.LOW:         # Show next available menu item.    
                            print("Button A was pressed!")
                            break # Display next food item
                            
                        if GPIO.input(24) == GPIO.LOW:         # Select meal to cook
                            print("Button B was pressed!")  
                            
                            #Display image "Let's Cook"
                            disp_out(img_filepaths['lets_cook'])
                            sleep(2)

                            # Display Cooking Temperature.
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
                            draw.rectangle((0, 0, width, height), outline=0, fill=(11, 8, 48))  # Cornell Tech Color set -> fill=400
                            
                            temperature = "Cooking Temperature \nfor " + key + ": \n" + get_cooking_temp(key) + "\n\n"
                            cooking_time = "Cooking Time \nfor " + key + ": " + str(get_cooking_time(key)/60) + " min"
                            y = top
                            draw.text((x, y), temperature + cooking_time, font=font, fill="#FFFFFF")
                            
                            # Display image.
                            disp.image(image, rotation)
                            sleep(5)

                            # Start Timer
                            timer(key)
                            flag = False # To break for loop after timer is done.

                            #Display Bon Appetit
                            disp_out(img_filepaths['bon_appetit'])
                            sleep(5)
                            break   # Break While Loop
                    except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
                        GPIO.cleanup()  
        else:
            break
                  
    # Recursive call to function to see menu options again
    # Cycle through menu options 
    cook()        
    


    # Cyle Through Proteins (Button A = Next, Button B = Select Protein)

    # User Selects Protein (Feedback From Button)

    # Show Timer to User

    # Display "Time to Flip Protein"

    # Continue Displaying Timer to User

    # Notify Food is Ready  

    # Return to Menu Selection (Press both buttons)


cook()

# Create a loop that will wait for a button press
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# while True:
#     # Check the state of the GPIO pin
#     if GPIO.input(23) == GPIO.LOW:
#         print("Button was pressed!")
        
#     if GPIO.input(23) == GPIO.HIGH:
#         print("Not pressed.")
        
#     # Wait 0.1 seconds before checking the button state again
#     sleep(0.1)