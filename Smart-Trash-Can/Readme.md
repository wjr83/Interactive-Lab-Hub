# Final Project: iRecycle

[Project Plan](#project-plan) 

[Functioning Project](#functioning-project) 

[Documentation of Design Process](#documentation-of-design-process) 

[Archive of All Code and Design Patterns](#archive-of-all-code-and-design-patterns) 

[Video Demo](#video-demo) 

[Reflections on Process](#reflections-on-process) 

[Group Work Distribution](#group-work-distribution) 


## Project Plan
Using the tools and techniques learned in this class, design, prototype, and test an interactive device that can distinguish between recyclable objects (paper, cardboard, plastic, glass, metal), trash, and batteries. 

#### COLLABORATOR: [Khushi Bhansali (ID: kb737)](https://github.com/Khushibhansali/Interactive-Lab-Hub/blob/Fall2023/FinalProject.md)

### Big Idea & Motivation for Project
- A system to recognize recyclable objects from non-recyclable objects is motivated by several factors:

> - Environmental Conservation: Effective waste separation and recycling play a crucial role in reducing the environmental impact of waste disposal. It helps conserve resources, reduce energy consumption, and lower greenhouse gas emissions.
> - Waste Reduction: Proper recycling minimizes the volume of waste sent to landfills or incinerators, leading to a reduction in the need for landfill space and decreased pollution from incineration.
> - Consumer Education: Confusion among individuals about the correct sorting of waste is a common issue. This system can serve as an educational tool, clarifying recycling guidelines and encouraging responsible disposal practices.
> - Convenience: Many consumers find it challenging to decipher complex instructions or symbols on bins. A machine learning solution simplifies the process by instantly classifying waste items through images, making it more user-friendly.

#### Intended Operation
- The system identifies an object and classifies it as one of the 5 recycled materials (paper, cardboard, glass, plastic, and metal), compost, special handling materials (e.g., batteries), or otherwise as trash.

> - Primary Goal: Design a system capable of identifying recyclable objects (paper, cardboard, plastic, glass, and metal), compost, items requiring special handling (e.g., batteries), and trash.
> - Secondary Goal: Deployment of the system increases the number of items recycled, and decreases the incidence of non-recyclable objects being mixed with recyclable items in the recycling bin due to misinformation about what items can and cannot be recycled.
> - Tertiary Goal: Educate the general public on what items can be recycled and which ones cannot.

Project plan - November 14
![image](https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/278df58d-139e-486b-bb4d-aecda3a21b7c)

Peer feedback on Project plans: November 21

Functional check-off - November 28 & 30

Final Project Presentations - December 5 & 7

Write-up and documentation due - December 14

### Parts Needed

The Device:

- 1x [Raspberry Pi 4 Model B Board](https://www.amazon.com/dp/B0899VXM8F?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- 1x [32GB MicroSD Cards w/ Card Reader](https://www.amazon.com/SanDisk-SDSQUAR-032G-GN6MA-Samsung-Everything-Stromboli/dp/B0796Y6177/ref=sr_1_3?crid=1GRBD63EDRPAP&keywords=32gb%2Bmicrosd%2Bcards%2Bwith%2F%2Bcard%2Breader&qid=1700809250&s=electronics&sprefix=32gb%2Bmicrosd%2Bcards%2Bw%2F%2Bcard%2Breader%2Celectronics%2C151&sr=1-3&th=1)
- 1x [Adafruit Mini PiTFT - 135x240 Color TFT Add-on for Raspberry Pi](https://www.adafruit.com/product/4393)
- 1x [SparkFun Qwiic LED Stick - APA102C](https://www.sparkfun.com/products/18354)
> - Note: The retired version of the [Qwiic LED Stick](https://www.sparkfun.com/products/retired/14783) is compatible with the Arduino but not the Raspberry Pi (no Python module for Raspberry Pi exists for this version)
- #x [SparkFun Qwiic Button - Red LED](https://www.sparkfun.com/products/15932)
- #x [SparkFun Qwiic Button - Green LED](https://www.sparkfun.com/products/16842)
- 1x [SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://www.sparkfun.com/products/15945)
- 1x [Adafruit 16-Channel PWM / Servo HAT for Raspberry Pi - Mini Kit](https://www.adafruit.com/product/2327)
- #x [SparkFun Proximity Sensor Breakout - 20cm, VCNL4040 (Qwiic)](https://www.sparkfun.com/products/15177)
> - 1x [5V 4A (4000mA) switching power supply - UL Listed](https://www.adafruit.com/product/1466)
- 2x [SparkFun Qwiic Mux Breakout - 8 Channel (TCA9548A)](https://www.sparkfun.com/products/16784)
> - Helpful troubleshooting guide: https://electronics.stackexchange.com/questions/585681/multiple-tca9548a-multiplexers-are-not-working-correctly-with-more-than-3-connec
> > - https://learn.sparkfun.com/tutorials/qwiic-mux-hookup-guide?_ga=2.40512486.592347460.1700772500-269332035.1698912388&_gl=1*1s9uhgb*_ga*MjY5MzMyMDM1LjE2OTg5MTIzODg.*_ga_T369JS7J9N*MTcwMDgwOTM1OS42LjEuMTcwMDgwOTU2NS42MC4wLjA.#p 
- Servo(s)
- Cardboard
- Camera with USB Connection
- #x Qwiic Cables
- Tape
- Glue


### Challenges  & Fall-back Plan
- A single continuous servo vs. multiple 180-degree servos for opening and closing the bins

### Work in Progress
#### Classification Algorithm
Classes trained: paper, cardboard, plastic, glass, metal, trash, background
> Video of 1st Working Model --> Classes trained: paper, cardboard, plastic, glass, metal, trash, background

https://github.com/wjr83/Interactive-Lab-Hub/assets/143034234/1a22da79-34c1-447c-b6e4-dba596737b10



#### Physical Prototype

#### Sensors






## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description
Your project is to design and build an interactive device to suit a specific application of your choosing, and *test the interaction with people*. 

## Deliverables
1. Project plan: Big idea, timeline, parts needed, fall-back plan.
2. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.
3. Documentation of design process
4. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
5. Video of someone using your project
6. Reflections on process (What have you learned or wish you knew at the start?)
7. Group work distribution questionnaire


## Change of Design

It is fine to change your project goals, but please resubmit the project plan for the new design when you do that.

## Grading rubric

20% Project planning: Allocation of needed resources (time, people, materials, facilities) anticipated well.
20% Design of project: Interaction, hardware and software aspects of projects planned well.
20% Testing of project: Functional or wizarded system tested with people
20% Prototype functionality: System capable of interaction, either through autonomous or wizarded mechanisms
20% Project documentation: Text, video, and photo of project illustratign capability and documenting plans and process

## Teams

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
