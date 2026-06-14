import cv2
import mediapipe as mp
import math

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Webcam
cap = cv2.VideoCapture(0)

# LED state (False = OFF, True = ON)
led_on = False

# To avoid multiple toggles while fingers stay pinched
pinch_detected = False

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Flip for mirror view
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hand
    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            # Thumb tip (Landmark 4)
            thumb = hand.landmark[4]

            # Index finger tip (Landmark 8)
            index = hand.landmark[8]

            h, w, _ = frame.shape

            # Convert to pixel coordinates
            x1 = int(thumb.x * w)
            y1 = int(thumb.y * h)

            x2 = int(index.x * w)
            y2 = int(index.y * h)

            # Draw points
            cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
            cv2.circle(frame, (x2, y2), 10, (0, 255, 0), -1)

            # Distance formula
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

            # Pinch threshold
            if distance < 40:

                # Toggle only once per pinch
                if not pinch_detected:
                    led_on = not led_on
                    pinch_detected = True

            else:
                pinch_detected = False

    # Draw LED
    if led_on:
        color = (0, 255, 0)      # Green = ON
    else:
        color = (0, 0, 255)      # Red = OFF

    cv2.circle(frame, (100, 100), 40, color, -1)

    cv2.imshow("LED Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()