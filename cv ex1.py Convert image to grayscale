import cv2

# Read the image
image = cv2.imread(r'/Users/leakhana/Downloads/images.jpeg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite("grayscale.jpg", gray)

# Display the original and grayscale images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
