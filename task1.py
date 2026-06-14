import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

canvas = np.zeros((480, 640, 3), dtype=np.uint8)

prev_x, prev_y = 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:

            h, w, _ = frame.shape

            # Index finger tip
            x = int(hand.landmark[8].x * w)
            y = int(hand.landmark[8].y * h)

            cv2.circle(frame, (x, y), 8, (0, 255, 0), -1)

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            cv2.line(canvas, (prev_x, prev_y), (x, y),
                     (255, 255, 255), 5)

            prev_x, prev_y = x, y
    else:
        prev_x, prev_y = 0, 0

    output = cv2.add(frame, canvas)

    cv2.imshow("Virtual Drawing Board", output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):     # clear canvas
        canvas[:] = 0

    elif key == ord('s'):   # save drawing
        cv2.imwrite("All Images/drawing.png", canvas)
        print("Drawing saved as drawing.png")

    elif key == 27:         # ESC
        break

cap.release()
cv2.destroyAllWindows()
