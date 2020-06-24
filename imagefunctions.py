import cv2
import numpy as np

img = cv2.imread("Resources/dog.png")
kernel = np.zeros((5,5), np.uint8)
#Grayscale image

greyimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurimg = cv2.GaussianBlur(greyimg,(5,5),0)
cannyimg = cv2.Canny(img,150,200)
dilimg = cv2.dilate(cannyimg,kernel, iterations=1)
erodedimg = cv2.erode(dilimg,kernel,iterations=1)

cv2.imshow("Grey", greyimg)
cv2.imshow("Blur", blurimg)
cv2.imshow("Canny", cannyimg)
cv2.imshow("Dilated", dilimg)
cv2.imshow("Eroded", erodedimg)

cv2.waitKey(0)