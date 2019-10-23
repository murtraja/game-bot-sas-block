from pymouse import PyMouseEvent
import pyscreenshot as ImageGrab
import numpy as np

top_left = [13, 143]
bottom_right = [816, 746]

class Capture(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
        self.top_left = []
        self.bottom_right = []

    def click(self, x, y, button, press):
        if button == 1:
            if press:
            	print("button press", x, y)
            	if not self.top_left:
            		self.top_left = [x, y]
            		print("top left stored")
            	elif not self.bottom_right:
            		self.bottom_right = [x, y]
            		print("bottom right stored")
            	else:
            		self.stop()
            		print("stop")
        else:  # Exit if any other mouse button used
            self.stop()

def get_bound_cords():
	c = Capture()
	c.run()
	print(c.top_left)
	print(c.bottom_right)

def grab_screen():
    im = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))  # X1,Y1,X2,Y2
    return np.array(im)


if __name__ == '__main__':
	main()