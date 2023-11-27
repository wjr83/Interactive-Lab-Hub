import qwiic_button
import time
my_button1 = qwiic_button.QwiicButton(0x6f)
my_button1.LED_on(0)
my_button2 = qwiic_button.QwiicButton(0x6e)
my_button2.LED_on(0)
my_button3 = qwiic_button.QwiicButton(0x6d)
my_button3.LED_on(0)

for i in range(255):
    time.sleep(0.1)
    if i % 5:
        my_button1.LED_on(0)
    else:
        my_button1.LED_on(i)
    if i % 3:
        my_button2.LED_on(0)
    else:
        my_button2.LED_on(i)
    if i % 7:
        my_button3.LED_on(0)
    else:
        my_button3.LED_on(i)


my_button1.LED_on(0)
my_button2.LED_on(0)
my_button3.LED_on(0)
    