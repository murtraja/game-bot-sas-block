import cv2
import numpy as np
from pymouse import PyMouse

import screen_grab

char_radius = 75

def imshowbgr(name, img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow(name, hsv_img)

def main():
    img = cv2.imread('s.png')
    # cv2.imshow('s', img)

    # c1 = round(img.shape[0]/2)
    # c2 = round(img.shape[1]/2)
    # img_center = img[c1-char_radius:c1+char_radius, c2-char_radius:c2+char_radius, ...]
    # cv2.imshow('c', img_center)

    blurred = cv2.GaussianBlur(img, (11, 11), 0)
    # cv2.imshow('d', blurred)

    lower = (175, 50, 50)
    higher = (180, 255, 255)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # imshowbgr('hsv', hsv)


    # # Find a mask using the lower and higher bounds
    mask = cv2.inRange(hsv, lower, higher)
    # for d1 in mask:
    #     for d2 in d1:
    #         if d2 > 0:
    #             print("found", d2)
    # cv2.imshow('inRange', mask)
    mask = cv2.erode(mask, None, iterations=2)
    # cv2.imshow('erode', mask)
    mask = cv2.dilate(mask, None, iterations=2)
    # cv2.imshow('dilate', mask)

    # # Find contours
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # print(len(cnts))
    ((x,y), rad) = cv2.minEnclosingCircle(cnts[0])
    x = round(x)
    y = round(y)
    s_x = screen_grab.top_left[0] + x
    s_y = screen_grab.top_left[1] + y
    m = PyMouse()
    m.move(s_x, s_y)
    # print (x,y,rad)
    # circled = cv2.circle(mask, (round(x), round(y)), round(rad)+20, 255)
    # cv2.imshow('cir', circled)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()