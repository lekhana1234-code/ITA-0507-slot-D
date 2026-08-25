import cv2
import numpy as np

image = cv2.imread((r'/Users/leakhana/Downloads/images.jpeg'))

if image is None:
    print("Error: Image not found!")
    exit()

kernel = np.ones((5, 5), np.uint8)

eroded_image = cv2.erode(image, kernel, iterations=1)

cv2.imwrite(r"C:\Users\sivad\OneDrive\Desktop\Computer Vision\eroded_output.jpg", eroded_image)

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
