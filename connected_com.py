from time import sleep

import cv2
import numpy as np


def normalize(im):
    return cv2.normalize(im, np.zeros(im.shape), 0, 255, norm_type=cv2.NORM_MINMAX)

image = cv2.imread("img/scan_score.jpg")

cropped_1 = image[2702:2757, 517:1006].copy()

im = normalize(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))



ret, thresh = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)

cv2.imshow("thresh", thresh)

connectivity = 8

output = cv2.connectedComponents(thresh, connectivity, cv2.CV_32S)

# num_lables = output[0]
#
# lables = output[1]
#
# stats = output[2]
#
# centroids = output[3]

print(output)