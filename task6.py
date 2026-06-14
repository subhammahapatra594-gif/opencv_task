import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Initial kernel size (must be odd)
kernel = 5

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (kernel, kernel), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, 100, 200)

    # Display kernel size
    cv2.putText(
        edges,
        f"Kernel: {kernel}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        255,
        2
    )

    # Show output
    cv2.imshow("Canny Edge Detection", edges)

    key = cv2.waitKey(1) & 0xFF

    # Increase blur
    if key == ord('i'):
        kernel += 2

    # Decrease blur
    elif key == ord('d'):
        kernel = max(3, kernel - 2)

    # Exit
    elif key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()