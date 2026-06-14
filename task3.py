import cv2

# Read image
image = cv2.imread("image1.jpeg")

# Check if image loaded
if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
height, width, channels = image.shape

# Calculate total pixels
total_pixels = height * width

print("Image Information")
print("------------------")
print("Height =", height)
print("Width =", width)
print("Channels =", channels)
print("Total Pixels =", total_pixels)

# Noise Removal
denoised = cv2.fastNlMeansDenoisingColored(
    image,
    None,
    10,
    10,
    7,
    21
)

# Save denoised image
cv2.imwrite("denoised_image.jpg", denoised)

print("Denoised image saved successfully!")

# Resize for display
display_original = cv2.resize(image, (800, 600))
display_denoised = cv2.resize(denoised, (800, 600))

# Create resizable windows
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Denoised Image", cv2.WINDOW_NORMAL)

# Show images
cv2.imshow("Original Image", display_original)
cv2.imshow("Denoised Image", display_denoised)

cv2.waitKey(0)
cv2.destroyAllWindows()