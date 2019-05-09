# import the necessary packages
from time import sleep

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


def normalize(im):
    return cv2.normalize(im, np.zeros(im.shape), 0, 255, norm_type=cv2.NORM_MINMAX)

def CvPy_2(image, even, odd, thresh_value, lower_bound):
    # edges = cv2.Canny(image, 100, 200)

    blurred = cv2.GaussianBlur(image, (11, 11), 10)
    # crop_1 = True
    im = normalize(cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY))

    ret, im = cv2.threshold(im, thresh_value, 255, cv2.THRESH_BINARY)

    thresh = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # thresh = cv2.bitwise_not(thresh)

    output = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)

    stats = output[2]
    labels = output[1]

    answers = []
    counts = []
    comp_list = []
    comp = []
    count = 1
    double = []

    for i in stats:

        if i[4] <= 3200:
            cv2.putText(image, str(count), (i[0], i[1] + i[3]), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, 255)
            # answers.append(i)
            comp_list.append(i)
            if count % 5 == 0:
                comp.append(comp_list)
                empty = True
                check_double = False
                for c in comp_list:
                    if c[4] >= lower_bound and c[4] <= 3200:
                        double.append(c)
                        # print(count, c)
                        empty = False
                # print(double)
                if len(double) >= 2 or empty == True:
                    answers.append([0])
                    check_double = True
                elif len(double) ==1 or empty == False:
                    answers.append(double[0])

                double = []
                comp_list = []
            counts.append(count)
            count += 1

    # for i in stats:
    #     cv2.putText(image, str(count), (i[0], i[1] + i[3]), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, 255)
    #
    #     if i[4] >= 2350 and i[4] <= 2900:
    #         print(count, i)
    #         answers.append(i)
    #
    #         counts.append(count)
    #         count += 1
    #     else:
    #         count += 1

    # print(counts)

    # for a in answers:
    #     print(a)

    a = []
    for i in range(len(answers)):
        if odd:
            if i % 2 == 0:
                if answers[i][0] >= 230 and answers[i][0] <= 250:
                    a.append('D')
                elif answers[i][0] >= 2 and answers[i][0] <= 15:
                    a.append('A')
                elif answers[i][0] >= 78 and answers[i][0] <= 90:
                    a.append('B')
                elif answers[i][0] >= 155 and answers[i][0] <= 170:
                    a.append('C')
                elif answers[i][0] >= 318 and answers[i][0] <= 335:
                    a.append('E')
                elif answers[i][0] == 0:
                    a.append('_')
            else:
                if answers[i][0] >= 230 and answers[i][0] <= 250:
                    a.append('J')
                elif answers[i][0] >= 2 and answers[i][0] <= 15:
                    a.append('F')
                elif answers[i][0] >= 78 and answers[i][0] <= 90:
                    a.append('G')
                elif answers[i][0] >= 155 and answers[i][0] <= 170:
                    a.append('H')
                elif answers[i][0] >= 318 and answers[i][0] <= 335:
                    a.append('K')
                elif answers[i][0] == 0:
                    a.append('_')

        elif even:
            if i % 2 == 0:
                if answers[i][0] >= 230 and answers[i][0] <= 250:
                    a.append('J')
                elif answers[i][0] >= 2 and answers[i][0] <= 15:
                    a.append('F')
                elif answers[i][0] >= 78 and answers[i][0] <= 90:
                    a.append('G')
                elif answers[i][0] >= 155 and answers[i][0] <= 170:
                    a.append(('H'))
                elif answers[i][0] >= 318 and answers[i][0] <= 335:
                    a.append('K')
                elif answers[i][0] == 0:
                    a.append('_')

            else:
                if answers[i][0] >= 230 and answers[i][0] <= 250:
                    a.append('D')
                elif answers[i][0] >= 2 and answers[i][0] <= 15:
                    a.append('A')
                elif answers[i][0] >= 78 and answers[i][0] <= 90:
                    a.append('B')
                elif answers[i][0] >= 155 and answers[i][0] <= 170:
                    a.append('C')
                elif answers[i][0] >= 318 and answers[i][0] <= 335:
                    a.append('E')
                elif answers[i][0] == 0:
                    a.append('_')

    # cv2.imshow("original", image)
    # # cv2.imshow("img", im)
    # cv2.imshow("th", thresh)
    # cv2.waitKey(0)

    return a

