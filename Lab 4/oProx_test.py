import qwiic_proximity
import time
from time import sleep

oProx = qwiic_proximity.QwiicProximity()
if oProx.begin() == False:
    print("The Qwiic Proximity device isn't connected to the system. Please check your connection", \
        file=sys.stderr)
print("Qwiic Proximity ready!")


while True:
    proxValue = oProx.get_proximity()
    print(proxValue)
    sleep(0.1)