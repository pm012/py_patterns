"""You are given a class called Square and a function calculate_area() which calculates the area
 of a given rectangle.
In order to use Square in calculate_area, instead of augmenting it with width/height members, 
please implement the SquareToRectangleAdapter class. 
This adapter takes a square and adapts it in such a way that it can be used as an argument to calculate_area().
"""

class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:    
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side
    
    @property
    def height(self):
        return self.square.side
        
        
            
        

sq = Square(11)
rec = SquareToRectangleAdapter(sq)
print(calculate_area(rec))
sq.side = 10
print(calculate_area(rec))
        