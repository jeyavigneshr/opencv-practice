import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv2.line(img, (0,0), (512,512), (0,255,0), 2)
cv2.rectangle(img, (0,0), (100,150), (255,0,0), 2)
cv2.circle(img, (256,128), 30, (255,255,0), 2)
cv2.putText(img, "Jey", (256,128), cv2.FONT_ITALIC,1,(0,150,0),2)
cv2.imshow("Image", img)
cv2.waitKey(0)