# Interactive Prototyping: The Clock of Pi
**NAMES OF COLLABORATORS HERE**

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

Lab Prep is extra long this week. Make sure to start this early for lab on Thursday.

1. ### Set up your Lab 2 Github

Before the start of lab Thursday, [pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub.


  If you are organizing your Lab Hub through folder in local machine, go to terminal, cd into your Interactive-Lab-Hub folder and run:

  ```
  Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
  Interactive-Lab-Hub $ git pull upstream Fall2023
  ```
  
  The reason why we are adding a upstream with **course lab-hub** instead of yours is because the local Interactive-Lab-Hub folder is linked with your own git repo already. Try typing ``git remote -v`` and you should see there is the origin branch with your own git repo. We here add the upstream to get latest updates from the teaching team by pulling the **course lab-hub** to your local machine. After your local folder got the latest updates, push them to your remote git repo by running:
  
  ```
  Interactive-Lab-Hub $ git add .
  Interactive-Lab-Hub $ git commit -m "message"
  Interactive-Lab-Hub $ git push
  ```
  Your local and remote should now be up to date with the most recent files.

The new GitHub.com UI makes this step easy from the webbrowser:
![image](https://github.com/FAR-Lab/Interactive-Lab-Hub/assets/90477986/91d0fbc8-2eba-401f-a5a7-66640910cb62)


2. ### Get Kit and Inventory Parts
Prior to the lab session on Thursday, taken inventory of the kit parts that you have, and note anything that is missing:

***Update your [parts list inventory](partslist.md)***

3. ### Prepare your Pi for lab this week
[Follow these instructions](prep.md) to download and burn the image for your Raspberry Pi before lab Thursday.




## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the \*\*\***stars**\*\*\*. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
### Connect to your Pi
Just like you did in the lab prep, ssh on to your pi. Once you get there, create a Python environment (named venv) by typing the following commands.

```
ssh pi@<your Pi's IP address>
...
pi@raspberrypi:~ $ python -m venv venv
pi@raspberrypi:~ $ source venv/bin/activate
(venv) pi@raspberrypi:~ $ 

```
### Setup Personal Access Tokens on GitHub
Set your git name and email so that commits appear under your name.
```
git config --global user.name "Your Name"
git config --global user.email "yourNetID@cornell.edu"
```

The support for password authentication of GitHub was removed on August 13, 2021. That is, in order to link and sync your own lab-hub repo with your Pi, you will have to set up a "Personal Access Tokens" to act as the password for your GitHub account on your Pi when using git command, such as `git clone` and `git push`.

Following the steps listed [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) from GitHub to set up a token. Depends on your preference, you can set up and select the scopes, or permissions, you would like to grant the token. This token will act as your GitHub password later when you use the terminal on your Pi to sync files with your lab-hub repo.


## Part B. 
### Try out the Command Line Clock
Clone your own lab-hub repo for this assignment to your Pi and change the directory to Lab 2 folder (remember to replace the following command line with your own GitHub ID):

```
(venv) pi@raspberrypi:~$ git clone https://github.com/<YOURGITID>/Interactive-Lab-Hub.git
(venv) pi@raspberrypi:~$ cd Interactive-Lab-Hub/Lab\ 2/
```
Depends on the setting, you might be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you just set up as the password instead of your account one!


Install the packages from the requirements.txt and run the example script `cli_clock.py`:

```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ pip install -r requirements.txt
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
02/24/2021 11:20:49
```

The terminal should show the time, you can press `ctrl-c` to exit the script.
If you are unfamiliar with the Python code in `cli_clock.py`, have a look at [this Python refresher](https://hackernoon.com/intermediate-python-refresher-tutorial-project-ideas-and-tips-i28s320p). If you are still concerned, please reach out to the teaching staff!


## Part C. 
### Set up your RGB Display
We have asked you to equip the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) on your Pi in the Lab 2 prep already. Here, we will introduce you to the MiniPiTFT and Python scripts on the Pi with more details.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware (you have already done this in the prep)

From your kit take out the display and the [Raspberry Pi 4](https://cdn-shop.adafruit.com/970x728/3775-07.jpg)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Testing your Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. We won't go in depth in this course over how SPI works. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol which we will cover later. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

To show you the IP and Mac address of the Pi to allow connecting remotely we created a service that launches a python script that runs on boot. For the following steps stop the service by typing ``` sudo systemctl stop mini-screen.service```. Othwerise two scripts will try to use the screen at once. 

We can test it by typing 
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ python screen_test.py
```

You can type the name of a color then press either of the buttons on the MiniPiTFT to see what happens on the display! You can press `ctrl-c` to exit the script. Take a look at the code with
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ cat screen_test.py
```

#### Displaying Info with Texts
You can look in `screen_boot_script.py` and `stats.py` for how to display text on the screen!

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?



## Part D. 
### Set up the Display Clock Demo
Work on `screen_clock.py`, try to show the time by filling in the while loop (at the bottom of the script where we noted "TODO" for you). You can use the code in `cli_clock.py` and `stats.py` to figure this out.

### How to Edit Scripts on Pi
Option 1. One of the ways for you to edit scripts on Pi through terminal is using [`nano`](https://linuxize.com/post/how-to-use-nano-text-editor/) command. You can go into the `screen_clock.py` by typing the follow command line:
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
```
You can make changes to the script this way, remember to save the changes by pressing `ctrl-o` and press enter again. You can press `ctrl-x` to exit the nano mode. There are more options listed down in the terminal you can use in nano.

Option 2. Another way for you to edit scripts is to use VNC on your laptop to remotely connect your Pi. Try to open the files directly like what you will do with your laptop and edit them. Since the default OS we have for you does not come up a python programmer, you will have to install one yourself otherwise you will have to edit the codes with text editor. [Thonny IDE](https://thonny.org/) is a good option for you to install, try run the following command lines in your Pi's ternimal:

  ```
  pi@raspberrypi:~ $ sudo apt install thonny
  pi@raspberrypi:~ $ sudo apt update && sudo apt upgrade -y
  ```

Now you should be able to edit python scripts with Thonny on your Pi.

Option 3. A nowadays often preferred method is to use Microsoft [VS code to remote connect to the Pi](https://www.raspberrypi.com/news/coding-on-raspberry-pi-remotely-with-visual-studio-code/). This gives you access to a fullly equipped and responsive code editor with terminal and file browser.  

Pro Tip: Using tools like [code-server](https://coder.com/docs/code-server/latest) you can even setup a VS Code coding environment hosted on your raspberry pi and code through a web browser on your tablet or smartphone! 

## Part E.
### Modify the barebones clock to make it your own
> **Note: All of Part E was developed in the python script named `escreen_clock.py`.**

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)
* We are measuring time with flowers! More specifically, by counting the petals of flowers!
Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.
* Will attempt to make use of the screen's buttons for Part 2 of the Lab.
Please sketch/diagram your clock idea. (Try using a [Verplank digram](http://www.billverplank.com/IxDSketchBook.pdf)!
![IMG_3564](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/95e1c5b4-8717-4a63-a831-13deba834306)

I decided to implement Idea "D" shown above as it seemed the most artistic and intuitive representation of time using mathematical functions (cosine and sine functions plotted in polar coordinates).
The first attempts at implementing Idea D are shown below:
![IMG_3542](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/eca07f64-f529-4c55-b7fe-3ec9c9007979)
![IMG_3535](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/0b74bdd1-fe0a-4afa-91cc-e6d62b54759f)
![IMG_3534](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/0a70de14-952f-4577-b289-12d5b5997bd1)


https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/cb120392-d470-42f9-9694-f596b5641df9


https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/1223c9c8-5dc2-4ea9-857f-930fc33645d0

After trying to tweak the parameters over and over so that the overlay is not overly cluttered in the tiny screen on the Raspberry Pi, I decided to separate the hour, minutes, and seconds "flowers" into their own "flower pot" (or formally, polar plot) for improved reading of the time. A sample output is shown below (where the time displayed HH:MM:SS is 01:22:18 PM, as indicated by the number of petals in each flower):
![time_output](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/bd0782f5-cadb-42d3-8cda-0f6e975c61ac)

After some more work, these were the results:



https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/d1677c33-f145-4659-abd8-c0afa33757e0



https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/a9bbab2c-85d4-424e-a02d-78bb44064924



https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/9a10dcdd-c79f-4d91-a2ec-b557041413d2




**We strongly discourage and will reject the results of literal digital or analog clock display.**


\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

After you edit and work on the scripts for Lab 2, the files should be upload back to your own GitHub repo! You can push to your personal github repo by adding the files here, commiting and pushing.

```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git add .
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'your commit message here'
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git push
```

After that, Git will ask you to login to your GitHub account to push the updates online, you will be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you set up in Part A as the password instead of your account one! Go on your GitHub repo with your laptop, you should be able to see the updated files from your Pi!


## Part F. 
## Make a short video of your modified barebones PiClock

\*\*\***Take a video of your PiClock.**\*\*\*

After investing time in making my code more efficient so as to make the transition of time smoother, this was the result:

https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/4e181d51-a537-44ab-b4a9-029ce1d61044



## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.
* Buttons:
> - Zoom in on each plot (hour, minutes, seconds) with each click
> - Switch display to showcase whether it is night or day
> - Switch display to showcase month, day, year
>   - Display the zodiac constellation to indicate the current month
>   - Display images representing important events in history for today's date (e.g., Independence Day, Christmas, New Year's Eve, birthdays of family and friends).
* Design the clock as a timer/reminder to take a break from studying (e.g., every 50min for 10 minutes).
* Design the screen as a countdown that tracks the metro lines Q & F in NYC at specific locations (Roosevelt Island and Midtown).
* - The countdown can be the logo of the line moving across the screen (or the logo fading away, or a train moving across the screen and coming to a stop when at the station).
<img width="30" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/3c5bbbca-9c4a-46d3-b539-b896aa854457">
<img width="30" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/d56295c9-8ce4-4466-bd37-a9a2dd8c43b9">
<img width="30" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/e21c8f59-1e7d-47ba-8655-2bc6a201f90f">
<img width="30" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/474fe5ff-95b2-47b5-9924-460b1baab9eb">
<img width="40" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/192f4f2d-74f5-4f99-be71-1e45b74503c2">
<img width="40" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/fd4a28da-816c-48ff-8283-cc7c82014339">
<img width="80" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/701bcabe-eb64-4838-a599-aa991322e4a1">

* Display a timer to cook different meats to perfection.




# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

Feedback received:
- I found the geometrical aesthetic quite captivating
- Nice contrast in colors and curves
- The labels seem to distract a bit from this
- I would try to find a way to fullscreen the visuals and discard the text and white space
- The aesthetics are really awesome, thinking about ways to maximize there appearance
- Maybe divide the 3 units of time across 3 different screens, integrating a button to push between them
- Overall I think you're on to something great with this, just need to try and remove the text distractors
- Add dynamic art component (similar to abstract screensaver, but this time the art itself should tell time).
- How important are the hours and minutes polar displays of time? Maybe these can be smaller compared to the seconds display as they change less frequently.
- - Maybe stack the hours and minutes vertically and center the seconds polar display on the screen.

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn-in; you are expected to make equal contributions on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn-in is linked to your Interactive Lab Hub page. 

## Per feedback received in class, I removed the axis of the polar plots to just display flowers (cosines and sines plotted in polar coordinates) with changing petals to denote hours, minutes, and seconds.
![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/b9b1864f-2092-46c8-b8ff-f806594da82c)


## Brainstorming Additional Ideas 
Certainly! Time can be harnessed creatively for a wide range of applications. Here are some creative ideas:

1. **Time Capsule Messages**: Create a digital platform where people can send messages, photos, or videos to their future selves or loved ones. These messages can be scheduled to be delivered on a specific date, such as a birthday, anniversary, or even many years into the future.

2. **Time-Limited Art Gallery**: Host an online art gallery that displays artworks for a limited time, creating a sense of urgency and exclusivity. Users can bid on or purchase the artworks during the exhibition, and once the timer runs out, the gallery closes, and the art is no longer available.

3. **Time-Based Charity Challenges**: Launch a platform where users can commit to donating a certain amount of money to a chosen charity if they fail to complete a specific challenge within a given timeframe. This could be anything from running a marathon to quitting a bad habit.

4. **Time-Activated Escape Room**: Design an escape room game where players solve puzzles and follow clues, but with a twist - they have a limited amount of real-time to complete it. The game can only be played at specific times and only lasts for a set duration.

5. **Time-Triggered Augmented Reality Stories**: Develop an AR app that allows users to experience stories or historical events at specific real-world locations. For example, users can visit a historical site, and the app uses GPS and time triggers to overlay historical scenes and characters onto the location.

6. **Time-Managed Music Streaming**: Create a music streaming service that curates playlists based on the time of day or season. Users can select playlists optimized for sunrise, sunset, rainy days, or even specific historical eras.

7. **Time-Dependent Recipe Recommendations**: Build a cooking app that suggests recipes based on the time available and the ingredients on hand. Users can input how much time they have, and the app provides suitable recipes with step-by-step instructions.

8. **Time-Driven Meditation Guides**: Develop a meditation app that guides users through different meditation techniques based on the time of day and their personal preferences. Morning meditations could focus on energizing, while evening meditations could be geared toward relaxation.

9. **Time-Stamped Travel Journals**: Create a travel app that automatically generates a digital journal of a user's journey, complete with photos, notes, and GPS data, timestamped at each location visited. Users can revisit their trips virtually and see their experiences unfold over time.

10. **Time-Encoded Educational Challenges**: Gamify learning by offering challenges and quizzes that are only accessible at specific times. For instance, users could unlock new lessons or challenges daily, encouraging consistent engagement.

11. **Time-Controlled Greenhouses**: Develop a smart greenhouse system that adjusts lighting, temperature, and humidity based on real-time and historical weather data, optimizing plant growth and minimizing resource usage.

12. **Time-Triggered Photography Challenges**: Develop a photography app that presents users with daily or weekly photo challenges, such as "golden hour landscapes" or "motion blur." Users have a limited time to capture and upload their photos, fostering creativity and community engagement.

13. **Time-Managed Fitness Classes**: Offer virtual fitness classes that adapt in real-time to the user's energy level. Users input their current mood and energy, and the class intensity and style adjust accordingly.

14. **Time-Stamped Event Planning**: Develop an event planning app that helps users coordinate schedules and logistics for gatherings. It includes a countdown timer, real-time updates, and reminders for tasks leading up to the event.

15. **Time-Dependent Gardening Assistance**: Create a gardening app that provides users with timely reminders and advice on when to plant, water, and harvest their crops based on their location and the current season.

16. **Time-Limited Learning Challenges**: Design a platform where users can compete in time-limited learning challenges. Participants have a set amount of time to study a topic and then take a quiz to earn points or rewards.

17. **Time-Activated Financial Goals**: Build a financial planning app that allows users to set time-based financial goals, like saving for a vacation or retirement. The app provides a visual representation of progress over time and suggests actions to meet those goals.

18. **Time-Driven Energy Conservation**: Create a smart home system that adjusts lighting, heating, and cooling based on the time of day, occupancy patterns, and weather forecasts to optimize energy efficiency.

19. **Time-Bound Virtual Book Club**: Organize a virtual book club where participants read a book together over a fixed duration. Weekly discussions and live author Q&A sessions make the experience immersive and time-bound.

20. **Time-Managed Productivity Tools**: Create a productivity app that helps users allocate their time effectively. It combines task management with time-blocking techniques, helping users plan their day and track their progress.

21. **Time-Driven Language Learning**: Build a language-learning app that offers short, time-bound lessons throughout the day. Users receive bite-sized language challenges during their free moments, making learning convenient and effective.

22. **Time-Activated Environmental Sensors**: Deploy environmental sensors that collect data on air quality, noise levels, and temperature over time. Users can access historical data and receive alerts when conditions surpass specified thresholds.

23. **Time-Enhanced Virtual Museums**: Create virtual museums where historical events, artifacts, and exhibits are showcased in chronological order. Users can explore history as it unfolds over time.

## Choose and Idea and Explore it Further

### Idea Chosen: Display a timer to cook different meats to perfection. 

Text-based storyboard shown below for Cooking Timer

Title: Raspberry Pi Cooking Timer Interaction Storyboard

Storyboard Description:
This storyboard outlines the user interaction with a cooking timer application running on a Raspberry Pi. The user wants to set a timer for cooking a specific type of meat on the stove. Current available options: chicken, lamb, fish, shrimp, pork, and steak. This text-based storyboard illustrates the step-by-step interaction of a user with athe cooking timer application on a Raspberry Pi, from setting the timer to acknowledging its completion.  

Scene 1:
[Image: A user standing in a kitchen with a Raspberry Pi and a touchscreen display.]

Narration: "User stands in the kitchen, ready to bake cookies."

1. User taps the Raspberry Pi display to wake it up.
2. Raspberry Pi displays current time at home screen.

Scene 2:
[Image: Close-up of the Raspberry Pi display.]

3. User presses top button to launch the cooking timer app.

Scene 3:
[Image: The Cooking App opens with a Grill Menu screen.]

4. The Cooking Timer app opens.

Scene 4:
[Image: Browse Menu Options]
5. User presses top button to show the first item in the menu.
6. User keeps pressing the top button to show the next item on the menu.

Scene 4:
[Image: The user selects the desired protein to cook.]
7. To select the intended protein to cook, user presses the bottom button.

Narration: "Cooking Timer Starts"

8. User is prompted to start cooking.
9. Timer starts at a predifined number of minutes depending on the protein selected.

Scene 5:
[Image: The Cooking Timer alerts user it's time to flip the protein]

10. When the elapsed time is half of the total time for that protein, the user is prompted to turn the protein on its other side.

Scene 6:
[Image: Cooking Timer Continues until remaining time has elapsed]
11. The timer then continues.

Scene 7:
[Image: Cooking Timer Alerts User Food is done until remaining time has elapsed]
12. User is visually told the food is ready!

