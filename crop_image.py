# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

#
# ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1, 5: 2, 6: 2, 7: 3, 8: 1, 9: 4, 10: 2,
#               11: 1, 12: 4, 13: 0, 14: 3, 15: 1,16: 2, 17: 2, 18: 3, 19: 1, 20: 4,
#               21: 1, 22: 4, 23: 0, 24: 3, 25: 1, 26: 2, 27: 2, 28: 3, 29: 1, 30: 4,
#               31: 1, 32: 4, 33: 0, 34: 3, 35: 1, 36: 2, 37: 2, 38: 3, 39: 1, 40: 4,
#               41: 1, 42: 4, 43: 0, 44: 3, 45: 1, 46: 2, 47: 2, 48: 3, 49: 1, 50: 4,
#               51: 1, 52: 4, 53: 0, 54: 3, 55: 1, 56: 2, 57: 2, 58: 3, 59: 1, 60: 4,
#               61: 1, 62: 4, 63: 0, 64: 3, 65: 1, 66: 2, 67: 2, 68: 3, 69: 1, 70: 4,
#               71: 1, 72: 4, 73: 0, 74: 3}

ANSWER_KEY = { 0: 1,
               1: 1,
               2: 1,
               3: 2,
               4: 1,
               5: 1,
               6: 2,
               7: 1,
               8: 2,
               9: 1,
               10: 1,
               11: 2,
               12: 1 }

def normalize(im):
    return cv2.normalize(im, np.zeros(im.shape), 0, 255, norm_type=cv2.NORM_MINMAX)

# load the image and show it
image = cv2.imread("img/scan_score.jpg")

cropped_1 = image[1278:2082, 599:1006].copy()
cv2.imshow("cropped", cropped_1)

edges = cv2.Canny(cropped_1, 100, 200)

blurred = cv2.GaussianBlur(cropped_1, (11, 11), 10)

im = normalize(cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY))

ret, im = cv2.threshold(im, 155, 255, cv2.THRESH_BINARY)

thresh = cv2.threshold(im, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cnts = imutils.grab_contours(cnts)

# print(cnts)
cv2.imshow('thresh', thresh)
questionCnts = []

for c in cnts:

    # ellipse = cv2.fitEllipse(c)
    # print(cv2.ellipse(thresh, ellipse, (0, 0,255), 2))
    # (x,y),radius = cv2.minEnclosingCircle(c)
    # center = (int(x), int(y))
    # radius = int(radius)
    # points.append(cv2.circle(cropped_1, center,radius,(0,255,0),2))
    # rect = cv2.minAreaRect(c)
    # box = cv2.boxPoints(rect)
    # box = np.int0(box)
    # points.append(cv2.drawContours(cropped_1, [box],0,(0,0,255),2))

    # perimeter.append(cv2.arcLength(c, True))
    perimeter = cv2.arcLength(c, True)
    # print(perimeter)

    ar = cv2.contourArea(c)
    cv2.drawContours(thresh, c, -1,(255,0,0),3)
    if perimeter>=70 and perimeter<= 71:
        questionCnts.append(c)
    # if h >= 42 or h <= 44 and w>=56 or w <= 59 and ar>=1.4 and ar<=1.5:
    #     questionCnts.append(c)

# print(points)
# print(len(perimeter))
# print(len(cnts))
print(len(questionCnts))

# print(len(perimeter))
# print(perimeter)

questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
# print(questionCnts)

# print(cv2.moments(questionCnts[0]))
correct = 0
#
for (q,i) in enumerate(np.arange(0, len(questionCnts), 4)):
    cnts = contours.sort_contours(questionCnts[i:i + 4])[0]
    bubbled = None
    # print(cnts)

    for (j, c) in enumerate(cnts):
        mask = np.zeros(thresh.shape, dtype="uint8")
        # print(mask)
        cv2.drawContours(mask, [c], -1, (255,0,0), 1)

        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        total = cv2.countNonZero(mask)

        if bubbled is None or total > bubbled[0]:
            bubbled = (total, j)

        color = (0, 0, 255)
        k = 0

        if k == bubbled[1]:
            color = (0, 255, 0)
            correct += 1
            print("correct", int(j))

            cv2.drawContours(thresh, [cnts[k]], -1, color, 3)
        # cv2.imshow("t", thresh)

#
# # grab the test taker
score = (correct / 13.0) * 100
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(im, "{:.2f}%".format(score), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
# # cv2.imshow("Original", image)
# cv2.imshow("Exam", im)

cv2.waitKey(0)