def CvPy(image, even, odd, thresh_value, lower_bound):
    # edges = cv2.Canny(image, 100, 200)

    blurred = cv2.GaussianBlur(image, (11, 11), 10)
    # crop_1 = True
    im = normalize(cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY))

    ret, im = cv2.threshold(im, thresh_value, 255, cv2.THRESH_BINARY)

    thresh = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # thresh = cv2.bitwise_not(thresh)

    output = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)

    stats = output[2]
    labels = output[1]

    answers = []
    counts = []
    comp_list = []
    comp = []
    double = []
    count = 1

    for i in stats:

        # print(count, i)

        if i[4] <= 8000:
            cv2.putText(image, str(count), (i[0], i[1] + i[3]), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, 255)
            # answers.append(i)
            comp_list.append(i)
            if count%4 == 0:
                comp.append(comp_list)
                empty = True
                check_double = False
                for c in comp_list:
                    if c[4] >= lower_bound and c[4] <= 8000:
                        double.append(c)
                        # print(count, c)
                        empty = False
                # print(double)
                if len(double) >= 2 or empty == True:
                    answers.append([0])
                    check_double = True
                elif len(double) ==1 or empty == False:
                    if double[0][4] > 5000:
                        answers.append([0])
                    else:
                        answers.append(double[0])

                double = []
                comp_list = []
            counts.append(count)
            count += 1

    # print(counts)
    # print(len(comp))
    # print(comp)
    # print(answers)
    cv2.imshow("original", image)
    # # # cv2.imshow("img", im)
    cv2.imshow("th", thresh)
    cv2.waitKey(0)

    # for a in answers:
    #     print(a)

    a = []
    for i in range(len(answers)):
        if odd:
            if i % 2 == 0:
                if answers[i][0] >= 230 and answers[i][0] <= 250:
                    a.append('D')
                elif answers[i][0] >= 2 and answers[i][0] <= 12:
                    a.append('A')
                elif answers[i][0] >= 78 and answers[i][0] <= 90:
                    a.append('B')
                elif answers[i][0] >= 155 and answers[i][0] <= 168:
                    a.append('C')
                elif answers[i][0] == 0:
                    a.append('_')
            else:
                if answers[i][0] >= 230 and answers[i][0] <= 250:
                    a.append('J')
                elif answers[i][0] >= 2 and answers[i][0] <= 12:
                    a.append('F')
                elif answers[i][0] >= 78 and answers[i][0] <= 90:
                    a.append('G')
                elif answers[i][0] >= 155 and answers[i][0] <= 168:
                    a.append('H')
                elif answers[i][0] == 0:
                    a.append('_')
        elif even:
            if i % 2 == 0:
                if answers[i][0] >= 230 and answers[i][0] <= 250:
                    a.append('J')
                elif answers[i][0] >= 2 and answers[i][0] <= 12:
                    a.append('F')
                elif answers[i][0] >= 78 and answers[i][0] <= 90:
                    a.append('G')
                elif answers[i][0] >= 155 and answers[i][0] <= 168:
                    a.append('H')
                elif answers[i][0] == 0:
                    a.append('_')
            else:
                if answers[i][0] >= 230 and answers[i][0] <= 250:
                    a.append('D')
                elif answers[i][0] >= 2 and answers[i][0] <= 12:
                    a.append('A')
                elif answers[i][0] >= 78 and answers[i][0] <= 90:
                    a.append('B')
                elif answers[i][0] >= 155 and answers[i][0] <= 168:
                    a.append('C')
                elif answers[i][0] == 0:
                    a.append('_')

    return a


