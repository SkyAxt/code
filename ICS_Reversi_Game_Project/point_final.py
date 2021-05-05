import math

class Point:
    def __init__(self, frac_x, frac_y):
        self._frac_x = frac_x
        self._frac_y = frac_y

    def frac(self):
        return (self._frac_x, self._frac_y)

    def pixel(self, width, height):
        return (int(self._frac_x *width), int(self._frac_y*height))

    def frac_distance_from(self, p):
        return math.sqrt((self._frac_x - p.frac_x) * (self._frac_x - p._frac_x)
            + (self._frac_y - p._frac_y) * (self._frac_y - p._frac_y))

def from_frac(frac_x, frac_y):
    return Point(frac_x, frac_y)

def from_pixel(pixel_x, pixel_y, width, height):
    return Point(pixel_x/width, pixel_y/height)
