class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()

def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done draw image')


if __name__ == '__main__':
    #bmp = Bitmap('facepalm.jpg')
    bmp = LazyBitmap('facepalm.jpg')
    draw_image(bmp)
    draw_image(bmp) #loading is done only once we work with existing instance of Bitmap