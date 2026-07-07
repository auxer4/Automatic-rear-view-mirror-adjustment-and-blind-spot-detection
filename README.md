AUTOMATIC ADJUSTABLE REAR VIEW MIRROR FOR TWO WHEELERS
📌 Overview
Improper rearview mirror adjustments on two-wheelers significantly reduce rear visibility and can lead to accidents. This project aims to solve this issue by developing an Automatic Adjustable Rear View Mirror (AARM) system. The mirror automatically adjusts its angle based on the rider’s position, ensuring optimal visibility and enhancing rider safety.

🎯 Objective
To design a smart system that:

Detects the real-time position and posture of the rider.
Calculates the optimal mirror angle.
Adjusts the mirror dynamically using servo motors on a 2-DOF (Degree of Freedom) mount.
⚙️ Key Features
Real-time image capture of the rider and environment.
Pose estimation and position detection using computer vision.
Intelligent control of mirror orientation via servo motors.
Enhanced safety and convenience with automatic adjustments.
🧠 Methodology
Image Capture
Capturing the rider’s image and surroundings using a mounted camera.

Image Processing
Detecting the rider's head/torso position using image processing and pose detection algorithms (e.g., OpenCV, MediaPipe, or custom CNN models).

Angle Calculation
Computing the required angle for the rearview mirror to ensure optimal rear visibility.

Mirror Adjustment
Using servo motors mounted on 2-DOF joints to adjust the mirror in real-time based on computed angles.

🛠️ Technologies Used
Languages: Python, C++
Libraries/Frameworks: OpenCV, MediaPipe (or similar pose estimation tools)
Hardware: Camera module, Microcontroller (e.g., Arduino), Servo motors, Mirror mount
Tools: Breadboard, Jumper wires, Power supply
📦 Installation & Setup
Hardware should be connected and powered properly before running the software. _this is for aurduino uno Pyfirmeta Code must be uploaded to the arduino board

