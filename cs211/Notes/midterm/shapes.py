"""CIS 211 Midterm Question"""


class Shape(object):

    def area(self):
        raise NotImplementedError("area method must be implemented")

    def bigger(self, other):
        return self.area() > other.area()


class Rect(Shape):
    def __init__(self, llx, lly, urx, ury):
        self.llx = llx
        self.lly = lly
        self.urx = urx
        self.ury = ury

    def area(self):
        return (self.urx - self.llx) * (self.ury - self.lly)


class Square(Rect):
    def __init__(self, llx, lly, side):
        self.llx = llx
        self.lly = lly
        self.urx = llx + side
        self.ury = lly + side


def q3():
    r = Rect(5.0, 5.0, 7.0, 7.0)
    s = Square(1.0, 1.0, 3.0)
    if r.bigger(s):
        print("Rectangles always win! Bigness of {}".format(r.area()))
    elif s.bigger(r):
        print("Squares rule! Bigness of {}".format(s.area()))
    else:
        print("Apples versus oranges! You just can't know.")


q3()
