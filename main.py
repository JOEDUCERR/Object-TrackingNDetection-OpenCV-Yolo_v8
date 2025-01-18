from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO('yolov8n.pt')

# Load video
video_path = "C:/Users/joeg1/OneDrive/Documents/Projects - All/Object_tracking_OpenCV/dogvideo.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Read and process frames
while True:
    ret, frame = cap.read()
    if not ret:  # Break the loop when the video ends or cannot read a frame
        print("End of video or cannot read frame.")
        break

    # Ensure the frame is valid before proceeding
    if frame is not None:
        # Detect and track objects
        results = model.track(frame, persist=True)

        # Plot results on the frame
        frame_ = results[0].plot()

        # Display the frame with results
        cv2.imshow('frame', frame_)

        # Exit the loop on 'q' key press
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("Exiting on user request.")
            break
    else:
        print("Warning: Received an empty frame. Skipping.")

# Release resources
cap.release()
cv2.destroyAllWindows()
