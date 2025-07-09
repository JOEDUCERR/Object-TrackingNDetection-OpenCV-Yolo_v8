# Object-Tracking and Detection using OpenCV 🎯

This project demonstrates real-time object detection and tracking using YOLOv8 and OpenCV on a video input. It utilizes the lightweight yolov8n.pt model from the Ultralytics YOLOv8 family for efficient performance.

# 🚀 Features
Object detection using YOLOv8
Real-time tracking with persistency
Frame-by-frame annotation with detection overlays
Graceful exit with keypress
Simple and readable code

# 📁 Video Input
Replace the path in the script with your own video file:
'''
video_path = "path/to/your/video.mp4"
'''

# 🧠 Model
This project uses the YOLOv8 Nano model (yolov8n.pt) which is:
Lightweight
Fast for real-time applications
Good for CPU and GPU usage
The model is automatically downloaded by the ultralytics library if not already present.

# 🧩 Dependencies
Python 3.7+
Ultralytics
OpenCV
