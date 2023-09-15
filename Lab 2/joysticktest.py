import smbus, time
bus = smbus.SMBus(1)

# bus_data, X, Y,BEEN_CLICKED
    
BEEN_CLICKED = 0

def qwiicjoystick():
    global BEEN_CLICKED
    bus_data = bus.read_i2c_block_data(0x20, 0x03, 5)
    X = (bus_data[0]<<8 | bus_data[1])>>6
    Y = (bus_data[2]<<8 | bus_data[3])>>6
    BUTTON = bus_data[4]
    
    # if X < 450:
    #     direction = RIGHT
    # elif 575 < X:
    #     direction = LEFT
    # if Y< 450:
    #     direction = DOWN
    # elif 575 < Y:
    #     direction = UP
    if BUTTON == 0:
        BEEN_CLICKED +=1
    # if BUTTON == 0 and BEEN_CLICKED == 1:
    #     BEEN_CLICKED = 0
        
    print(X, Y, " Button = ", BUTTON)
    print(BEEN_CLICKED)
    time.sleep(.05)
    
while True:
    qwiicjoystick()