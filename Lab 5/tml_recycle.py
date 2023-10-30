from teachable_machine_lite import TeachableMachineLite
import cv2 as cv

cap = cv.VideoCapture(0)

model_path = 'recycling_model_1/model.tflite'
# model_path = 'lite-model_yolo-v5-tflite_tflite_model_1.tflite'
# model_path = 'ssd_mobilenet_v1_1_metadata_1.tflite'


image_file_name = "frame.jpg"
labels_path = "recycling_model_1/labels.txt"
# labels_path = "labelmap.txt"

tm_model = TeachableMachineLite(model_path=model_path, labels_file_path=labels_path)

# Initialize variables for object tracking
tracking = True
prev_x, prev_y, prev_w, prev_h = 0, 0, 0, 0

while True:
    ret, frame = cap.read()
    results = tm_model.classify_frame(image_file_name)

     # Draw a bounding box and label on the frame
    if results['confidence'] > 0.5:  # You can adjust the confidence threshold as needed
        
        x, y, w, h = 100, 100, 200, 200  # Adjust the coordinates and size of the bounding box
        if tracking:
            # Adjust the bounding box position based on object movement
            x += int(0.2 * (x - prev_x))
            y += int(0.2 * (y - prev_y))
            w += int(0.2 * (w - prev_w))
            h += int(0.2 * (h - prev_h))
        tracking = True
    else:
        tracking = False

    # Draw a bounding box and label on the frame
    prev_x, prev_y, prev_w, prev_h = x, y, w, h
    # cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle
    cv.putText(frame, results['label'], (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv.imshow('Cam', frame)
    cv.imwrite(image_file_name, frame)
    
    
    print("results:",results)
    
    k = cv.waitKey(1)
    if k% 255 == 27:
        # press ESC to close camera view.
        break


