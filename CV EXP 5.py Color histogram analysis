import cv2
import matplotlib.pyplot as plt

analyze_histogram(r'/Users/leakhana/Downloads/images.jpeg')
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    cv2.imshow("Original Image", img)

    colors = ('b', 'g', 'r')

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])

        print(color.upper(), "Channel Histogram")
        print("Minimum intensity:", hist.min())
        print("Maximum frequency:", hist.max())
        print("Total pixels:", int(hist.sum()))
        print()

        plt.plot(hist, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


analyze_histogram(r'/Users/leakhana/Downloads/images.jpeg')
