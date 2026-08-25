import cv2

img = cv2.imread((r'/Users/leakhana/Downloads/images.jpeg'))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)

sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

combined = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

cv2.imshow("Original",img)
cv2.imshow("Sobel X",sobelx)
cv2.imshow("Sobel Y",sobely)
cv2.imshow("Combined",combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
