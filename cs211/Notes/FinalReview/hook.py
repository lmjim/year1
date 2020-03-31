"""Inferring hook usage from Python source"""


class Fruit(object):
    """This is an abstract superclass"""
    def __init__(self):
        raise NotImplementedError("Each concrete subclass must instantiate its own constructor")

    def describe(self, name: str):
        print("{} is very {}".format(name, self._qual()))


class Apple(Fruit):
    """Concrete subclass"""
    def __init__(self, variety: str, quality: str):
        self.variety = variety
        self.quality = quality

    def announce(self):
        self.describe(self.variety)

    def _qual(self):
        return self.quality


def main():
    gala = Apple("Gala", "sweet")
    braeburn = Apple("Braeburn", "crunchy")

    gala.announce()
    braeburn.announce()


main()
#Expected output:
#Gala is very sweet
#Braeburn is very crunchy