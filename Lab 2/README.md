# Interactive Prototyping: The Clock of Pi

## Overview

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## Part E.
### Modify the barebones clock to make it your own
> **Note: All of Part E was developed in the python script named `escreen_clock.py`.**

* We are measuring time with flowers! More specifically, by counting the petals of flowers!
Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.
* Will attempt to make use of the screen's buttons for Part 2 of the Lab.


Sketch/diagram of clock idea:
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
Feedback received:
- I found the geometrical aesthetic quite captivating
- Nice contrast in colors and curves
- The labels seem to distract a bit from this
- I would try to find a way to fullscreen the visuals and discard the text and white space
- The aesthetics are really awesome, thinking about ways to maximize their appearance
- Maybe divide the 3 units of time across 3 different screens, integrating a button to push between them
- Overall I think you're on to something great with this, just need to try and remove the text distractors
- Add dynamic art component (similar to abstract screensaver, but this time the art itself should tell time).
- How important are the hours and minutes polar displays of time? Maybe these can be smaller compared to the seconds display as they change less frequently.
- - Maybe stack the hours and minutes vertically and center the seconds' polar display on the screen.

# Lab 2 Part 2

## Per feedback received in class, I removed the axis of the polar plots to just display flowers (cosines and sines plotted in polar coordinates) with changing petals to denote hours, minutes, and seconds.
![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/b9b1864f-2092-46c8-b8ff-f806594da82c)


## Brainstorming Additional Ideas 
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

## Choose an Idea and Explore it Further

### Idea Chosen: Display a timer to cook different meats to perfection. 

A visual representation is shown below for Cooking Timer application:

Title: Raspberry Pi Cooking Timer Interaction Storyboard

Storyboard Description:
This storyboard outlines the user interaction with a cooking timer application running on a Raspberry Pi. The user wants to set a timer for cooking a specific type of meat on the stove. Current available options: chicken, lamb, fish, shrimp, pork, and steak. This text-based storyboard illustrates the step-by-step interaction of a user with the cooking timer application on a Raspberry Pi, from setting the timer to acknowledging its completion.  

Scene 1: A user standing in a kitchen with a Raspberry Pi and a display, hoping to cook a protein to perfection.

1. The user turns on the Raspberry Pi.
2. Raspberry Pi displays the current time on the home screen.

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/4b6bf7c4-4f8d-4d93-9253-846de44c3cb5">

Scene 2: Close-up of the Raspberry Pi display.

3. The user presses the top button to launch the cooking timer app.

<img width="300" alt="image" src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png">

Scene 3: The Cooking App opens with a Grill Menu screen.

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/3d2f22da-2a7b-4e8b-9a3f-0ecce31c8960">

4. The Cooking Timer app opens.

Scene 4:
[Image: Browse Menu Options]

5. The user presses the top button to show the first item in the menu.
6. The user keeps pressing the top button to show the next item on the menu. See all menu options below:

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/fbcd0048-b9e8-446c-a870-09c3adfa9381">
<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/e746b36b-9441-45cf-8e6c-efb393d85431">
<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/eaddb382-8429-4cea-962f-122b02e8f210">
<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/13af15ac-4acb-46f2-80a9-920399e7b45a">
<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/5a1100d0-a39d-4c48-88a0-ce52d198bb62">
<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/baaba2cf-df89-4b13-b8bc-d203e86ff5ee">



Scene 4: The user selects the desired protein to cook.

7. To select the intended protein to cook, the user presses the bottom button.

<img width="300" alt="image" src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png">

8. The user is prompted to start cooking by the following image:

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/545abce5-3326-415f-87d2-80874ee3185b">

9. The timer starts at a predefined number of minutes depending on the protein selected. The cooking duration, along with the cooking temperature, is displayed to the user before the timer starts the countdown. Note that a key difference between the timer (shown below) and the current time clock (as seen in Scene 1) is that the timer's background is black while the background of the current time clock is white.

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/6d4682f0-69e7-4911-979d-db92e2e9ccac">

Cooking Temperature & Time for Menu Items:
  * chicken: ['Medium Heat', 20 minutes]
  * fish: ['Med-High Heat', 10 minutes]
  * lamb: ['High Heat', 15 minutes]
  * pork: ['High Heat', 15 minutes] 
  * shrimp: ['Med-High Heat', 6 minutes]
  * steak' ['High Heat', 13 minutes] 


Sample temperature and cooking time shown to the user:

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/d2a24404-6a29-49e7-a968-5121bb1d4462">

Scene 5: The Cooking Timer alerts the user that it's time to flip the protein (by the following image).

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/7ade8c13-8a4b-4b6a-ad0a-ee1c9661e20a">

10. When the elapsed time is half of the total time for that protein, the user is prompted to turn the protein on its other side.

Scene 6: Cooking Timer Continues until the remaining time has elapsed

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/6d4682f0-69e7-4911-979d-db92e2e9ccac">

Scene 7: Cooking Timer Alerts User Food is done when all the remaining time has elapsed.

11. The user is visually told the food is ready!

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/4adf0d36-dfbd-4902-8c7b-398ad7a768d9">

Scene 8: Display returns to show the current time.

<img width="300" alt="image" src="https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/6de7ec00-7d2b-4101-8b74-f9e1be95c568">

## Videos of final result: PiClock for Cooking Proteins "Just Right"! Never worry about overcooking your steak, or undercooking your poultry and seafood!
**NOTE: You must log in to your Cornell Google Account to gain access to the video links below!**

Full Video: Cooking Shrimp from start to finish (Video Speed: 1x)
> - https://drive.google.com/file/d/1xma0W7vaNPXSR1_7-gBLWx_ZqeJw_rox/view?usp=drive_link

Sample Video: Cooking Pork
> - https://drive.google.com/file/d/14cswX4Cb0FfBULm_j0k7Vz3HeHDN8ijS/view?usp=sharing

Sample Video: Cooking Fish
> - https://drive.google.com/file/d/16IUb6jiWxw2WUO4WFl1NYn1VzMqsCmk5/view?usp=sharing
