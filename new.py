import cv2
import imutils
import matplotlib
import notebook as notebook
import numpy as np
import matplotlib.pyplot as plt


import matplotlib.image as mpimg


# %matplotlib notebook

# img = cv2.imread('img/scan_score.jpg')

def normalize(im):
    return cv2.normalize(im, np.zeros(im.shape), 0, 255, norm_type=cv2.NORM_MINMAX)

# load the image and show it
image = cv2.imread("img/scan_score.jpg")

cropped_1 = image[2702:2757, 517:1006].copy()
# cv2.imshow("cropped", cropped_1)

edges = cv2.Canny(cropped_1, 100, 200)


blurred = cv2.GaussianBlur(cropped_1, (11, 11), 10)

im = normalize(cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY))

ret, im = cv2.threshold(im, 155, 255, cv2.THRESH_BINARY)

thresh = cv2.threshold(im, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cnts = imutils.grab_contours(cnts)


# image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# contours,_ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print('No of shapes {0}'.format(len(cnts)))
area = 0.0
perimeter = 0.0
center = 0.0
cx= 0
cy = 0

for cnt in cnts:
    # rect = cv2.minAreaRect(cnt)
    # box = cv2.boxPoints(rect)
    # box = np.int0(box)

    # epsilon = 0.01* cv2.arcLength(cnt, True)
    # approx = cv2.approxPolyDP(cnt, epsilon, True)
    #
    # img = cv2.drawContours(thresh, [approx], 0, (0,0,255), 5)

    M = cv2.moments(cnt)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    center = (cx, cy)

    area = cv2.contourArea(cnt)

    perimeter = cv2.arcLength(cnt, True)

    print("Area: ", area)
    print("P: ", perimeter)


cv2.putText(thresh, "A:{0:2.1f}".format(area), center,
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.3,(255,0,0),3)

cv2.putText(thresh, "P:{0:2.1f}".format(perimeter), (cx, cy + 30),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.3,(255,0,0),3)

plt.figure("Example 1")
plt.imshow(thresh)
plt.title('Binary contours in an image')
plt.show()