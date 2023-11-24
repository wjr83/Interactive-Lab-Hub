from teachable_machine_lite import TeachableMachineLite
import os
from datetime import datetime
import cv2 as cv
import time
from adafruit_servokit import ServoKit
# import qwiic_led_stick
from word_counter import WordCounter # custom class to validate reading from camera



##############################################################################
label_counter = WordCounter()
# my_stick = qwiic_led_stick.QwiicLEDStick()
# my_stick.set_all_LED_brightness(5)

# Dictionary to map classifications to colors
colors_dict = {
    'background': (255, 255, 255),   # White
    'paper': (255, 255, 102),        # Yellow
    'cardboard': (128, 0, 128),      # Purple
    'trash': (255, 165, 0),          # Orange
    'plastic': (255, 0, 255),        # Magenta
    'metal': (0, 255, 255),          # Cyan
    'glass': (0, 128, 0),            # Dark Green
    'batteries': (200, 150, 100)     # Light Brown
}

# Dictionary to store file paths for misclassified items
misclassified_items = {
    'paper': 'new_training_items/paper',
    'cardboard': 'new_training_items/cardboard',
    'trash': 'new_training_items/trash',
    'plastic': 'new_training_items/plastic',
    'metal': 'new_training_items/metal',
    'glass': 'new_training_items/glass',
    'batteries': 'new_training_items/batteries'
}

# Dictionary to map label to servo rotation
servo_rotation = {
    'paper': 60,
    'cardboard': 60,
    'trash': 120,
    'plastic': 180,
    'metal': 240,
    'glass': 300,
    'batteries': 360
}
##############################################################################
# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo = kit.servo[2]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo.set_pulse_width_range(500, 2500)

# Model 1: wjr83 selfmade dataset
# model_path = 'recycling_model_1/model.tflite'
# labels_path = "recycling_model_1/labels.txt"

# Model 2: Kaggle Dataset
model_path = 'smart_trashcan_model_v1/model.tflite'
labels_path = 'smart_trashcan_model_v1/labels.txt'

image_file_name = "frame.jpg"


tm_model = TeachableMachineLite(model_path=model_path, labels_file_path=labels_path)


text_color = (0, 0, 0)
servo.angle = 0

def confirm_classification(label, r, g, b):
    # label = results['label']
    label_counter.process_word(label)
    if label_counter.count == 50:
        flag = False
        #TODO: All LEDs on LED Stick should be turned on 
        # my_stick.change_length(label_counter.count // 50) # turn on the LED's as a progress bar of confidence
        # my_stick.set_all_LED_color(r, g, b)
    else:
        #TODO: Every 5 words turn on an LED
        pass
        # my_stick.change_length(label_counter.count // 50) # turn on the LED's as a progress bar of confidence
        # my_stick.set_all_LED_color(r, g, b)
    print("text_color:", colors_dict[label])
    text_color = (r, g, b)
    return text_color 
    # Set the servo to 180 degree position
    # servo.angle = 36*2
    # time.sleep(1)


def save_misclassified_item(label, frame):
    folder_path = misclassified_items.get(label)
    if folder_path:
        # Use the class name and timestamp to create a unique file name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_name = f"{label}_{timestamp}.jpg"
        image_path = os.path.join(folder_path, image_name)

        cv.imwrite(image_path, frame)
        print(f"Saved misclassified item ({label}) image to: {image_path}")
    else:
        print(f"Error: No folder path defined for misclassified item ({label})")

# Function to rotate servo to a specified set of degrees 
def rotate_servo(label):
    angle = servo_rotation.get(label)
    
    if angle is not None:
        # Ensure the angle is within the valid range (0 to 180)
        angle = max(0, min(angle, 180))
        
        # Set the servo angle
        kit.servo[2].angle = angle
        
        print(f"Rotated servo to {angle} degrees for item: {label}")
    else:
        print(f"Error: No servo angle defined for item: {label}")

def read_object():

    # Check if the camera opened successfully
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
    # Set the frame width and height (optional)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    flag = True
    while flag == True:

        # Get frame from camera
        ret, frame = cap.read()

        # Classify current fram of camera
        results = tm_model.classify_frame(image_file_name)
        label = results['label']

        # Set the color scheme for the LED Stick & Label on Camera
        r, g, b = colors_dict[results['label']][0], colors_dict[results['label']][1], colors_dict[results['label']][2]

        # Draw label on the frame
        if results['confidence'] > 0.5 and label != 'background':  # You can adjust the confidence threshold as needed
            if label == 'paper' or label == 'cardboard': # paper (1) and cardboard (2)
                text_color = confirm_classification(label, r, g, b)
            elif label == 'trash': # trash
                text_color = confirm_classification(label, r, g, b)
            elif label == 'plastic': # plastic
                text_color = confirm_classification(label, r, g, b)
            elif label == 'metal': # metal
                text_color = confirm_classification(label, r, g, b)
            elif label == 'glass': # glass
                text_color = confirm_classification(label, r, g, b)
            
            # Place text on Camera Display
            cv.putText(frame, results['label'], (100, 90), cv.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2) # coordinates (x, y) for text placement = (100, 90)
        
        # Display Camera & Prediction Label
        cv.imshow('Cam', frame)
        # Save current image
        cv.imwrite(image_file_name, frame)
        # Visualize Results in Terminal
        print("results:", results)

        # Break the loop if 'q' key is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv.destroyAllWindows()
            break


while True:

    # Classify Item
    read_object()

    time.sleep(5)
    
    k = cv.waitKey(1)
    if k% 255 == 27:
        # press ESC to close camera view.
        break


