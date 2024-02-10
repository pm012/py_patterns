from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    class PointFactory:

        def new_cartesian_point(self, x, y):
            p = Point()
            p.x = x
            p.y = y
            return p

        def new_polar_point(self, rho, theta):
            p = Point()
            p.x = rho * cos(theta)
            p.y = rho * sin(theta)
            return p


if __name__ == '__main__':
    p = Point().PointFactory.new_polar_point(1,2)
    p2 = Point().PointFactory.new_cartesian_point(2,3)
    print(p2)
    print(p)
