import point_final
class Model:
    def __init__(self,top_left, bottom_right, width, height, x,y):
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._minimum_x, self._minimum_y = self._top_left.frac()
        self._maximum_x, self._maximum_y = self._bottom_right.frac()
        self._width = width
        self._height = height
        self._x = x + 1
        self._y = y + 1
    def position(self, x,y):
        '''returns true if the move is correctly inside of the square'''
        return(
            self._minimum_x *self._width < x < self._maximum_x * self._width
            and self._minimum_y *self._height < y < self._maximum_y * self._height)
    def attempt_move(self):
        return self._x, self._y
