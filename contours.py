import numpy as np
import cv2

im = cv2.imread('/home/junaid/PycharmProjects/omr/img/scan_score.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# img = cv2.drawContours(imgray, contours, -1, (0,255,0), 3)

img = cv2.drawContours(im, contours, 3, (0,255,0), 3)


cv2.imshow('Image',im)
cv2.waitKey(0)



































# import cv2
# import numpy
#
# image = cv2.imread('/home/junaid/PycharmProjects/omr/img/q_sheet.JPEG')
#
# blurred = cv2.pyrMeanShiftFiltering(image, 31,91)
#
# gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
#
# ret, threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#
# contours,_ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#
# # print("Number of contours detected &d -> " % (len(contours)))
#
# cv2.drawContours(image,contours,1,(0,0,255),6)
#
# cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
#
# cv2.imshow('Display', image)
#
# cv2.waitKey()

#
# # Standard imports
# import cv2
# import numpy as np
#
# # Read image
# im = cv2.imread("/home/junaid/PycharmProjects/omr/img/export_black.png", cv2.IMREAD_GRAYSCALE)
#
# # Set up the detector with default parameters.
# detector = cv2.SimpleBlobDetector()
#
# # Detect blobs.
# # keypoints = detector.detect(im)
# keypoints = detector.detect(im)
# # Draw detected blobs as red circles.
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
# im_with_keypoints = cv2.drawContours(im, keypoints, np.array([]), (0, 0, 255),
#                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
# # Show keypoints
# cv2.imshow("Keypoints", im_with_keypoints)
# cv2.waitKey(0)