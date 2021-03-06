import numpy as np
from nummu import draw

class Rect:

    def init(self):
        self.size = 0
        self.pos = 50

    def update(self, delta):
        self.size += delta
        self.pos = (100 - self.size) / 2
        if self.size >= 100:
            raise StopIteration

    def draw(self, pallete):
        x, y, w, h = self.pos, self.pos, self.size, self.size
        color = (255, 255, 255)
        draw.rect(pallete, x, y, w, h, color=color)


def main():
    from nummu import Nummu
    nm = Nummu(100, 100)
    nm.add(Rect())
    nm.export('rect.gif', delay=4)


if __name__ == '__main__':
    main()


