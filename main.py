import cv2
import numpy as np
import time

import screen_grab, process

def get_screen():
	img = screen_grab.grab_screen()
	img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
	return img

def show_screen(img):
	cv2.imshow('1', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def save_screen():
	img = get_screen()
	cv2.imwrite('s.png', img)

def main():
	while True:
			img = get_screen()
			process.process(img)
			time.sleep(0.2)


if __name__ == '__main__':
	main()