import qwiic_button
import time
my_button1 = qwiic_button.QwiicButton(0x6f)
my_button1.LED_on(250)
time.sleep(0.5)
my_button2 = qwiic_button.QwiicButton(0x6e)
my_button2.LED_on(150)
time.sleep(0.5)
my_button3 = qwiic_button.QwiicButton(0x6d)
my_button3.LED_on(150)
time.sleep(0.5)
my_button4 = qwiic_button.QwiicButton(0x6b)
my_button4.LED_on(150)
time.sleep(0.5)
my_button5 = qwiic_button.QwiicButton(0x6c)
my_button5.LED_on(150)
time.sleep(0.5)
my_button6 = qwiic_button.QwiicButton(0x67)
my_button6.LED_on(150)
time.sleep(0.5)
my_button7 = qwiic_button.QwiicButton(0x63)
my_button7.LED_on(150)
time.sleep(0.5)
my_button8 = qwiic_button.QwiicButton(0x68)
my_button8.LED_on(150)
time.sleep(0.5)
my_button9 = qwiic_button.QwiicButton(0x69)
my_button9.LED_on(150)
time.sleep(0.5)
my_button10 = qwiic_button.QwiicButton(0x61)
my_button10.LED_on(150)
time.sleep(0.5)


my_button1.LED_on(0)
my_button2.LED_on(0)
my_button3.LED_on(0)
my_button4.LED_on(0)
my_button5.LED_on(0)
my_button6.LED_on(0)
my_button7.LED_on(0)
my_button8.LED_on(0)
my_button9.LED_on(0)
my_button10.LED_on(0)



# for i in range(255):
#     time.sleep(0.1)
#     if i % 5:
#         my_button1.LED_on(0)
#     else:
#         my_button1.LED_on(i)
#     if i % 3:
#         my_button2.LED_on(0)
#     else:
#         my_button2.LED_on(i)
#     if i % 7:
#         my_button3.LED_on(0)
#     else:
#         my_button3.LED_on(i)


my_button1.LED_on(0)
my_button2.LED_on(0)
my_button3.LED_on(0)
    