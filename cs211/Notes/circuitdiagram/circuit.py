"""
Circuit diagram with graphics
--- in class coding exercise
"""

import graphics.graphics as g

WINDOW = None


def make_window(width=400, height=400) -> g.GraphWin:
    return g.GraphWin("Sample", width, height)


class AndGate(object):
    """The model part of an AndGate"""
    pass

class VisibleAndGate(AndGate):
    """ and AndGate with graphics"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        """Place an and-gate on the diagram at x,y"""
        p = g.Point(self.x, self.y)
        self.image = g.Image(p, "images/and_gate.gif")
        self.image.draw(WINDOW)
        return self

    def width(self):
        return self.image.getWidth()

    def height(self):
        return self.image.getHeight()

    def connect(self, other, connection=1):
        output = g.Point(self.x + 0.5*self.width(), self.y)
        inport = g.Point(other.x - 0.5*self.width(), other.y - 0.5*self.height() + 0.33 * connection * self.height())
        wire = g.Line(output, inport)
        wire.draw(WINDOW)


def and_gate(x,y):
    """Place an and-gate on the diagram at x,y"""
    p = g.Point(x, y)
    image = g.Image(p, 'images/and_gate.gif')
    image.draw(WINDOW)
    return image


"""
def main():
    global WINDOW
    WINDOW = make_window(600,600)
    gate = and_gate(100, 100)
    gate2 = and_gate(200, 200)
    # corner = g.Rectangle(
        # g.Point(100, 100),
        # g.Point(200,200))
    # corner.draw(WINDOW)
    gate_width = gate.getWidth()
    wire = g.Line(g.Point(100+(0.5*gate_width), 100),
                  g.Point(g.Point(200 - (0.5*gate_width), 200)))
    print(gate_width)
    input("Press enter to close")
    WINDOW.close()
"""


def main():
    global WINDOW
    WINDOW = make_window(600,600)
    gate = VisibleAndGate(100, 100)
    gate.draw()
    gate2 = VisibleAndGate(400, 400)
    gate2.draw()
    # corner = g.Rectangle(
        # g.Point(100, 100),
        # g.Point(200,200))
    # corner.draw(WINDOW)
    # gate_width = gate.getWidth()
    #wire = g.Line(g.Point(100+(0.5*gate_width), 100),
    #              g.Point(g.Point(200 - (0.5*gate_width), 200)))
    gate.connect(gate2)
    # print(gate_width)
    input("Press enter to close")
    WINDOW.close()


if __name__ == '__main__':
    main()