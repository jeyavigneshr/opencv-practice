################Practice for Basic Open CV operations###############

import cv2

#Basic Image read
# img = cv2.imread("Resources/DSC_0001.JPG.JPG")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# Basic Video Read

#video_capture = cv2.VideoCapture("Resources/video.mp4")

#Webcam read
video_capture = cv2.VideoCapture(0)
video_capture.set(3,640)
video_capture.set(4,480)

#While loop to capture the images
while True:
    success, img = video_capture.read()
    cv2.imshow("Video Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
