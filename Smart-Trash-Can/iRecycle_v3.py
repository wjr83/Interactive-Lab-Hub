from teachable_machine_lite import TeachableMachineLite
import os
import shutil
import sys
from datetime import datetime
import cv2 as cv
import time
from adafruit_servokit import ServoKit
import qwiic_led_stick
from word_counter import WordCounter # custom class to validate reading from camera
import walking_rainbow_LED_stick
import qwiic_button

##############################################################################
# Check if the camera opened successfully
def initialize_camera():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    return cap

##############################################################################
label_counter = WordCounter()

walking_rainbow_LED_stick.run_example()
my_stick = qwiic_led_stick.QwiicLEDStick()
my_stick.set_all_LED_color(0,50,0)
my_stick.set_all_LED_brightness(1)
# Turn on all the LEDs to white
my_stick.LED_off()

if my_stick.begin() == False:
    print("\nThe Qwiic LED Stick isn't connected to the sytsem. Please check your connection", \
        file=sys.stderr)

print("\nLED Stick ready!")
##############################################################################

# Dictionary to map classifications to colors
colors_dict = {
    'background': (0,0,0),          # Off
    'paper': (0, 0, 255),           # Blue
    'cardboard': (0, 0, 255),       # Blue      # (128, 0, 128),       # Purple
    'trash': (255, 255, 255),       # White
    'plastic': (255, 0, 0),         # Red
    'metal': (255, 255, 0),         # Yellow             
    'glass': (0, 255, 0),           # Green
    'battery': (255, 13, 0)         # Orange
}

# Dictionary to store file paths for misclassified items
misclassified_items = {
    'paper': 'new_training_items/paper',
    'cardboard': 'new_training_items/cardboard',
    'trash': 'new_training_items/trash',
    'plastic': 'new_training_items/plastic',
    'metal': 'new_training_items/metal',
    'glass': 'new_training_items/glass',
    'battery': 'new_training_items/battery'
}

# Dictionary to map label to servo rotation
servo_index = {
    'paper': 0,
    'cardboard': 0,
    'trash': 7,
    'plastic': 8,
    'metal': 15,
    'glass': 10,
    'battery': 12
}

# Dictionary to map label to qwiic button
qwiic_button_address = {
    'paper': 0x6b,      # Soldered: A2 -> Green Button
    'cardboard': 0x6b,  # Soldered: A2 -> Green Button
    'trash': 0x6c,      # Soldered: A0 & A1 -> Green Button
    'plastic': 0x6e,    # Soldered: A0 -> Green Button
    'metal': 0x69,      # Soldered: A1 & A2 -> Green Button
    'glass': 0x67,      # Soldered: A3 -> Green Button 
    'battery': 0x63   # Soldered: A2 & A3 -> Green Button
}
##############################################################################
# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to channel using for physical prototype.
servo_paper_cardboard = kit.servo[servo_index['paper']]
servo_trash = kit.servo[servo_index['trash']]
servo_plastic = kit.servo[servo_index['plastic']]
servo_metal = kit.servo[servo_index['metal']]
servo_glass = kit.servo[servo_index['glass']]
servo_battery = kit.servo[servo_index['battery']]


# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo_paper_cardboard.set_pulse_width_range(525, 2500)
servo_trash.set_pulse_width_range(525, 2500)
servo_plastic.set_pulse_width_range(525, 2500)
servo_metal.set_pulse_width_range(525, 2500)
servo_glass.set_pulse_width_range(525, 2500)
servo_battery.set_pulse_width_range(525, 2500)
#############################################################################################################
# Initialize buttons for each class
red_button = qwiic_button.QwiicButton(0x6f) # Soldered: None (Set -> Red Button)
paper_button = qwiic_button.QwiicButton(qwiic_button_address['paper']) # Soldered: A2 -> Green Button
trash_button = qwiic_button.QwiicButton(qwiic_button_address['trash']) # Soldered: A0 & A1 -> Green Button
plastic_button = qwiic_button.QwiicButton(qwiic_button_address['plastic']) # Soldered: A0 -> Green Button
metal_button = qwiic_button.QwiicButton(qwiic_button_address['metal']) # Soldered: A1 & A2 -> Green Button
glass_button = qwiic_button.QwiicButton(qwiic_button_address['glass']) # Soldered: A3 -> Green Button 
battery_button = qwiic_button.QwiicButton(qwiic_button_address['battery']) # Soldered: A2 & A3 -> Green Button

