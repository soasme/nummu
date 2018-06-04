from random import randint
import numpy as np
from nummu import Nummu


class HelloWorld:

    def __init__(self):
        self.position = 0

    def update(self, delta):
        self.position += delta
        if self.position >= 100:
            raise StopIteration

    def draw(self, pallete):
        pallete[:, self.position, 0] = randint(0, 255)
        pallete[:, self.position, 1] = randint(0, 255)
        pallete[:, self.position, 2] = randint(0, 255)


def main():
    nm = Nummu(100, 100)
    nm.extend(HelloWorld())
    nm.export('helloworld.png', delay=4)


if __name__ == '__main__':
    main()

