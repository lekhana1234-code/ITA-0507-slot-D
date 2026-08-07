import cv2

# Read the image in grayscale
img = cv2.imread(r'/Users/leakhana/Downloads/images.jpeg', cv2.IMREAD_GRAYSCALE)

# Check whether the image is loaded
if img is None:
    print("Error: Image not found. Check the file path.")
else:
    # Apply Histogram Equalization
    equalized = cv2.equalizeHist(img)

    # Display Original and Equalized Images
    cv2.imshow("Original Image", img)
    cv2.imshow("Histogram Equalized Image", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