##############################################################################################################
# Model 1: wjr83 selfmade dataset
# model_path = 'recycling_model_1/model.tflite'
# labels_path = "recycling_model_1/labels.txt"

# Model 2: Kaggle Dataset
model_path = 'smart_trashcan_model_v1/model.tflite'
labels_path = 'smart_trashcan_model_v1/labels.txt'

image_file_name = "frame.jpg"


tm_model = TeachableMachineLite(model_path=model_path, labels_file_path=labels_path)


text_color = (0, 0, 0)

# Ensure all bin lids are closed
servo_paper_cardboard.angle = 90
servo_trash.angle = 90
servo_plastic.angle = 90
servo_metal.angle = 97  # Correction for this particular servo after testing
servo_glass.angle = 90
servo_battery.angle = 90


def confirm_classification(label, r, g, b):
    # label = results['label']
    label_counter.process_word(label)
    if label_counter.count == 10:
        flag = False
        #TODO: All LEDs on LED Stick should be turned on 
        # my_stick.change_length(label_counter.count // 50) # turn on the LED's as a progress bar of confidence
        my_stick.set_all_LED_color(r, g, b)
    elif label_counter.count == 0:
        my_stick.LED_off()
        time.sleep(0.5) # Account for person placing object
        my_stick.set_single_LED_color(0, r, g, b)
        time.sleep(0.5) # Account for person placing object
    else:
        #TODO: Every 5 words turn on an LED
        pass
        time.sleep(0.1) # Necessary to avoid spamming the bus. Prevents I/O error
        my_stick.set_single_LED_color(label_counter.count, r, g, b) # turn on the LED's as a progress bar of confidence
        # my_stick.set_all_LED_color(r, g, b)
    print("text_color:", colors_dict[label])
    text_color = (r, g, b)
    return text_color 
    # Set the servo to 180 degree position
    # servo.angle = 36*2
    # time.sleep(1)


def save_item(label, frame): # Increase dataset of objects by saving a picture to folder
    folder_path = misclassified_items.get(label)
    if folder_path:
        # Use the class name and timestamp to create a unique file name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_name = f"{label}_{timestamp}.jpg"
        image_path = os.path.join(folder_path, image_name)

        cv.imwrite(image_path, frame)
        print(f"Saved classified item ({label}) image to: {image_path}")
    else:
        print(f"Error: No folder path defined for misclassified item ({label})")

# If item was misclassified, user inputs correct label by pressing the red button followed by the corrected green button associated with the class.
def move_item_to_correct_folder(label, corrected_label):
    # Get the folder paths for misclassified and correct labels
    misclassified_folder = misclassified_items.get(label)
    correct_folder = misclassified_items.get(corrected_label)

    if misclassified_folder and correct_folder:
        # Get the list of files in the misclassified folder
        misclassified_files = os.listdir(misclassified_folder)

        if misclassified_files:
            # Move the last item to the correct folder
            last_item = misclassified_files[-1]
            misclassified_item_path = os.path.join(misclassified_folder, last_item)
            correct_item_path = os.path.join(correct_folder, last_item)

            # Move the item
            shutil.move(misclassified_item_path, correct_item_path)

            # Rename the file in the correct folder
            base_name, extension = os.path.splitext(last_item)
            new_name = f"{base_name}_corrected{extension}"
            new_item_path = os.path.join(correct_folder, new_name)
            os.rename(correct_item_path, new_item_path)

            print(f"Moved {last_item} from '{misclassified_folder}' to '{correct_folder}'.")
            print(f"Renamed to {new_name} in '{correct_folder}'.")

            # Rotate the corresponding servo by 90 degrees
            open_lid(corrected_label)
            # time.sleep(1)  # Adjust sleep time as needed
        else:
            print(f"No items found in '{misclassified_folder}'.")
    else:
        print("Error: Invalid labels or folder paths.")


