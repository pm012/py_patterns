class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def draw_point(p):
    print('.', end='')
#^^ given point

class Line:
    def __init__(self,start, end) -> None:
        self.start = start
        self.end = end

class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))



class LineToPointAdapter():
    cache = {}

    def __init__(self, line):
        #self.h = hash(line) # incorrect hashing as objects are hashed incorrectly
        self.h = hash((line.start.x, line.start.y, line.end.x, line.end.y)) # tuple is immutable and can be perfectly hashed
        if self.h in self.cache:
            return 
        
       # super().__init__()       Incorrect as it just calls object, simply can be removed

        print(f'\nGenerating points for line '
              f'[{line.start.x}, {line.start.y}]->'
              f'[{line.end.x}, {line.end.y}]', end='')
        
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        points = []
        
        if right - left == 0:
            for y in range(top, bottom+1):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right+1):
                points.append(Point(x, top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])

def draw(rcs):
    print('\n *** Drawing some stuff ***')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)       
        print('\n !!! End Drawing !!!')

if __name__ == '__main__':

    print("@@@ Different rectangles @@@")
    rcs = [
        Rectangle(1,1,10,10),
        Rectangle(3,3,6,6)
    ]

    draw(rcs)
    draw(rcs)

    print("\n\n @@@ Same rectangles (worked incorrectly with caching objects) @@@")
    rcs = [
        Rectangle(3,3,16,16),
        Rectangle(3,3,16,16)
    ]
    
    draw(rcs)
    draw(rcs)
