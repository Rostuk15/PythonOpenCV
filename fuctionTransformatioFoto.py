import cv2
import numpy as np 


img = cv2.imread("img/image.JPG")

new_img = np.zeros(img.shape, dtype='uint8')


### -find contur image 

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img, con, -1, (230, 111, 148), 1)

cv2.imshow("Result", new_img)
cv2.waitKey(0)


#/
#cap = cv2.VideoCapture('videos/Road.mp4')

#while True:
#    success, img = cap.read()

    # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
#    img = cv2.GaussianBlur(img, (9,9), 0)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#    img = cv2.Canny(img, 30, 30)

#    kernel = np.ones((5, 5), np.uint8)
#    img = cv2.dilate(img, kernel, iterations=1)

#    img = cv2.erode(img, kernel, iterations=1)

#    cv2.imshow('Result', img)

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break 

#/

#/ transformation picture 
##### - rotate



# img = cv2.flip(img, -1)
# cv2.imshow("Result", img)

# cv2.waitKey(0)


def rotate(img_param, angle):    
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)
    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (width, height))

# img = rotate(img, -90)

####### - smeschenize

def transform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param[0]))

# img = transform(img, 30, 200)

# cv2.imshow("Result", img)

# cv2.waitKey(0)


#/ Pobitoperation und mask 

img = np.zeros((350, 350), dtype='uint8')

circle = cv2.circle(img.copy(), (0, 0), 80, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(circle, square) # or // xor // not   

cv2.imshow("result", circle)


# // mask

photo = cv2.imread("img/image.JPG")
img = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=circle)
