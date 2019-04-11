# import the necessary packages
import numpy as np
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

cropped_1 = image[1292:2072, 599:1006].copy()
crop_1 = True
cropped_2 = image[1292:2072, 1147:1549].copy()

cropped_3 = image[1303:1363, 599:1006]
crop_2 = False
# cv2.imshow("cropped", cropped_1)

edges = cv2.Canny(cropped_2, 100, 200)

blurred = cv2.GaussianBlur(cropped_1, (11, 11), 10)
# crop_1 = True
im = normalize(cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY))

ret, im = cv2.threshold(im, 150, 255, cv2.THRESH_BINARY)

thresh = cv2.threshold(im, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# thresh = cv2.bitwise_not(thresh)

output = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)

stats = output[2]
labels = output[1]

answers = []
counts = []
count = 0

for i in stats:
    cv2.putText(cropped_1, str(count), (i[0], i[1] + i[3]), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, 255)

    if i[4]>=2550 and i[4]<= 2900:
        answers.append(i)

        counts.append(count)
        count += 1
    else:
        count += 1

print(counts)

# for a in answers:
#     print(a)

a = []
for i in range(len(answers)):
    if crop_1:
        if i % 2 == 0:
            if answers[i][0]>=235 and answers[i][0]<= 240:
                a.append('D')
            elif answers[i][0]>=3 and answers[i][0]<= 6:
                a.append('A')
            elif answers[i][0]>=80 and answers[i][0]<= 84:
                a.append('B')
            elif answers[i][0]>=159 and answers[i][0]<= 165:
                a.append('C')
        else:
            if answers[i][0]>=235 and answers[i][0]<= 240:
                a.append('J')
            elif answers[i][0]>=3 and answers[i][0]<= 6:
                a.append('F')
            elif answers[i][0]>=80 and answers[i][0]<= 84:
                a.append('G')
            elif answers[i][0]>=159 and answers[i][0]<= 165:
                a.append('H')
    elif crop_2:
        if i % 2 == 0:
            if answers[i][0]>=235 and answers[i][0]<= 240:
                a.append('J')
            elif answers[i][0]>=3 and answers[i][0]<= 6:
                a.append('F')
            elif answers[i][0]>=80 and answers[i][0]<= 84:
                a.append('G')
            elif answers[i][0]>=159 and answers[i][0]<= 165:
                a.append(('H'))
        else:
            if answers[i][0]>=235 and answers[i][0]<= 240:
                a.append('D')
            elif answers[i][0]>=3 and answers[i][0]<= 6:
                a.append('A')
            elif answers[i][0]>=80 and answers[i][0]<= 84:
                a.append('B')
            elif answers[i][0]>=159 and answers[i][0]<= 165:
                a.append('C')

print(a)


# print(len(answers))

cv2.imshow("original", cropped_1)
# cv2.imshow("img", im)
cv2.imshow("th", thresh)


cv2.waitKey(0)