def turn_on_button(label,brightness=150):
    if label == 'paper' or label == 'cardboard': # paper (1) and cardboard (2)
        paper_button.LED_on(brightness)
    elif label == 'trash': # trash
        trash_button.LED_on(brightness)
    elif label == 'plastic': # plastic
         plastic_button.LED_on(brightness)
    elif label == 'metal': # metal
        metal_button.LED_on(brightness)
    elif label == 'glass': # glass
        glass_button.LED_on(brightness)
    elif label == 'battery': # battery
        battery_button.LED_on(brightness)

def turn_off_button(label,brightness=0):
    if label == 'paper' or label == 'cardboard': # paper (1) and cardboard (2)
        paper_button.LED_on(brightness)
    elif label == 'trash': # trash
        trash_button.LED_on(brightness)
    elif label == 'plastic': # plastic
         plastic_button.LED_on(brightness)
    elif label == 'metal': # metal
        metal_button.LED_on(brightness)
    elif label == 'glass': # glass
        glass_button.LED_on(brightness)
    elif label == 'battery': # battery
        battery_button.LED_on(brightness)
 

# Function to rotate servo pertaining to identified item to a specified set of degrees 
def open_lid(label, degrees=0):
    turn_on_button(label)
    if label == 'paper' or label == 'cardboard': # paper (1) and cardboard (2)
        servo_paper_cardboard.angle = degrees
    elif label == 'trash': # trash
        servo_trash.angle = degrees
    elif label == 'plastic': # plastic
         servo_plastic.angle = degrees
    elif label == 'metal': # metal
        servo_metal.angle = degrees
    elif label == 'glass': # glass
        servo_glass.angle = degrees
    elif label == 'battery': # battery
        servo_battery.angle = degrees

# Function to rotate servo pertaining to identified item to a specified set of degrees 
def close_lid(label, degrees=90):
    turn_off_button(label)
    if label == 'paper' or label == 'cardboard': # paper (1) and cardboard (2)
        servo_paper_cardboard.angle = degrees
    elif label == 'trash': # trash
        servo_trash.angle = degrees
    elif label == 'plastic': # plastic
         servo_plastic.angle = degrees
    elif label == 'metal': # metal
        servo_metal.angle = 97
    elif label == 'glass': # glass
        servo_glass.angle = degrees
    elif label == 'battery': # battery
        servo_battery.angle = degrees
        

