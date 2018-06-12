# nummu (南無)

An animated image maker.

NOTE: this project in WIP and thus interface might change a lot. Be cautious when using in production.

|Image|Script|
|-----|------|
|![helloworld](https://github.com/soasme/nummu/raw/master/examples/helloworld.png)|[examples/helloworld.py](examples/helloworld.py)|
|![line](https://github.com/soasme/nummu/raw/master/examples/line.gif)|[examples/line.py](examples/line.py)|
|![rect](https://github.com/soasme/nummu/raw/master/examples/rect.gif)|[examples/rect.py](examples/rect.py)|
|![bubblesort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/bubblesort.png) Bubble Sort<br> ![heapsort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/heapsort.png) Heap Sort<br> ![insertionsort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/insertionsort.png) Insertion Sort<br> ![mergesort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/mergesort.png) Merge Sort<br> ![quicksort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/quicksort.png) Quick Sort<br> ![selectionsort](https://gist.github.com/soasme/e3f1a210cc7e7750d304cb43b6aaad23/raw/d6e5687ce8492bd5865f4d7f38a5ec421c5d4c1b/selectionsort.png) Selection Sort |[examples/sort.py](examples/sort.py)|
|![image](https://github.com/soasme/nummu/raw/master/examples/ghost.gif)|[examples/image.py](examples/image.py)|
|![text](https://github.com/soasme/nummu/raw/master/examples/text.gif)|[examples/text.py](examples/text.py)|


## Install

```
$ pip install nummu
```

## Usage

Nummu is simply a framework so you might want to implement a class having these methods: `update(delta)`, `draw(palette)`. None of them are absolutely required.

    class HelloWorld:

        def __init__(self):
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

    # add drawer defined previously
    nm.add(HelloWorld())

    # export to gif
    nm.export('helloworld.gif', delay=5)


Check the examples in project repo, and hopefully it might help you!

## Develop

```
$ poetry develop
$ poetry run python examples/helloworld.py
```

## Test

Currently nummu support running on 3.6, 3.7

```
$ pyenv install 3.6.5
$ pyenv install 3.7.0b2
$ pyenv local 3.6.5 3.7.0b2
$ export PATH=$(pyenv root)/shims:$PATH
$ tox
py36 runtests: commands[0] | poetry develop
py36 runtests: commands[0] | poetry run pytest
py37 runtests: commands[0] | poetry develop
py37 runtests: commands[0] | poetry run pytest
  py36: commands succeeded
  py37: commands succeeded
  congratulations :)
```

## Credit

Thanks Pillow, numpy, numpngw and array2gif! Nummu stands on the shoulder of these giants!
