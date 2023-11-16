# Little Interactions Everywhere

**NAMES OF COLLABORATORS HERE**: [Khushi Bhansali](https://github.com/Khushibhansali/Interactive-Lab-Hub/edit/Fall2023/Lab%206)

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop. If you are using Mac, MQTT Explorer only works when installed from the [App Store](https://apps.apple.com/app/apple-store/id1455214828).
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.


<img width="1026" alt="Screen Shot 2022-10-30 at 10 40 32 AM" src="https://user-images.githubusercontent.com/24699361/198885090-356f4af0-4706-4fb1-870f-41c15e030aba.png">



### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment:

  ```
  pi@raspberrypi:~/Interactive-Lab-Hub $ source circuitpython/bin/activate
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub $ cd Lab\ 6
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ...
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.

  ```
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/AlexandraTesting
  now writing to topic IDD/AlexandraTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics. Type a message inside MQTT explorer and see if you can receive it with `reader.py`.

  ```
  (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

<img width="890" alt="Screen Shot 2022-10-30 at 10 47 52 AM" src="https://user-images.githubusercontent.com/24699361/198885135-a1d38d17-a78f-4bb2-91c7-17d014c3a0bd.png">


**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

Home Automation System:

- Use Raspberry Pi as a central hub for home automation.
- Connect various sensors (e.g., motion sensors, temperature sensors, door/window sensors) to the Raspberry Pi.
- Use MQTT to publish sensor data to specific topics.
- Implement subscriber devices (smartphones, tablets, or other Raspberry Pis) to receive and act upon the sensor data, triggering home automation actions like turning lights on/off, adjusting thermostat settings, etc.


Smart Garden Monitoring:

- Connect sensors to Raspberry Pi to monitor soil moisture, temperature, and sunlight levels in a garden.
- Use MQTT to publish real-time data to specific topics.
- Subscribers (e.g., a mobile app or a web interface) can receive updates and provide insights about the garden conditions.
- Implement automated watering systems or send alerts to users when the garden needs attention.


Interactive Display for Events:

- Set up Raspberry Pi-powered interactive displays at events or exhibitions.
- Use MQTT to push real-time updates, such as schedule changes, announcements, or interactive polls.
- Attendees can interact with the displays using their smartphones, with the Raspberry Pi serving as a central communication point.


Security System with Camera Integration:

- Build a home security system using Raspberry Pi with a camera module.
- Use motion detection to trigger capturing images or video clips.
- Publish security alerts and captured images/videos to MQTT topics.
- Subscribers (e.g., a security monitoring app) can receive instant notifications and access the captured media.


Weather Station:

- Create a weather station using Raspberry Pi with sensors for temperature, humidity, and barometric pressure.
- Use MQTT to publish weather data to specific topics at regular intervals.
- Users can subscribe to receive weather updates on their devices, or you can integrate the data into a web dashboard.
- Additional features such as historical data storage or weather trend analysis could also be implemented.




Several games could also be implemented, such as the ones listed below:

Quiz Game:

- Create a multiplayer quiz game where each Raspberry Pi acts as a player's buzzer.
- Use MQTT to transmit quiz questions to all players simultaneously.
- Players can press a button on their Raspberry Pi to submit their answers.
- The central Raspberry Pi receives the answers, scores them, and displays the results.


Multiplayer Arcade Game:

- Develop a simple multiplayer arcade game (e.g., a racing game or a space shooter).
- Each Raspberry Pi serves as a game controller with buttons or sensors.
- Use MQTT to synchronize game events and player actions across all devices.
- Display the game screen on a central display connected to another Raspberry Pi.


Escape Room Puzzle:

- Design an escape room-style game where each Raspberry Pi represents a different puzzle or challenge.
- Use MQTT to send and receive messages related to solving puzzles.
- Players must collaborate, solving puzzles on different Raspberry Pis to progress through the "escape room."


Real-Time Strategy (RTS) Game:

- Implement a simple RTS game where each Raspberry Pi represents a player's base or unit.
- Use MQTT to transmit game state, commands, and updates between the Raspberry Pis.
- Players can control their units and engage in real-time battles or strategic moves.


Collaborative Drawing Game:

- Create a collaborative drawing game where each Raspberry Pi contributes to a shared canvas.
- Use MQTT to transmit drawing commands (lines, colors) between devices.
- Players can use buttons or sensors to control their drawing tools.
- The collaborative canvas is displayed on a central screen.

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. 

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***
![IMG_4135](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/854d3916-096d-4862-b3e7-c8f2f7e53baf)

![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/4de7847d-b60d-46b6-ad69-f754a523950d)

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***
The LED Button was integrated in a similar fashion to indicate whether or not the button was pressed on the MQTT 

![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/04821297-7c0a-42f1-854e-28632fff1f48)


### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our hearts, minds, and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to activate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ systemctl stop mini-screen.service
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

**\*\*\*Can you set up the script that can read the color anyone else publishes and display it on your screen?\*\*\***


### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote-controlled banana piano, explain why anyone would want such a thing.

Design Explanation: Encrypted Messaging System with Raspberry Pi and MQTT

Our goal in creating this encrypted messaging system was to establish a secure and private means of communication between my partner and me. The design incorporated several components, utilizing MQTT for efficient message transfer and a Raspberry Pi for decryption and message display. Here's an in-depth explanation of the design:

Sender Module (Partner's Side):

> - The sender module, operated by my partner, was responsible for composing messages on a computer or mobile device.
> - A script encrypted these messages using a secure algorithm, ensuring the confidentiality of the communication.
> - The encrypted messages were then published to specific MQTT topics on a broker.


Receiver Module (My Side - Raspberry Pi):

> - On my side, a Raspberry Pi served as the receiver module.
> - The Raspberry Pi subscribed to the MQTT topics where the encrypted messages were published by my partner.
> - An MQTT client script on the Raspberry Pi constantly monitored these topics for new messages.
> > - Decryption and Notification:

> > > - Upon receiving an encrypted message, the Raspberry Pi ran a decryption script.
> > > - The decryption script utilized a secure key or algorithm, transforming the encrypted message into its original, readable form.
> > > - To notify me of a new message, an LED button on the Raspberry Pi was programmed to light up for a short duration (e.g., 3 seconds), creating a visual indicator.

> > - Message Display:
> > > - Simultaneously, the Raspberry Pi displayed the decrypted message on an OLED screen connected to it.
> > > - The OLED screen provided a convenient and discrete way to read the messages without requiring an external display.


**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

Sender (Your Raspberry Pi)

>   | --- [Type message on Raspberry Pi's Terminal] ---> [ Encryption] ---> [ MQTT Publish ] ---> MQTT Broker (farlab.infosci.cornell.edu)

                                                                              
**Decrypter (Partner's Raspberry Pi) **

>   |--- [ MQTT Subscribe ] ---> [ Decryption ] ---> [LED Button Turns On for 3 Seconds] ---> [OLED Screen Displays Decrypted Message]
  
  
- Sender (Your Raspberry Pi): Responsible for writing and encrypting messages and publishing them to the MQTT broker.
- MQTT Broker (farlab.infosci.cornell.edu): Acts as an intermediary for message communication between the sender Raspberry Pi (encryptor) and the receiving Raspberry Pi  (decrypter).
- Decrypter (Partner's Raspberry Pi): Subscribes to the MQTT broker to receive encrypted messages, decrypts them, notifies the user a new message has been received by flashing the LED on the LED Button and displays the original messages on the OLED screen.
- LED Button: Flashes for 3 seconds every time a new message is received.
- OLED Screen: Displays the decrypted messages.


**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

For the user interface, the system acts as a secure notification system. As the sender, I interact with my Raspberry Pi to input messages. The OLED screen on my partner's Raspberry Pi serves as the output, displaying decrypted messages in a secure manner. Users interacting with the system in the wild would only see the OLED screen, which acts as a discreet notification display, preserving the confidentiality of the messages that pass through the MQTT broker (available to everyone). The interaction is minimal, emphasizing the discreet nature of the encrypted messaging system.

Sender's Raspberry Pi:

> - The sender interacts with their Raspberry Pi to input messages. This interaction can occur through a simple command-line interface or a more sophisticated graphical user interface (GUI) depending on the design.
> - The sender's Raspberry Pi handles the encryption process and publishes the encrypted messages to the designated MQTT topics.

Receiver's Raspberry Pi:

> - Users encountering the system in the wild would primarily interact with the OLED screen on the receiver's Raspberry Pi. The OLED screen acts as a discreet notification display.
> - There's minimal user interaction required on the receiver's side. The system is designed to automatically decrypt incoming messages and display them on the OLED screen without additional input from the user.

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing a response in another location.
Link to Video: [Secure Messanger](https://drive.google.com/file/d/133k2zyBwb7Y0QzSkS0HCe5Ngb2HYswb_/view?usp=sharing)

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

