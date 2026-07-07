[README (2).md](https://github.com/user-attachments/files/29746986/README.2.md)
# AUTOMATIC ADJUSTABLE REAR VIEW MIRROR FOR TWO WHEELERS

## 📌 Overview

Improper rear-view mirror adjustments on two-wheelers significantly
reduce rear visibility and can lead to accidents. This project aims to
solve this issue by developing an **Automatic Adjustable Rear View
Mirror (AARM)** system. The mirror automatically adjusts its angle based
on the rider's position, ensuring optimal visibility and enhancing rider
safety.

## 🎯 Objective

Design a smart system that: - Detects the rider's real-time position and
posture. - Calculates the optimal rear-view mirror angle. - Dynamically
adjusts the mirror using servo motors mounted on a **2-DOF (Degree of
Freedom)** mechanism.

## ⚙️ Key Features

-   Real-time image capture of the rider.
-   Pose estimation and position detection using computer vision.
-   Intelligent mirror orientation control using servo motors.
-   Automatic adjustment for improved safety and convenience.

## 🧠 Methodology

### 1. Image Capture

Capture the rider's image and surroundings using a mounted camera.

### 2. Image Processing

Detect the rider's head and shoulder position using image processing and
pose estimation algorithms such as **OpenCV** and **MediaPipe**.

### 3. Angle Calculation

Compute the optimal rear-view mirror angle to maximize rear visibility.

### 4. Mirror Adjustment

Control servo motors mounted on a **2-DOF** mechanism to adjust the
mirror in real time according to the calculated angles.

## 🛠️ Technologies Used

### Languages

-   Python
-   C++

### Libraries & Frameworks

-   OpenCV
-   MediaPipe
-   PyFirmata

### Hardware

-   Arduino Uno
-   USB Camera/Webcam
-   Servo Motors
-   Rear View Mirror Mount
-   Breadboard
-   Jumper Wires
-   Power Supply

## 📦 Installation & Setup

### Hardware Setup

1.  Connect all hardware components properly.
2.  Upload the **StandardFirmata** sketch to the **Arduino Uno** using
    the Arduino IDE.
3.  Connect the Arduino to your computer via USB.
4.  Ensure the camera is connected and accessible.

### Software Setup

1.  Install Python and the required dependencies.
2.  Install the required libraries:
    -   OpenCV
    -   MediaPipe
    -   PyFirmata
3.  Run the Python application.
4.  The system will detect the rider's posture and automatically adjust
    the rear-view mirror in real time.

## 🚀 Future Improvements

-   Wireless communication between camera and controller.
-   Integration with blind spot detection.
-   Support for different motorcycle models.
-   AI-based rider posture prediction for smoother mirror adjustment.

## 📄 License

This project is intended for educational and research purposes.
