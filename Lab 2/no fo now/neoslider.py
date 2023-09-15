# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple seesaw test using an LED attached to Pin 15.
#
# See the seesaw Learn Guide for wiring details:
# https://learn.adafruit.com/adafruit-seesaw-atsamd09-breakout?view=all#circuitpython-wiring-and-test
import time

import board
import busio
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.analoginput import AnalogInput
from adafruit_seesaw import neopixel

i2c = busio.I2C(board.SCL, board.SDA)

ss = Seesaw(i2c, addr=0x30)
potentiometer = AnalogInput(ss, 18)
pixels = neopixel.NeoPixel(ss, 14, 4, pixel_order=neopixel.GRB)


ss.pin_mode(15, ss.OUTPUT)

while True:
    ss.digital_write(15, True)  # turn the LED on (True is the voltage level)
    time.sleep(1)  # wait for a second
    ss.digital_write(15, False)  # turn the LED off by making the voltage LOW
    time.sleep(1)
    
    
# def potentiometer_to_color(value):
#     """Scale the potentiometer values (0-1023) to the colorwheel values (0-255)."""
#     return value / 1023 * 255


# while True:
#     ss.digital_write(15, True)
#     print(potentiometer.value)
    
    
# while True:
#     ss.digital_write(15, True)  # turn the LED on (True is the voltage level)
#     time.sleep(1)  # wait for a second
#     ss.digital_write(15, False)  # turn the LED off by making the voltage LOW
#     time.sleep(1)