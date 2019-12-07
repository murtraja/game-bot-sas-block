import time
import cv2
import numpy as np
from pymouse import PyMouse

import screen_grab

m = PyMouse()

def process(cnts):
    if len(cnts) <= 0:
        return
    ((x,y), radius) = cv2.minEnclosingCircle(cnts[0])
    x = round(x)
    y = round(y)
    s_x = screen_grab.top_left[0] + x
    s_y = screen_grab.top_left[1] + y
    m.move(s_x, s_y)

def main():
    # img = cv2.imread('s.png')
    img = screen_grab.grab_screen()
    while True:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        l = 3
        lower = (l, 0, 0)
        higher = (4, 255, 255)
        mask = cv2.inRange(hsv, lower, higher)#(0,0,210), (0,0,255))
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        process(cnts)
        time.sleep(0.5)
        # cv2.imshow('m', mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
if __name__ == '__main__':
    main()