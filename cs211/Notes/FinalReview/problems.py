from typing import List
from typing import Tuple

"""Problem 1"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "Interval({},{})".format(self.start, self.end)

    def __str__(self):
        return self.__repr__()

    def slide(self, delta):
        self.start += delta
        self.end += delta

    def scale(self, factor):
        self.end = self.start + factor * (self.end - self.start)


from_zero = Interval(0,1)
from_one = Interval(1,2)
from_zero.slide(10)
from_zero.scale(10)
from_one.slide(8)
print(from_zero)
print(from_one)


"""Problem 2"""
class Listener(object):
    def notify(self, event):
        raise NotImplementedError


class Listenable(object):
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def notify_all(self, event):
        for listener in self.listeners:
            listener.notify(event)


class SillyWalk(Listenable):
    def __init__(self, steps):
        super().__init__()
        self.steps = steps

    def walk(self):
        for step in self.steps:
            self.notify_all({"step": step})


class StepWatcher(Listener):
    def __init__(self):
        self.count = 0

    def notify(self, event):
        self.count += 1
        print("Step {}: {}".format(self.count, event["step"]))


silly = SillyWalk(["kick", "wiggle", "swing"])
silly.add_listener(StepWatcher())
silly.walk()


"""Problem 3"""
def pack (a: int, b: int, c:int):
    word = (a & 3) << 6 | (b & 7) << 3 | (c & 7)
    return word


def unpack(word) -> Tuple:
    a = (word >> 6) & 3
    b = (word >> 3) & 7
    c = word & 7
    return (a, b, c)


w1 = pack(3, 7, 7)
print(unpack(w1))
w2 = pack(1, 1, 1)
print(unpack(w2))


"""Problem 4"""
class Seg(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def length(self):
        return self.high - self.low

    def __str__(self):
        return "Seg({},{})".format(self.low, self.high)


class Comparison(object):
    def compare(self, s1: Seg, s2: Seg) -> bool:
        raise NotImplementedError("override")


class Longer(Comparison):
    def compare(self, s1: Seg, s2: Seg) -> bool:
        return s1.length() > s2.length()


class SegList():
    def __init__(self, segs: List[Seg]):
        assert len(segs) > 0, "segs must not be empty"
        self._contents = segs

    def maximal(self, comparison):
        max_seg = self._contents[0]
        for seg in self._contents:
            if comparison.compare(seg, max_seg):
                max_seg = seg
        return max_seg


segs = SegList([Seg(3, 4), Seg(1, 10), Seg(1, 2), Seg(4, 6)])
print(segs.maximal(Longer()))  # Expected: Seg(1,10)


"""Problem 5"""
class Area(object):
    def __init__(self, name):
        self.name = name

    def population(self):
        raise NotImplementedError("Override")


class Place(Area):
    def __init__(self, name, pop):
        self.pop = pop
        super().__init__(name)

    def population(self) -> int:
        return self.pop


class Region(Area):
    def __init__(self, name, subregions: List[Area]):
        super().__init__(name)
        self.subregions = subregions

    def population(self) -> int:
        pop = 0
        for region in self.subregions:
            pop += region.population()  # Not Place.population(region)
        return pop


lane = Region("Lane County", [Place("Eugene", 166575), Place("Springfield", 60177)])
benton = Region("Benton County", [Place("Corvallis", 55298), Place("Philomath", 4594)])
s_willamette = Region("South Willamette Valley", [lane, benton])
print(s_willamette.population())  # Expected: 286644


"""Problem 6"""
class Score(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return 'Score("{}",{})'.format(self.name, self.score)


def normalize(projects: List[Score]) -> List[Score]:
    max_score = 0
    for obj in projects:
        if obj.score > max_score:
            max_score = obj.score
    new_scores = []
    for obj in projects:
        normalized = (obj.score*100) // max_score  # Not (max_score // obj.score) * 100
        name = obj.name
        new_score = Score(name, normalized)
        new_scores.append(new_score)
    return new_scores


scores = [Score("Leslie", 40), Score("Bobby", 23), Score("Adrian", 42)]
print(normalize(scores))
# [Score("Leslie", 95), Score("Bobby", 54), Score("Adrian", 100)]
