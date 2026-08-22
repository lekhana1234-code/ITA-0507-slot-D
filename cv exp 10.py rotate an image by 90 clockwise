import cv2

image = cv2.imread((r'/Users/leakhana/Downloads/images.jpeg'))

if image is None:
    print("Error: Image not found!")
    exit()

rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite(r"C:\Users\sivad\OneDrive\Desktop\Computer Vision\rotated_output.jpg", rotated_image)

cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
