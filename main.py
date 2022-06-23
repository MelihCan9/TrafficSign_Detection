import cv2
import numpy as np


def red_detect(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Specify 2 lower and upper bound for red color in hsv color model. Bounds includes hue, saturation, value range.
    lbound1 = np.array([0, 73, 104])
    ubound1 = np.array([7, 255, 255])

    lbound2 = np.array([139, 73, 104])
    ubound2 = np.array([180, 255, 255])

    # Two masks for two seperate bounds.
    mask = cv2.inRange(hsv, lbound1, ubound1)
    mask2 = cv2.inRange(hsv, lbound2, ubound2)

    # Combining the masks.
    full_mask = mask + mask2

    # cv2.imshow("red_mask", full_mask)
    # cv2.waitKey(0)
    return full_mask


def detect_blue(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lbound = np.array([105, 158, 83])
    ubound = np.array([120, 255, 255])

    mask = cv2.inRange(hsv, lbound, ubound)

    # cv2.imshow("blue_mask", mask)
    # cv2.waitKey(0)

    return mask


def area_filter(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 810:  # 740

            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif area > 288:
            kernel = np.ones((5, 5), dtype=np.uint8)
            result2 = cv2.dilate(img, kernel, iterations=1)
            contours1, hierarchy = cv2.findContours(result2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            for cnt1 in contours1:
                area1 = cv2.contourArea(cnt1)
                if area1 > 460:
                    peri = cv2.arcLength(cnt1, True)

                    approx = cv2.approxPolyDP(cnt1, 0.02 * peri, True)
                    x, y, w, h = cv2.boundingRect(approx)
                    cv2.rectangle(imgContour, (x, y), (x + w, y + h), (135, 65, 135), 2)


img = cv2.imread('BIM472_Image01.jpg')

imgContour = img.copy()
red = red_detect(img)
blue = detect_blue(img)

full = red + blue
area_filter(full)
cv2.imshow("Result", imgContour)
cv2.waitKey(0)


