import inspect
inspect.getargspec = inspect.getfullargspec

import cv2
import mediapipe as mp
import math
import time
from pyfirmata import Arduino, util, SERVO

port = 'COM5'
servox = 9
servoy = 10
board = Arduino(port)
board.digital[servox].mode = SERVO
board.digital[servoy].mode = SERVO

def movx(angle):
    board.digital[servox].write(angle)
    time.sleep(0.05)

def movy(angle):
    board.digital[servoy].write(angle)
    time.sleep(0.05)

# Function to draw a point with a specific color
def draw_point(img, color, center):
    cv2.circle(img, center, 5, color, -1)

# Function to calculate the distance between two points
def calculate_distance(pt1, pt2):
    return math.sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

def map_value(x, in_min, in_max, out_min, out_max, base, top):
    if base == 1:
        movx((x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min)
    elif top == 1:
        movy((x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min)

# Initialize MediaPipe's holistic model
mp_holistic = mp.solutions.holistic.Holistic(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Camera setup
width = 320
height = 240
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FPS, 60 )
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

movx(90)
movy(90)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Reference point as a percentage of the screen
ref_x_percent = 50
ref_y_percent = 50
reference_point = (int(ref_x_percent / 100 * frame_width),
                   int(ref_y_percent / 100 * frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_holistic.process(frame_rgb)

    if results.pose_landmarks is not None:
        right_shoulder = (
            int(results.pose_landmarks.landmark[mp.solutions.holistic.PoseLandmark.RIGHT_SHOULDER].x * frame_width),
            int(results.pose_landmarks.landmark[mp.solutions.holistic.PoseLandmark.RIGHT_SHOULDER].y * frame_height)
        )

        draw_point(frame, (0, 0, 255), right_shoulder)
        text = "ShoPos: ({}, {})".format(right_shoulder[0], right_shoulder[1])
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        x_movement = reference_point[0] - right_shoulder[0]
        y_movement = reference_point[1] - right_shoulder[1]
        text = "MovTo: ({}, {}) pixels".format(x_movement, y_movement)
        cv2.putText(frame, text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        it = util.Iterator(board)
        it.start()

        if x_movement < 0:
            x_movement = -x_movement
            movx(90 - x_movement // 2.35)
        else:
            movx(90 + x_movement // 2.35)

        if y_movement < 0:
            y_movement = -y_movement
            movy(90 + y_movement // 2.35)
        else:
            movy(90 - y_movement // 2.35)

    draw_point(frame, (0, 255, 0), reference_point)
    cv2.imshow('Shoulder Detected', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

movx(90)
movy(90)
cap.release()
cv2.destroyAllWindows()