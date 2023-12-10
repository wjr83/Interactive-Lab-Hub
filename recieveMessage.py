from __future__ import print_function
import paho.mqtt.client as mqtt
import uuid
import ssl
import qwiic_button 
import time
import sys
import qwiic_oled_display
import board

my_button = qwiic_button.QwiicButton()
my_button.LED_off()


i2c = board.I2C()
myOLED = qwiic_oled_display.QwiicOledDisplay()

if not myOLED.connected:
    print("The Qwiic OLED Display isn't connected to the system. Please check your connection", \
        file=sys.stderr)
myOLED.begin()
#  clear(ALL) will clear out the OLED's graphic memory.
#  clear(PAGE) will clear the Arduino's display buffer.
myOLED.clear(myOLED.ALL)  #  Clear the display's memory (gets rid of artifacts)
#  To actually draw anything on the display, you must call the
#  display() function.
myOLED.display()
time.sleep(1)

myOLED.clear(myOLED.PAGE)




def disp_message_oled(myOLED, message):
    myOLED.clear(myOLED.PAGE)            # Clear the display
    # print("TEST")
    myOLED.set_cursor(0, 0)           # Set cursor to bottom-left
    myOLED.set_font_type(1)             # Smallest font
    myOLED.print(message)
    myOLED.display()


# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))

# configure network encryption etc
# Configure SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Set the SSL context
client.tls_set_context(ssl_context)

# this is the username and pw we have set up for the class
client.username_pw_set('idd', 'device@theFarm')

# connect to the broker
client.connect('farlab.infosci.cornell.edu', port=8883)

def on_message(client, userdata, msg):
    disp_message_oled(myOLED, msg.payload)
    brightness = 100
    my_button.LED_on(brightness)
    time.sleep(5)

# Set the callback function for message reception
client.on_message = on_message

# Subscribe to a specific topic to receive notifications
subscribe_topic = "IDD/iRecycle"
client.subscribe(subscribe_topic)

# Continue the loop to keep the client running and receiving messages
client.loop_forever()