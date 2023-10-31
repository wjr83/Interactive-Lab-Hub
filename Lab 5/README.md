# Observant Systems

**NAMES OF COLLABORATORS HERE**


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

## Prep

1.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/-/Lab%202/prep.md#using-vnc-to-see-your-pi-desktop).
2.  Install the dependencies as described in the [prep document](prep.md). 
3.  Read about [OpenCV](https://opencv.org/about/),[Pytorch](https://pytorch.org/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:
1. Pull the new Github Repo
1. Raspberry Pi
1. Webcam 

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### Pytorch for object recognition

For this first demo, you will be using PyTorch and running a MobileNet v2 classification model in real time (30 fps+) on the CPU. We will be following steps adapted from [this tutorial](https://pytorch.org/tutorials/intermediate/realtime_rpi.html).

![torch](Readme_files/pyt.gif)


To get started, install dependencies into a virtual environment for this exercise as described in [prep.md](prep.md).

Make sure your webcam is connected.

You can check the installation by running:

```
python -c "import torch; print(torch.__version__)"
```

If everything is ok, you should be able to start doing object recognition. For this default example, we use [MobileNet_v2](https://arxiv.org/abs/1801.04381). This model is able to perform object recognition for 1000 object classes (check [classes.json](classes.json) to see which ones.

Start detection by running  

```
python infer.py
```

The first 2 inferences will be slower. Now, you can try placing several objects in front of the camera.

Read the `infer.py` script, and get familiar with the code. You can change the video resolution and frames per second (fps). You can also easily use the weights of other pre-trained models. You can see examples of other models [here](https://pytorch.org/tutorials/intermediate/realtime_rpi.html#model-choices). 


### Machine Vision With Other Tools
The following sections describe tools ([MediaPipe](#mediapipe) and [Teachable Machines](#teachable-machines)).

#### MediaPipe

A recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Media pipe](Readme_files/mp.gif)

To get started, install dependencies into a virtual environment for this exercise as described in [prep.md](prep.md):

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(venv-ml) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(venv-ml) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py`. 

Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) is very useful for prototyping with the capabilities of machine learning. We are using [a python package](https://github.com/MeqdadDev/teachable-machine-lite) with tensorflow lite to simplify the deployment process.

![Tachable Machines Pi](Readme_files/tml_pi.gif)

To get started, install dependencies into a virtual environment for this exercise as described in [prep.md](prep.md):

After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)


```
(venv-tml) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tml_example.py
```


Next train your own model. Visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. The raspberry pi 4 is capable to run not just the low resource models. Second, use the webcam on your computer to train a model. *Note: It might be advisable to use the pi webcam in a similar setting you want to deploy it to improve performance.*  For each class try to have over 150 samples, and consider adding a background or default class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate. Finally export your model as a 'Tensorflow lite' model. You will find an '.tflite' file and a 'labels.txt' file. Upload these to your pi (through one of the many ways such as [scp](https://www.raspberrypi.com/documentation/computers/remote-access.html#using-secure-copy), sftp, [vnc](https://help.realvnc.com/hc/en-us/articles/360002249917-VNC-Connect-and-Raspberry-Pi#transferring-files-to-and-from-your-raspberry-pi-0-6), or a connected visual studio code remote explorer).
![Teachable Machines Browser](Readme_files/tml_browser.gif)
![Tensorflow Lite Download](Readme_files/tml_download-model.png)

Include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.
Model #1: Using self-made dataset from objects found in my apartment.
![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/2eb054b0-2e39-4ac9-a730-bb3c57d75006)
![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/26b8b476-2a81-42ee-8e07-f88adb1a5dc8)
![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/1ac64b9b-1920-4bec-8dd2-412905f0ef32)
![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/ed2c09b5-dcb2-4130-9d0f-f91d89112c23)
![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/d934a539-a00b-4f30-a705-47af48ac1cf4)

Model #2: Trained a second model using available databases of recyclable and non-recyclable objects found online at: https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification/
![Screenshot from 2023-10-30 04-06-32](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/1e484efe-5ac3-4e49-85d8-e3bc5f01fb35)
![Screenshot from 2023-10-30 04-06-15](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/f1f32453-a83f-4255-94c0-c42e44185d68)


#### (Optional) Legacy audio and computer vision observation approaches
In an earlier version of this class students experimented with observing through audio cues. Find the material here:
[Audio_optional/audio.md](Audio_optional/audio.md). 
Teachable machines provides an audio classifier too. If you want to use audio classification this is our suggested method. 

In an earlier version of this class students experimented with foundational computer vision techniques such as face and flow detection. Techniques like these can be sufficient, more performant, and allow non discrete classification. Find the material here:
[CV_optional/cv.md](CV_optional/cv.md).

### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.


**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***
> * I chose to use the Teachable Machines model. Ideas brainstormed for interaction:
> * 1. ASL (American Sign Language) gesture classification to allow deaf or hard-of-hearing individuals to use ASL with individuals who are not proficient in ASL. Interaction would be first prototyped to work on systems such as Zoom or Google Meet (i.e., video calls).
>   2. Alert users when a parking spot opens on his/her street. Rationale: street parking in Manhattan is in extremely high demand. The alert could help a user find street parking closer to his/her apartment.
>   3. System to Recognize Recyclable Objects. 

I chose to implement idea #3: System to Recognize Recyclable Objects

Implementing a system to recognize recyclable objects from non-recyclable objects is motivated by several factors:
> * Environmental Conservation: Effective waste separation and recycling play a crucial role in reducing the environmental impact of waste disposal. It helps conserve resources, reduce energy consumption, and lower greenhouse gas emissions.
> * Waste Reduction: Proper recycling minimizes the volume of waste sent to landfills or incinerators, leading to a reduction in the need for landfill space and decreased pollution from incineration.
> * Consumer Education: Confusion among individuals about the correct sorting of waste is a common issue. This system can serve as an educational tool, clarifying recycling guidelines and encouraging responsible disposal practices.
> * Convenience: Many consumers find it challenging to decipher complex instructions or symbols on bins. A machine learning solution simplifies the process by instantly classifying waste items through images, making it more user-friendly.

> Description of the System:
> > The proposed system integrates a camera into trash and recycling bins, providing guidance on which bin to use before disposal. Here's how it will look, feel, and operate:

> User Interface:
> > A camera is integrated into the trashcan and recycling bin system, making it a seamless part of the waste disposal process in various settings, including businesses, cafes, and outdoor spaces.
Users approach the integrated camera system with their waste items and receive real-time guidance on which bin their waste item belongs to before disposal.


### Part C
### Test the interaction prototype

Sample Tests Screenshots of System that Recognizes Recyclable Objects (Model #2) in action:
![IMG_4062](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/9032bc7f-e3c9-4f62-bbaa-6cf6d8a511fc)
![IMG_4061](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/bb37b888-9d66-418e-99b0-6472d74871bb)
![IMG_4060](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/6a3b12bc-2208-4383-a02a-3eb88539eb1c)
![IMG_4059](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/eb50df40-0e3d-49b4-a0f2-85bd4bd84990)

Sample Video Interaction / Test:

https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/23aa7962-0dc6-44b8-b884-e2ae458af5d6



Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it do what it is supposed to do?
> * The system accurately identifies waste items. The next step in the design of this system would be to guide the user to the correct disposal bin, streamlining the waste sorting process. Thus, users receive clear guidance on which bin to use before disposing of their waste.
2. When does it fail?
> * In cases of poor lighting or obstructed views, making it challenging for the camera to capture clear images of the waste items.
> * When tested on some objects it hasn't seen or different sides of objects it has seen but was not tested on.
> * It also struggles when identifying items with similar appearances that belong in different bins, such as clear plastics and glass, which look alike.
> * In situations where users deposit waste items very quickly, the system may occasionally struggle to keep up, leading to slight delays in providing guidance.
3. When it fails, why does it fail?
> * Poor lighting conditions can affect image quality, leading to misclassifications or a failure to identify the waste item correctly.
> * Obstructed views or partially obscured items may make it difficult for the camera to capture and classify the waste.
> * Similar-looking items may pose a challenge because the system may not have fine-grained classification capabilities to distinguish between them or not enough training data to yield a robust trash vs. recyclables classification model.
> * Rapid user turnover can overwhelm the system's processing capacity, causing it to miss some waste items or provide guidance after the item has been deposited.
4. Based on the behavior you have seen, what other scenarios could cause problems?
> * Language barriers: If the system relies on verbal or text-based instructions to guide users, individuals who do not understand the language used might face difficulties.
> * Age and accessibility issues: Users with visual or hearing impairments might face challenges if the system relies heavily on visual or audio cues without considering accessibility features.
> * Rapid user turnover: In busy public spaces, multiple users deposit waste items in quick succession. The system should be capable of handling high user volumes efficiently without causing bottlenecks or errors.
> * Maintenance issues: The camera and machine learning model require regular maintenance to ensure proper functioning. Neglecting maintenance can lead to performance issues over time.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
> * Users may not always be fully aware of the uncertainties in the system. They might assume that the system's classifications are always accurate, especially if it doesn't provide clear feedback about its confidence level. 
2. How bad would they be impacted by a miss classification?
> * The impact of a misclassification on users can vary. In some cases, misclassifying an item as recyclable when it's not could lead to contamination of recycling streams and added processing costs. Misclassifying an item as non-recyclable when it's recyclable might lead to missed recycling opportunities. For compostable materials, misclassification could affect organic waste diversion rates.
3. How could change your interactive system to address this?
> * To address these concerns, the interactive system could:
> > * Implement a confidence level indicator: The system could provide a confidence score along with its classification. This way, users are aware of how certain or uncertain the system is about its decision.
> > * Offer clear instructions: If an item is challenging to classify, the system could provide guidance to the user, such as suggesting a specific bin but indicating that the user should double-check.
> > * Collect user feedback: Allow users to report misclassifications or provide feedback, which can be used to improve the system's accuracy over time.
4. Are there optimizations you can try to do on your sense-making algorithm.
> * Continuous learning: Implement a self-learning algorithm that can adapt to new objects and user behaviors over time.
> * Real-time model updates: Ensure that the machine learning model is regularly updated with new data to stay current with evolving waste items.
> * Transfer Learning: Utilize transfer learning techniques where the model is initially trained on a broad dataset of waste items and then fine-tuned with specific data from the local environment. This can help the system adapt to local variations in waste categorization.
> * Semantic Segmentation: Employ more advanced computer vision techniques like semantic segmentation to precisely identify regions within an image that correspond to different waste materials. This level of granularity can improve classification accuracy.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***



### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
