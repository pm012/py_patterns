class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def draw_point(p):
    print('.', end='')

class Line:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))

class LineToPointAdapter(list):
    count = 0  # Static field (shared for all instances)

    def __init__(self, line):
        super().__init__()
        LineToPointAdapter.count += 1  # Increising static counter

        print(f'\n[{LineToPointAdapter.count}] Generating points for line '
              f'[{line.start.x}, {line.start.y}]->'
              f'[{line.end.x}, {line.end.y}]: ', end='')
        
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y) 

        # Vertical line (X identical)
        if right - left == 0:
            for y in range(top, bottom + 1):
                self.append(Point(left, y))
        # Horizontal line (Y everywhere is the same)
        elif line.end.y - line.start.y == 0:
            for x in range(left, right + 1):
                self.append(Point(x, top))

def draw(rcs):
    print('\n\n--- Start Drawing ---')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
    print('\n--- End Drawing ---')

if __name__ == '__main__':
    rcs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    # Call drawing twice, to see work without chaching
    draw(rcs)
    draw(rcs)
