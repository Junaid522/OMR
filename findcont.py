import numpy as np
import cv2

im = cv2.imread('img/scan_score.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[4]
cv2.drawContours(im, [cnt], 0, (0, 255, 0), 3)
cv2.imshow("im", im)
cv2.waitKey(0)