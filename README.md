# Iris-Tracking-System

## Overview

The Iris Tracking and Gaze Estimation System is a sophisticated computer vision project designed to track the iris in real-time using a webcam or from an uploaded video file. The system utilizes advanced machine learning and computer vision techniques to estimate the user's gaze direction (left, right, or center) and the corresponding gaze angle. This project leverages the power of the MediaPipe Face Mesh model and integrates it with OpenCV for real-time processing and visualization.

## Results: 
![GIFMaker_me](https://github.com/user-attachments/assets/56ac0803-5a15-4aa5-a1a7-57dad1d95041)


## Features

- **Real-Time Iris Tracking**: Track the position of the user's iris in real-time using a webcam.
- **Video Processing**: Upload and process video files to analyze gaze direction frame by frame.
- **Gaze Estimation**: Calculate the direction (left, right, or center) and angle of the user's gaze based on the relative position of the iris.
- **User-Friendly GUI**: A simple graphical interface allows users to choose between real-time tracking and video processing.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
    - [Real-Time Tracking](#real-time-tracking)
    - [Video Processing](#video-processing)
3. [Technical Details](#technical-details)
    - [MediaPipe Face Mesh](#mediapipe-face-mesh)
    - [OpenCV Integration](#opencv-integration)
    - [Gaze Estimation Algorithm](#gaze-estimation-algorithm)
4. [Relevance to Human Interaction Research](#relevance-to-human-interaction-research)
5. [Contributing](#contributing)
6. 
## Installation

Before you start using the Iris Tracking and Gaze Estimation System, ensure you have the necessary dependencies installed. This project requires Python 3.6+ and several Python libraries.

### Dependencies

1. **Python 3.6+**
2. **OpenCV**: For video capture and image processing.
3. **MediaPipe**: For facial landmark detection, including iris tracking.
4. **tkinter**: For creating the GUI.
5. **NumPy**: For mathematical operations and handling arrays.

### Installing the Required Libraries

You can install all the required libraries using `pip`:

```bash
pip install opencv-python mediapipe numpy tk
```

## Usage

### Real-Time Tracking

To start the iris tracking in real-time using your webcam, run the following command in your terminal:

```bash
python iris_tracking.py
```

Once the script runs, a GUI will appear. Click on the "Real-Time Tracking" button to start the webcam feed.

### Video Processing

To process an uploaded video file and analyze the gaze direction, click the "Upload Video" button in the GUI. Select the video file you want to analyze, and the system will process each frame, displaying the gaze direction and angle.

## Technical Details

### MediaPipe Face Mesh

**MediaPipe** is a machine learning framework developed by Google that provides pre-trained models for various computer vision tasks, including facial landmark detection. The Face Mesh model detects over 468 facial landmarks in real-time, which are critical for precise facial feature tracking.

**Key Components**:

- **Facial Landmarks**: The model identifies key points on the face, including the eyes, mouth, nose, and jawline.
- **Iris Landmarks**: Specific landmarks are designated to the iris, allowing for accurate tracking of the eye's movements.

**How it Works**:

1. **Face Detection**: The model first detects the face in the video frame.
2. **Landmark Detection**: It then identifies 468 landmarks on the face, with special attention to the eyes and iris.
3. **Iris Tracking**: The iris landmarks are used to determine the center of the iris, essential for gaze estimation.

### OpenCV Integration

**OpenCV** (Open Source Computer Vision Library) is a powerful tool used for real-time computer vision tasks. In this project, OpenCV is utilized for:

- **Video Capture**: Capturing video input from the webcam or a video file.
- **Image Processing**: Converting the image from BGR to RGB, drawing circles, and overlaying text on the frames.
- **Display**: Visualizing the processed frames in a GUI window.

**Key Functions**:

- **cv2.VideoCapture()**: Initializes video capture from a webcam or video file.
- **cv2.cvtColor()**: Converts the color space from BGR (used by OpenCV) to RGB (used by MediaPipe).
- **cv2.circle()**: Draws circles on the frame to indicate the iris position.
- **cv2.putText()**: Displays text on the frame to show the gaze direction and angle.

### Gaze Estimation Algorithm

The gaze estimation algorithm calculates the direction of the user's gaze by analyzing the position of the iris relative to the eye corners and the nose. The steps involved are:

1. **Iris Center Calculation**: The center of the iris is computed using the average of the iris landmarks.
2. **Relative Positioning**: The iris center is compared to the eye corners to determine the gaze direction.
3. **Angle Calculation**: An angle is calculated between the nose tip, eye corner, and iris center to quantify the gaze direction.

**Relevance**:

This algorithm is critical in human-computer interaction (HCI) research as it enables systems to understand where the user is looking, which can be used in various applications such as eye-tracking studies, user experience testing, and assistive technologies.

## Relevance to Human Interaction Research

### Importance in HCI

Gaze tracking and estimation play a vital role in Human-Computer Interaction (HCI) research. Understanding where a user is looking can provide valuable insights into their cognitive state, attention, and intentions. The ability to accurately track and estimate gaze direction enables:

- **User Experience Studies**: Understanding how users interact with interfaces by tracking where they look.
- **Assistive Technology**: Developing tools for individuals with disabilities, allowing them to control devices using their eyes.
- **Behavioral Analysis**: Studying human behavior and reactions in different scenarios, which is particularly valuable in psychology and cognitive science research.
- **Augmented Reality (AR) and Virtual Reality (VR)**: Enhancing user interaction within virtual environments by allowing systems to respond to where users are looking.

### Applications

This project can be integrated into several fields of study:

1. **Eye-Tracking Studies**: Used to analyze where users focus their attention on a screen.
2. **Assistive Devices**: Enables gaze-based interaction for individuals with mobility impairments.
3. **Marketing Research**: Understanding user engagement with visual content.
4. **Psychological Research**: Studying the correlation between gaze patterns and cognitive states.

## Contributing

Contributions to the Iris Tracking and Gaze Estimation System are welcome. If you have suggestions for improvements or new features, feel free to submit a pull request or open an issue.

### Guidelines

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure the code is well-documented.
4. Submit a pull request with a detailed explanation of your changes.

