import cv2
import time

# Start webcam
cap = cv2.VideoCapture(0)

# For FPS calculation
prev_time = 0

# Image counter
count = 1

while True:

    success, frame = cap.read()

    if not success:
        break

    # Current time
    current_time = time.time()

    # FPS formula
    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    # Display FPS
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show webcam feed
    cv2.imshow("Webcam Feed", frame)

    key = cv2.waitKey(1)

    # Save image when S is pressed
    if key == ord('s'):

        filename = f"image_{count}.png"

        cv2.imwrite(filename, frame)

        print(filename, "saved")

        count += 1

    # Exit when ESC pressed
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()