import numpy as np

class HelloWorld:

    def __init__(self):
        self.position = 0

    def update(self, delta):
        self.position += delta
        if self.position >= 100:
            raise StopIteration

    def draw(self, pallete):
        pallete[:, self.position, :] = 255


def main():
    from nummu import Nummu
    nm = Nummu(100, 100)
    nm.add(HelloWorld())
    nm.export('helloworld.gif', delay=5)


if __name__ == '__main__':
    main()

