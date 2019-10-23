import cv2
import numpy as np

import screen_grab

def get_screen():
	img = screen_grab.grab_screen()
	img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
	return img

def show_screen(img):
	cv2.imshow('1', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def main():
	img = get_screen()
	cv2.imwrite('s.png', img)

if __name__ == '__main__':
	main()