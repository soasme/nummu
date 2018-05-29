# nummu (南無)

An animated image maker.

NOTE: this project in WIP and thus interface might change a lot. Be cautious when using in production.

|Image|Script|
|-----|------|
|![helloworld](https://github.com/soasme/nummu/raw/master/examples/helloworld.png)|[examples/helloworld.py](examples/helloworld.py)|
|![line](https://github.com/soasme/nummu/raw/master/examples/line.gif)|[examples/line.py](examples/line.py)|
|![rect](https://github.com/soasme/nummu/raw/master/examples/rect.gif)|[examples/rect.py](examples/rect.py)|
|![bubblesort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/bubblesort.png) Bubble Sort<br> ![heapsort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/heapsort.png) Heap Sort<br> ![insertionsort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/insertionsort.png) Insertion Sort<br> ![mergesort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/mergesort.png) Merge Sort<br> ![quicksort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/quicksort.png) Merge Sort<br> ![selectionsort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/selectionsort.png) Selection Sort |[examples/sort.py](examples/sort.py)|

## Install

```
$ pip install nummu
```

## Usage

By extending Nummu, you might want to implement a class having these methods: `init()`, `update(delta)`, `draw(palette)`. None of them are absolutely required.

    class HelloWorld:

        def init(self):
            # Do initial work here
            self.position = 0

        def update(self, delta):
            # Do some calculation before draw each frame.
            # The delta is in millisecond unit.
            #
            # Don't forget to raise StopIteration somewhere!
            #
            self.position += delta
            if self.position >= 100:
                raise StopIteration

        def draw(self, pallete):
            # Pallete is simply a numpy.zeros instance.
            # Overwrite any pixels as you want.
            #
            pallete[:, self.position, :] = 255

Basic usage:

    # import nummu
    from nummu import Nummu

    # set file size
    nm = Nummu(100, 100)

    # extend nummu
    nm.extend(HelloWorld())

    # export to gif
    nm.export('helloworld.gif', delay=5)


Check the examples in project repo, and hopefully it might intrigue you some!

## Develop

```
$ poetry develop
$ poetry run python examples/helloworld.py
```

## Credit

Thanks Pillow, numpy, numpngw and array2gif! Nummu stands on the shoulder of these giants!
