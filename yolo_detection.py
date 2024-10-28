import cv2
import torch

# Load YOLOv5 model from the yolov5 package
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Capture video from webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)
    
    # Render the bounding boxes and labels
    frame = results.render()[0]

    # Show the frame with detections
    cv2.imshow('YOLO Object Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
