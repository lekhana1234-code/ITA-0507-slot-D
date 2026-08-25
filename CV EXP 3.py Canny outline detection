import cv2

# Read the image
image = cv2.imread(r'/Users/leakhana/Downloads/images.jpeg')

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Detection", edges)

    # Save the output image
    cv2.imwrite("outline_image.jpg", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
