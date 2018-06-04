import numpy as np
from nummu import draw

class Line:

    def __init__(self):
        self.y1 = 0
        self.y2 = 100

    def update(self, delta):
        self.y1 += delta
        self.y2 -= delta
        if self.y1 >= 100 or self.y2 <= 0:
            raise StopIteration

    def draw(self, pallete):
        x1, y1, x2, y2 = 0, self.y1, 100, self.y2
        color = (255, 255, 255)
        draw.line(pallete, x1, y1, x2, y2, color=color)


def main():
    from nummu import Nummu
    nm = Nummu(100, 100)
    nm.extend(Line())
    nm.export('line.gif', delay=4)


if __name__ == '__main__':
    main()



