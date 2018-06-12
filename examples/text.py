import string
import numpy as np
from nummu import draw

class Text:

    def __init__(self):
        self.pos = 0
        self.chars = string.ascii_uppercase
        self.char = ''

    def update(self, delta):
        if self.pos >= len(self.chars):
            raise StopIteration
        self.char = self.chars[self.pos]
        self.pos += 1


    def draw(self, pallete):
        draw.text(pallete, 0, 0, text=self.char,
                font='./examples/OpenSans-Regular.ttf',
                size=50,
                color=(100, 179, 248))


def main():
    from nummu import Nummu
    nm = Nummu(100, 100)
    nm.add(Text())
    nm.export('text.gif', delay=4)


if __name__ == '__main__':
    main()
