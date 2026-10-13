# To run tests execute: python -m pytest -v

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self._height = height
        self._width = width

    def __str__(self):
        return f"width: {self.width}, height: {self.height}, area: {self.area}"

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


class Square(Shape):
    def __init__(self, size):
        self._size = size

    def __str__(self):
        return f"size: {self.size}, area: {self.area}"

    @property
    def size(self):
        return self._size

    def area(self):
        return self._size ** 2

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def __str__(self):
        return f"radius: {self.radius}, area: {self.area}"

    @property
    def radius(self):
        return self._radius

    def area(self):
        import math
        return math.pi * (self._radius ** 2)

class ShapeFactory:
    @staticmethod
    def create_rectangle(width, height):
        return Rectangle(width, height)

    @staticmethod
    def create_circle(radius):
        return Circle(radius)

    @staticmethod
    def create_square(size):
        return Square(size)
