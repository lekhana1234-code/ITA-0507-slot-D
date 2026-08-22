import cv2

image = cv2.imread((r'/Users/leakhana/Downloads/images.jpeg'))

if image is None:
    print("Error: Image not found!")
    exit()

small_image = cv2.resize(image, (300, 200))
large_image = cv2.resize(image, (900, 600))

cv2.imwrite(r"C:\Users\sivad\OneDrive\Desktop\Computer Vision\small_image.jpg", small_image)
cv2.imwrite(r"C:\Users\sivad\OneDrive\Desktop\Computer Vision\large_image.jpg", large_image)

cv2.imshow("Original Image", image)
cv2.imshow("Smaller Image", small_image)
cv2.imshow("Larger Image", large_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
