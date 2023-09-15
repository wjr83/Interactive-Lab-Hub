import board
import busio
import adafruit_apds9960.apds9960
import time
import board
from adafruit_apds9960.apds9960 import APDS9960

i2c = busio.I2C(board.SCL, board.SDA)
apds = APDS9960(i2c)

apds.enable_gesture = True
apds.enable_proximity = True

while True:
    gesture = apds.gesture()
    if gesture == 0x01:
        print('up')
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print('right')
    time.sleep(0.2)