def read_object():


    label_counter.count = 0 # Reset counter everytime a new object is placed onto the tray
    while True: 

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
                if label_counter.count == 10:
                    save_item(label, frame) # save image to class folder 
                    cap.release()
                    cv.destroyAllWindows() # Close Camera Window
                    break
            elif label == 'trash': # trash
                text_color = confirm_classification(label, r, g, b)
                if label_counter.count == 10:
                    save_item(label, frame) # save image to class folder 
                    cap.release()
                    cv.destroyAllWindows() # Close Camera Window
                    break
            elif label == 'plastic': # plastic
                text_color = confirm_classification(label, r, g, b)
                if label_counter.count == 10:
                    save_item(label, frame) # save image to class folder 
                    cap.release()
                    cv.destroyAllWindows() # Close Camera Window
                    break
            elif label == 'metal': # metal
                text_color = confirm_classification(label, r, g, b)
                if label_counter.count == 10:
                    save_item(label, frame) # save image to class folder 
                    cap.release()
                    cv.destroyAllWindows() # Close Camera Window
                    break
            elif label == 'glass': # glass
                text_color = confirm_classification(label, r, g, b)
                if label_counter.count == 10:
                    save_item(label, frame) # save image to class folder 
                    cap.release()
                    cv.destroyAllWindows() # Close Camera Window
                    break
            elif label == 'battery': # battery
                text_color = confirm_classification(label, r, g, b)
                if label_counter.count == 10:
                    save_item(label, frame) # save image to class folder 
                    cap.release()
                    cv.destroyAllWindows() # Close Camera Window
                    break
            
            # Place text on Camera Display
            cv.putText(frame, results['label'], (100, 90), cv.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2) # coordinates (x, y) for text placement = (100, 90)
        else:
            time.sleep(0.1)
            my_stick.LED_off() # Turn off LED Stick if reading background

        # Display Camera & Prediction Label
        if label_counter.count < 10: # Only display camera output prior to prediction confirmation
            cv.imshow('Cam', frame)
            # Save current image
            cv.imwrite(image_file_name, frame)
        # Visualize Results in Terminal
        print("results:", results)

        # To terminate the program, press 'q' on the keyboard
        if cv.waitKey(1) & 0xFF == ord('q'):
            cap.release() # Close Camera Connection
            cv.destroyAllWindows() # Close Camera Window
            my_stick.LED_off() # Turn of LED Stick
            # Break the loop if 'q' key is pressed
            sys.exit(0)
    return label

# Decoration Function for LED Button
def perform_led_pattern(button, duration=0.05):
    button.LED_on(200)
    time.sleep(duration)
    button.LED_on(0)


from teachable_machine_lite import TeachableMachineLite
import os
import shutil
import sys
from datetime import datetime
import cv2 as cv
import time
from adafruit_servokit import ServoKit
import qwiic_led_stick
import walking_rainbow_LED_stick
import qwiic_button
from word_counter import WordCounter

# Constants
MODEL_PATH = 'smart_trashcan_model_v1/model.tflite'
LABELS_PATH = 'smart_trashcan_model_v1/labels.txt'
IMAGE_FILE_NAME = "frame.jpg"
BACKGROUND_CONFIDENCE_THRESHOLD = 0.5

def initialize_camera():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    return cap

def initialize_led_stick():
    walking_rainbow_LED_stick.run_example()
    my_stick = qwiic_led_stick.QwiicLEDStick()
    my_stick.set_all_LED_color(0, 50, 0)
    my_stick.set_all_LED_brightness(1)
    my_stick.LED_off()
    
    if not my_stick.begin():
        print("\nThe Qwiic LED Stick isn't connected to the system. Please check your connection", file=sys.stderr)
    
    print("\nLED Stick ready!")
    return my_stick


def classify_object(cap, tm_model, label_counter, my_stick):
    label_counter.count = 0
    while True:
        ret, frame = cap.read()
        results = tm_model.classify_frame(IMAGE_FILE_NAME)
        label = results['label']
        r, g, b = colors_dict[label][0], colors_dict[label][1], colors_dict[label][2]
        
        if results['confidence'] > 0.5 and label != 'background':
            text_color = confirm_classification(label, r, g, b)
            if label_counter.count == 10:
                save_item(label, frame)
                break
        else:
            time.sleep(0.1)
            my_stick.LED_off()
        
        if label_counter.count < 10:
            cv.imshow('Cam', frame)
            cv.imwrite(IMAGE_FILE_NAME, frame)
        
        print("results:", results)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv.destroyAllWindows()
            my_stick.LED_off()
            sys.exit(0)
    
    return label


def is_background_detected(cap, tm_model):
    label_counter.count = 0
    ret, frame = cap.read()
    cv.imwrite(IMAGE_FILE_NAME, frame)
    results = tm_model.classify_frame(IMAGE_FILE_NAME)
    cv.putText(frame, results['label'], (100, 90), cv.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)
    cv.imshow('Cam', frame)
    print("results:", results)
    
    return results['label'] == 'background' and results['confidence'] > BACKGROUND_CONFIDENCE_THRESHOLD


