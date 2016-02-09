def pixels(pixel_range, width, height):
	outcome = (pixel_range ** 3) * width * height

class Rect:
	""" Create and compare if two rectangle objects overlap """
	def __init__(self, x, y, w, h):
		# creates a rectangle 
		self.x = float(x) # top left point
		self.y = float(y) # bottom left point
		self.w = float(w) # top right point
		self.h = float(h) # bottom right point

def compare(r1, r2):
	# compares if two rectangles overlap
		if r1.x < r2.x + r2.w and r2.x < r1.x + r1.w and r1.y < r2.y + r2.h and r2.y < r1.y + r1.h:
			print("Collision Detected!")
		else:
			print("Whew, all clear, no collision detected.")

a = Rect(1, 1, 4, 2)
b = Rect(4, 2, 2, 5)
compare(a, b)

c = Rect(1, -3, 4, 2)
d = Rect(4, -6, 2, 4)
compare(c, d)

compare(a, c)
compare(b, d)
compare(a, a)



