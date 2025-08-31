
# Real-Time-Sign-Language-Detection-with-Web-interface

I have developed this project for my machine learning course by using all the basic knowledge of HTML,CSS for fontend design and python,Flask ,tensorflow, opencv and numpy libraries. For dataset, I have used my own hand dataset collected using laptop's web camera and then trained the data using google teachable machine.


## Features

- Real-time gesture detection using a webcam.
- Detects custom hand gestures (trained on own dataset).
- Displays the recognized gesture.
- Uses MediaPipe for accurate hand tracking.
- Built with TensorFlow for Machine Learning predictions.
- Uses Flask API for web interface


## Dataset
This project uses my own dataset of hand gestures. I collected the hand gestures(700+ images of 2 categories) using my web camera and trained them using google teachable machine. After that i exported them as keras model and use them.
## Requirements
- Flask(3.1.2)
- TensorFlow(2.12.10)
- OpenCV(4.11.0)
- NumPY(1.23.5)
- HTML
- CSS
- JavaScript


## Workflow
The project follows a real-time machine learning pipeline for sign language detection:

- Webpage Connection:HTML,CSS are used to create the webpage design and Flask API used to connect the web interface. 

- Data Collection & Model Preparation: The TensorFlow model is trained on custom hand gesture images collected specifically for this project.Each gesture (e.g., "Yes", "Hello") has multiple images for better generalization.

- Webcam Input & Hand Detection: The application accesses the webcam using OpenCV.MediaPipe's Hand Tracking module detects and tracks hand landmarks in real-time.

- Feature Extraction & Preprocessing:Hand landmarks are extracted as keypoints (x, y coordinates).Keypoints are normalized and reshaped to match the TensorFlow model input format.

- Gesture Prediction:Pre-processed features are fed into the TensorFlow model.The model predicts the gesture and outputs a confidence percentage for each gesture.

- Output Display:The predicted gesture is displayed on the screen along with the confidence score (e.g., "Hello – 92%").eal-time feedback allows users to see gestures detected live as they perform them.

- Optional Enhancements:Detect multiple gestures in sequence.
## User Guideline
- Activate your virtual environment.
- Install all libraries as mentioned earlier.
- Download the code files along with model.
- Place all files in a single folder.
- Use IDE(VS Code).
- Run the test Python script
- Perform hand gestures in front of the webcam.
- The predicted gesture and confidence will be displayed in real-time.