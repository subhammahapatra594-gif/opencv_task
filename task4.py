import cv2
import numpy as np

# Open Webcam
cap = cv2.VideoCapture(0)

while True:

    # Capture frame
    ret, frame = cap.read()

    if not ret:
        break

    # --------------------------------------------------
    # STEP 1
    # Remove mirror effect
    # --------------------------------------------------

    frame = cv2.flip(frame, 1)

    # --------------------------------------------------
    # STEP 2
    # Downscale to half size
    # --------------------------------------------------

    half_frame = cv2.resize(
        frame,
        None,
        fx=0.5,
        fy=0.5
    )

    # Convert half-size image to grayscale
    gray = cv2.cvtColor(
        half_frame,
        cv2.COLOR_BGR2GRAY
    )

    # Show grayscale image
    cv2.imshow(
        "Half Size Grayscale",
        gray
    )

    # --------------------------------------------------
    # STEP 3
    # Create quarter-size image
    # --------------------------------------------------

    quarter = cv2.resize(
        frame,
        None,
        fx=0.5,
        fy=0.5
    )

    # Top Left
    original = quarter.copy()

    # Top Right
    vertical_flip = cv2.flip(
        quarter,
        0
    )

    # Bottom Left
    hsv = cv2.cvtColor(
        quarter,
        cv2.COLOR_BGR2HSV
    )

    hsv_display = cv2.cvtColor(
        hsv,
        cv2.COLOR_HSV2BGR
    )

    # Bottom Right
    red_channel = np.zeros_like(quarter)

    red_channel[:, :, 2] = quarter[:, :, 2]

    # --------------------------------------------------
    # Join images
    # --------------------------------------------------

    top_row = np.hstack(
        (original, vertical_flip)
    )

    bottom_row = np.hstack(
        (hsv_display, red_channel)
    )

    final_output = np.vstack(
        (top_row, bottom_row)
    )

    # Display
    cv2.imshow(
        "Four View Window",
        final_output
    )

    # ESC to Exit
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()