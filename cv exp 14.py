import cv2
import numpy as np

img = cv2.imread((r'/Users/leakhana/Downloads/images.jpeg'))

rows, cols = img.shape[:2]

pts1 = np.float32([[50,50],[400,50],[50,400],[400,400]])
pts2 = np.float32([[10,100],[300,50],[100,300],[350,350]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

output = cv2.warpPerspective(img,matrix,(cols,rows))

cv2.imshow("Original",img)
cv2.imshow("Perspective",output)

cv2.waitKey(0)
cv2.destroyAllWindows()