def main():
    cap = initialize_camera()
    my_stick = initialize_led_stick()
    tm_model = TeachableMachineLite(model_path=MODEL_PATH, labels_file_path=LABELS_PATH)
    label_counter = WordCounter()

    try:
        while True:
            label = classify_object(cap, tm_model, label_counter, my_stick)

            while True:
                if is_background_detected(cap, tm_model):
                    break
                
                if red_button.is_button_pressed():
                    red_button.LED_on(150)
                    print("Misclassification detected. Press a correction button.")
                    
                    corrected_label = None
                    while corrected_label is None:
                        # Correction button handling...
                        time.sleep(0.1)
                    
                    close_lid(label)
                    open_lid(corrected_label)
                    move_item_to_correct_folder(label, corrected_label)
                    time.sleep(2)
                    close_lid(corrected_label)
                    
                    break

            time.sleep(1)
            open_lid(label, 0)
            time.sleep(2)
            close_lid(label)
            time.sleep(1)

    except (KeyboardInterrupt, SystemExit) as exErr:
        print("Terminating iRecycle")
        my_stick.LED_off()
        sys.exit(0)

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()

    #     # TODO: Open lid corresponding to item detected. Update block accordingly to support feedback.
    #     close_lid(label)

    #     # TODO: Display Prediction on OLED Screen. 

    #     # TODO: Add feedback to correct wrong prediction using Qwiic Buttons. Make sure instruction to do so are clear (these can be written on the physical prototype)
    #     # This includes closing the lid for the miscclassification and opening the correct lid based on the button pressed by the user mapped to the correct classification.
    #     # Make sure to save picture of the object in the correct folder, and remove the picture of item in the folder that it was previously saved inside the read_object() function.
        
    #     time.sleep(2) 

    #     # TODO: Close lid (when should the lid close? After how much time if the object was classified correctly?) 
    #     # Should we run a classification on when a hand is detected and then count 10 seconds from there? 
    #     # Should the distance sensor capture this when the lid is open? NOTE: The angle of the distance sensor is very tiny, likely to miss objects being placed inside.
    #     # Should we have a 2nd camera to indicate when a person moves/grabs object/ leaves away from the system? 
    #     # NOTE: Best Idea so far: If the lid is open, run a function to check when background is detected again. Only when background is detected again. 
    #     # If so, wait for 10 seconds before runing the read_object() function to classify a new object.   
    #     open_lid(label, 0)

    #     # TODO: Integrate distance sensors using i2c mux to show ow full each bin is. 

    #     # TODO: Use distance sensor to send information to the "maintenance department's" Raspberry Pi via MQTT indicating 
    #     # location of iRecycle trashcan and which bins are full / need to be emptied out. This should be display on the OLED screen
    #     # of the "maintenance department's" Raspberry Pi. Once the bin is emptied out, the distance sensor should update the OLED screen
    #     # on Raspberry Pi of the maintenance departement showing that no bin needs to be emptied out. The maintenance department should 
    #     # not need to press any button to confirm the bins were emptied (this should be captured automatically by the distance sensor). 
    #     # We do NOT need a way (a code, that only the maintenance department knows) to open the lid when when the trash is full as the bins are not
    #     # physically attached to the lids, they simply sit underneath the lid. The bins are all independent from each other. The lids are attached to the 
    #     # "table" of the system, not the actual bins.

    #     # TODO: Nice to have: a button to pause/resume execution of the read_object() function in case the maintenance department needs to clean the spot 
    #     # where items are placed and avoid any noisy data from being captured.

    
    # except (KeyboardInterrupt, SystemExit) as exErr:
    #     print("Terminating iRecycle")
    #     my_stick.LED_off() # Turn off LED Stick
    #     # Break the loop if 'q' key is pressed
    #     sys.exit(0)
   
    # k = cv.waitKey(1)
    # if k% 255 == 27:
    #     # press ESC to close camera view.
    #     break


