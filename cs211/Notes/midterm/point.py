"""CIS 211 Midterm Question - solved incorrectly"""


class Point(object):
    """Point.x and Point.y are 'public' fields"""
    def __init__(self, x, y):
        self.listeners = []
        self.x = x
        self.y = y

    def add_listener(self, listener: "PointListener"):
        self.listeners.append(listener)

    def notify_all(self):
        for listener in self.listeners:
            listener.notify(self)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.notify_all()


class PointListener(object):
    """Complete Me"""
    '''Doesn't work:
    def notify(self):
        print("Point moved to {},{}".format(Point.x, Point.y))'''
    def notify(self, Point):
        print("Point moved to {},{}".format(Point.x, Point.y))


p = Point(5, 5)
p.add_listener(PointListener())
p.move(4, 3)  # Expected output: "Point moved to 9,8"
p.move(3, 2)  # Expected output: "Point moved to 12,10"
