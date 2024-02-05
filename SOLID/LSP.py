# LSP
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    def __str__(self):
        return f"width: {self.width}, height: {self.height}"

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value  # Breaks LIskow sabstitution principle

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


# To solve this we don't need a separate Square class and we can
# use factory to define if the rectangle is a square to resolve this issue
#

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
