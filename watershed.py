import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/scan_score.jpg')
cropped_1 = img[1292:2072, 599:1006].copy()
cropped_2 = img[1292:2072, 1147:1549].copy()

gray = cv2.cvtColor(cropped_1, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)

sure_bg = cv2.dilate(opening, kernel, iterations=3)

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# cv2.imshow('DT',dist_transform)
# cv2.imshow('TH', thresh)

ret, markers = cv2.connectedComponents(sure_fg)

markers = markers + 1

markers[unknown==255] = 0

markers = cv2.watershed(cropped_1, markers)
cropped_1[markers == -1] = [0,255,0]

print(ret)

cv2.imshow('TH', cropped_1)

cv2.waitKey(0)