import numpy as np
from nummu import draw

class Rect:

    def init(self):
        self.size = 0

    def update(self, delta):
        self.size += delta
        if self.size >= 100:
            raise StopIteration

    def draw(self, pallete):
        pos = (100 - self.size) / 2
        draw.rect(pallete, pos, pos, self.size, self.size, color=(255, 255, 255))


def main():
    from nummu import Nummu
    nm = Nummu(100, 100)
    nm.extend(Rect())
    nm.export('rect.png', delay=4)


if __name__ == '__main__':
    main()


