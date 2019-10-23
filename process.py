import cv2
import numpy as np
from pymouse import PyMouse

import screen_grab

char_radius = 75
m = PyMouse()

def imshowbgr(name, img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow(name, hsv_img)

def process(img):
    blurred = cv2.GaussianBlur(img, (11, 11), 0)

    lower = (175, 50, 50)
    higher = (180, 255, 255)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # # Find a mask using the lower and higher bounds
    mask = cv2.inRange(hsv, lower, higher)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # # Find contours
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # print(len(cnts))
    if len(cnts) <= 0:
        return

    ((x,y), rad) = cv2.minEnclosingCircle(cnts[0])
    x = round(x)
    y = round(y)
    s_x = screen_grab.top_left[0] + x
    s_y = screen_grab.top_left[1] + y
    m.move(s_x, s_y)

def main():
    img = cv2.imread('s.png')
    process(img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()