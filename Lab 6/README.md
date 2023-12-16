# Little Interactions Everywhere

**NAMES OF COLLABORATORS HERE**: [Khushi Bhansali (NetID: kb737)](https://github.com/Khushibhansali/Interactive-Lab-Hub/edit/Fall2023/Lab%206)


## Overview

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.



### Part B

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

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***
![IMG_4135](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/854d3916-096d-4862-b3e7-c8f2f7e53baf)

![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/4de7847d-b60d-46b6-ad69-f754a523950d)

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***
> - The LED Button was integrated in a similar fashion to indicate whether or not the button was pressed on the MQTT Explorer.

![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/04821297-7c0a-42f1-854e-28632fff1f48)


### Part D
### The One True ColorNet

**\*\*\*Can you set up the script that can read the color anyone else publishes and display it on your screen?\*\*\***

Video showing a working version of reading a color anyone else publishes and displaying it on my screen: 

https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/7dd90030-6b9b-4659-a2d6-08def3265134

Printed to the terminal the RGB of the colors received through MQTT Broker messages: 

![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/493fa38d-b5e9-4e35-96eb-bef66981229a)


### Part E
### Make it your own

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
> - Link to Video: [Secure Messenger](https://drive.google.com/file/d/133k2zyBwb7Y0QzSkS0HCe5Ngb2HYswb_/view?usp=sharing)