def main():
    test_1_list = []
    test_2_list = []
    test_3_list = []
    test_4_list = []

    # load the image and show it
    image = cv2.imread("img/scan_score.jpg")
    sleep(5)

    # Test 1
    cropped_1 = image[1292:2072, 599:1006].copy() # ok
    test_1_list.append(CvPy(cropped_1, False, True, 150, 2550)) # ok
    cropped_2 = image[1292:2072, 1147:1549].copy() # ok
    test_1_list.append(CvPy(cropped_2, True, False, 150, 2550)) # ok
    cropped_3 = image[1292:2072, 1693:2095].copy() # ok
    test_1_list.append(CvPy(cropped_3, False, True, 150, 2550)) # ok
    cropped_4 = image[1292:2072, 2242:2642].copy() # ok
    test_1_list.append(CvPy(cropped_4, True, False, 150, 2550)) # ok
    cropped_5 = image[1292:2072, 2788:3196].copy() # ok
    test_1_list.append(CvPy(cropped_5, False, True, 150, 2550)) # ok
    cropped_6 = image[1292:2072, 3338:3737].copy() # ok
    test_1_list.append(CvPy(cropped_6, True, False, 150, 2550)) # ok

    # Test 2
    cropped_1 = image[2222:2837, 599:1006].copy() # ok
    test_2_list.append(CvPy_2(cropped_1, False, True, 130, 2250)) # ok
    cropped_2 = image[2222:2837, 1147:1549].copy() # ok
    test_2_list.append(CvPy_2(cropped_2, False, True, 130, 2250)) # ok
    cropped_3 = image[2222:2837, 1693:2095].copy() # ok
    test_2_list.append(CvPy_2(cropped_3, False, True, 130, 2250)) # ok
    cropped_4 = image[2222:2837, 2242:2642].copy() # ok
    test_2_list.append(CvPy_2(cropped_4, False, True, 130, 2250)) # ok
    cropped_5 = image[2222:2837, 2788:3196].copy() # ok
    test_2_list.append(CvPy_2(cropped_5, False, True, 130, 2250)) # ok
    cropped_6 = image[2222:2837, 3338:3737].copy() # ok
    test_2_list.append(CvPy_2(cropped_6, False, True, 130, 2250)) # ok
    #
    # # Test 3
    cropped_1 = image[2979:3411, 599:1006].copy() # ok
    test_3_list.append(CvPy(cropped_1, False, True, 140, 2350)) # ok
    cropped_2 = image[2979:3411, 1147:1549].copy() # ok
    test_3_list.append(CvPy(cropped_2, True, False, 140, 2350)) # ok
    cropped_3 = image[2979:3411, 1693:2095].copy() # ok
    test_3_list.append(CvPy(cropped_3, False, True, 140, 2350)) # ok
    cropped_4 = image[2979:3411, 2242:2642].copy() # ok
    test_3_list.append(CvPy(cropped_4, True, False, 140, 2350)) # ok
    cropped_5 = image[2979:3411, 2788:3196].copy() # ok
    test_3_list.append(CvPy(cropped_5, False, True, 140, 2350)) # ok
    cropped_6 = image[2979:3411, 3338:3737].copy() # ok
    test_3_list.append(CvPy(cropped_6, True, False, 120, 2250)) # ok
    # #
    # # # Test 4
    cropped_1 = image[3558:3984, 599:1006].copy() # ok
    test_4_list.append(CvPy(cropped_1, False, True, 140, 2350)) # ok
    cropped_2 = image[3558:3984, 1147:1549].copy() # ok
    test_4_list.append(CvPy(cropped_2, True, False, 140, 2350)) # ok
    cropped_3 = image[3558:3984, 1693:2095].copy() # ok
    test_4_list.append(CvPy(cropped_3, False, True, 140, 2350)) # ok
    cropped_4 = image[3558:3984, 2242:2642].copy() # ok
    test_4_list.append(CvPy(cropped_4, True, False, 140, 2350)) # ok
    cropped_5 = image[3558:3984, 2788:3196].copy() # ok
    test_4_list.append(CvPy(cropped_5, False, True, 140, 2350)) # ok
    cropped_6 = image[3558:3984, 3338:3737].copy() # ok
    test_4_list.append(CvPy(cropped_6, True, False, 140, 2350)) # ok
    #
    #
    test_dict ={ }

    test_dict['test_1'] = test_1_list
    test_dict['test_2'] = test_2_list
    test_dict['test_3'] = test_3_list
    test_dict['test_4'] = test_4_list

    print(test_dict)

if __name__ == '__main__':
    main()

