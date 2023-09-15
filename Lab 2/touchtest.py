import time
import board
import busio
import adafruit_mpr121
import smbus
bus = smbus.SMBus(1)
for address in range(0x08, 0x78):
    try:
        # Try to read a byte from the current address
        bus.read_byte(address)
        print(f"Device found at address: 0x{hex(address)}")
    except:
        pass
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c,0x5a)

while True:
    # Loop through all 12 inputs (0-11).
    for i in range(12):
        # Call is_touched and pass it then number of the input.  If it's touched
        # it will return True, otherwise it will return False.
        if mpr121[i].value:
            print("Input {} touched!".format(i))
    time.sleep(0.25)  # Small delay to keep from spamming output messages.
