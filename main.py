import cv2
import numpy as np

img = cv2.imread('img/image.JPG')
cv2.imshow("image", img)
# cv2.imshow('Result', img[0:100, 0:150]) - schneiden
# new_img = cv2.resize(img, (300, 500)) große
# new_img1 = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) porperitionale große 
# img = cv2.GaussianBlur(img, (3,3), 0) - Blur nur nechotnie 3,5,9...
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) - convert.color für bessere auslesung 
# img = cv2.Canny(img, 200, 200) - find eckel bilder - macht bilder in binar
# img = cv2.dilate(img, )


kernel = np.ones((5, 5), np.uint8) # - macht matriza wo alle elements sind (spysok v spysok)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
cv2.waitKey(0)
cv2.destroyAllWindows()



### video example 

#/
# cap = cv2.VideoCapture('videos/Road.mp4') webcam == 0 - index camera 
# cap.set(3, 500)
# cap.set(4, 500)
#
# while True:
#      success, img = cap.red()
#       cv2.imshow('Result', img)
#
#       if cv2.waitKey(1) & ord('q') == 0xFF:
#           break 