"""Personal Practice for Midterm"""


class Dessert(object):
    pass


class Chocolately(Dessert):
    def __init__(self, name, density):
        self.name = name
        self.density = density


class Vanilla(Dessert):
    def __init__(self, name, sweetness):
        self.name = name
        self.sweetness = sweetness


