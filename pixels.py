def pixels(pixel_range, width, height):
	outcome = (pixel_range ** 3) * width * height

class Rect:
	""" Comparing if multiple rectangles objects overlap """
	def __init__(self, x, y, w, h):
		self.x = float(x)
		self.y = float(y)
		self.w = float(w)
		self.h = float(h)