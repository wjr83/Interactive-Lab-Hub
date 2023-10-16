import time
import board
import busio


# import smbus
# bus = smbus.SMBus(1)
# for address in range(0x08, 0x78):
#     try:
#         # Try to read a byte from the current address
#         bus.read_byte(address)
#         print(f"Device found at address: 0x{hex(address)}")
#     except:
#         pass

# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
NeoSlider NeoPixel Rainbow Demo
"""
import board
from rainbowio import colorwheel
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.analoginput import AnalogInput
from adafruit_seesaw import neopixel

# NeoSlider Setup
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
neoslider = Seesaw(i2c, 0x30)
potentiometer = AnalogInput(neoslider, 18)
pixels = neopixel.NeoPixel(neoslider, 14, 4, pixel_order=neopixel.GRB)


def potentiometer_to_color(value):
    """Scale the potentiometer values (0-1023) to the colorwheel values (0-255)."""
    return value / 1023 * 255


while True:
    print(potentiometer.value)
    # Fill the pixels a color based on the position of the potentiometer.
    pixels.fill(colorwheel(potentiometer_to_color(potentiometer.value)))

