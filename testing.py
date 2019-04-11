import numpy as np
import cv2

def normalize(im):
    return cv2.normalize(im, np.zeros(im.shape), 0, 255, norm_type=cv2.NORM_MINMAX)

# load the image and show it
image = cv2.imread("img/scan_score.jpg")

cropped_1 = image[1292:2072, 599:1006].copy()
cropped_2 = image[1292:2072, 1147:1549].copy()
cropped_3 = image[1292:2072, 1693:2095].copy()
cropped_4 = image[1292:2072, 2242:2642].copy()
cropped_5 = image[1292:2072, 2788:3196].copy()
cropped_6 = image[1292:2072, 3383:3737].copy()


edges = cv2.Canny(image, 100, 200)

blurred = cv2.GaussianBlur(image, (11, 11), 10)
# crop_1 = True
im = normalize(cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY))

ret, im = cv2.threshold(im, 150, 255, cv2.THRESH_BINARY)

thresh = cv2.threshold(im, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# thresh = cv2.bitwise_not(thresh)

output = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)

stats = output[2]
lines = []
# print(len(stats))
count = 0
for i in stats:
    # if i[4]>=64600 and i[4]<=70100:
    cv2.putText(image, str(count), (i[0], i[1] + i[3]), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, 255)
        # lines.append(i)
    count += 1


# for l in lines:
#     print(l)
cv2.imshow("original", image)
# cv2.imshow("img", im)
cv2.imshow("th", thresh)


cv2.waitKey(0)