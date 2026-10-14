"""
You are given an example of an inheritance hierarchy which results in Cartesian-product duplication.

Please refactor this hierarchy, giving the base class Shape  a constructor that takes an interface Renderer  defined as

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

        as well as VectorRenderer  and RasterRenderer  classes. Each inheritor of the Shape  abstract class should have a constructor that takes a Renderer  
such that, subsequently, each constructed object's __str__()  operates correctly, for example,

str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels" 

"""
from abc import ABC

# class Shape:
#     def __init__(self, render):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too
# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer

from abc import ABC, abstractmethod

class Renderer(ABC):
    
    @property
    @abstractmethod            
    def what_to_render_as(self):
        pass
        
class VectorRenderer(Renderer):
    @property    
    def what_to_render_as(self):
        return "lines"        

class RasterRenderer(Renderer):

    @property
    def what_to_render_as(self):
        return "pixels"

class Shape(ABC):
    def __init__(self, renderer: Renderer):        
        self.renderer = renderer
        self.name = None

    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"


class Triangle(Shape):
    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.name = 'Triangle'   

class Square(Shape):
    def __init__(self, render):
        super().__init__(render)
        self.name = 'Square'     


if __name__ == "__main__":
    raster_triangle = Triangle(RasterRenderer())
    vector_square = Square(VectorRenderer())

    print(raster_triangle)
    print(vector_square)


