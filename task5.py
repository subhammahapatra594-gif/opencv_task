import cv2
import numpy as np

# Read image
image = cv2.imread("image2.jpeg")

# Check image
if image is None:
    print("Image not found")
    exit()

# Split channels
blue, green, red = cv2.split(image)

# Display channels
cv2.imshow("Blue Channel", blue)
cv2.imshow("Green Channel", green)
cv2.imshow("Red Channel", red)

# Remove Green channel
zero = np.zeros_like(green)

# Merge Blue + Zero + Red
merged = cv2.merge((blue, zero, red))

# Display merged image
cv2.imshow("Green Removed", merged)

# Save images
cv2.imwrite("blue_channel.jpg", blue)
cv2.imwrite("green_channel.jpg", green)
cv2.imwrite("red_channel.jpg", red)
cv2.imwrite("green_removed.jpg", merged)

print("Images saved successfully")

cv2.waitKey(0)
cv2.destroyAllWindows()