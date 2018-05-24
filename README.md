# nummu

An animation image &amp; video maker.

NOTE: this project in WIP and thus interface might change a lot. Be cautious when using in production.

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
            pallete[:, self.position] = 1

Basic usage:

    # import nummu
    from nummu import Nummu

    # set file size
    nm = Nummu(100, 100)

    # extend nummu
    nm.extend(HelloWorld())

    # export to apng
    nm.export('helloworld.png', delay=5)

![helloworld](examples/helloworld.png)

Check the examples in project repo, and hopefully it might intrigue you some!

## Credit

Thanks numpy and numpngw! Nummu stands on the shoulder of these giants!
