import cv2

img = cv2.imread((r'/Users/leakhana/Downloads/images.jpeg'))

cv2.putText(img, "WATCH DETECTED", (30,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0,255,0), 2)

cv2.rectangle(img, (120,100), (320,300), (0,255,0), 2)

cv2.imshow("Watch Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
