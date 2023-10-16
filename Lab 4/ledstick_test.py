
from __future__ import print_function
import qwiic_led_stick
import time
import sys


my_stick = qwiic_led_stick.QwiicLEDStick()

if my_stick.begin() == False:
    print("\nThe Qwiic LED Stick isn't connected to the sytsem. Please check your connection", \
        file=sys.stderr)
print("\nLED Stick ready!")

# individual
red_list = [214, 78, 183, 198, 59, 134, 15, 209, 219, 186]
green_list = [59, 216, 170, 21, 114, 63, 226, 92, 155, 175]
blue_list = [214, 147, 25, 124, 153, 163, 188, 33, 175, 221]
my_stick.set_all_LED_unique_color(red_list, green_list, blue_list, 10)

# brightness
for i in range(0, 32):
    my_stick.set_all_LED_brightness(i)
    print("\nBrightness level: " + str(i))
    time.sleep(1)
    
# binary
# serial port and the LED stick
#     for i in range(0, 1024):
#         binary_LED_display(my_stick, i, 10)
#         binary_serial_display(i, 10)
#         time.sleep(1)
def binary_LED_display(LED_stick, count, LED_length):
    # Create color arrays because we want to turn on whole string of LEDs at one time
    red_list = [0] * LED_length
    green_list = [0] * LED_length
    blue_list = [0] * LED_length
    
    # This for loop will repeat for each pixel of the LED Stick
    for i in range(0, LED_length):
        # For ith_bit, we use the bitshift operator. count >> i takes the binary
        # representation of count and shifts it to the right i times. For example, 
        # if count was 10, 0b1010, and i was 2, we get 0b10. This aligns with the 
        # ith bit of count to the 0th bit of ith_bit
        ith_bit = count >> i
        # This will resolve to the oth bit of ith_bit
        ith_bit_true = ith_bit & 0b1
        # Write the color red to the current LED if the ith_bit_true
        # LED_stick.set_single_LED_color(10 - i, 255 * ith_bit_true, 0, 0)
        red_list[LED_length - i - 1] = 255 * ith_bit_true
    
    LED_stick.set_all_LED_unique_color(red_list, green_list, blue_list, LED_length)
def binary_serial_display(count, bit_length):
    print(str(count) + "\t" + str(bin(count)))

# end
my_stick.set_all_LED_color(50, 50, 50)
time.sleep(1)
my_stick.LED_off()
time.sleep(1)
