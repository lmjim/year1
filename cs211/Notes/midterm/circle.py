"""CIS 211 Midterm Question"""


class Circle(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def expand(self, factor):
        self.radius = self.radius * factor

    def __repr__(self):
        return "Circle({}, {}, {})".format(self.x, self.y, self.radius)

    def __str__(self):
        return repr(self)


def q1():
    c = Circle(5, 3, 15)
    c.expand(4)
    d = Circle(-1, -3, 4)
    d.move(15, 15)
    print("c: {}".format(c))
    print("d: {}".format(d))


q1()
