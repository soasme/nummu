import numpy as np
from nummu import draw

class Ghost:

    def init(self):
        self.seq = 0
        self.total = 4

    def update(self, delta):
        self.seq = self.seq + 1
        if self.seq > self.total:
            raise StopIteration

    def draw(self, pallete):
        draw.image(pallete, 0, 0, f'./ghost-0{self.seq}.png')


def main():
    from nummu import Nummu
    nm = Nummu(32, 32)
    nm.extend(Ghost())
    nm.export('ghost.gif', delay=2)


if __name__ == '__main__':
    main()



