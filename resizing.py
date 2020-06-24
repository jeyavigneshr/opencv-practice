import cv2

img = cv2.imread("Resources/DSC_0001.JPG")

#Finding size of the image
print(img.shape)
#Resize order in opencv is width and height
img = cv2.resize(img, (1000,600))
#Cropping order is height and width
imgCropped = img[100:500, 250:750]
cv2.imshow("Resized Image", img)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)