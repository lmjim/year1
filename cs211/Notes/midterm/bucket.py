"""CIS 211 Midterm Question"""


class Spillage(Exception):
    pass


class Bucket(object):
    """You can put stuff in! You can pour stuff out!"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.holding = 0  # Initially bucket is empty

    def pour_in(self, amount):
        """Pour amount of liquid into bucket, if there is enough room left"""
        space = self.capacity - self.holding
        if amount > space:
            raise Spillage("Too much! Over flowing!")
        self.holding += amount

    def pour_out(self, requested_amount):
        """Pour UP TO amount of liquid from the bucket.
        Iff more is requested than the bucket currently holds,
        pour out just what the bucket currently holds.
        Returns the amount of liquid actually poured out."""
        #FixMe
        if requested_amount > self.holding:
            out = self.holding  # don't add .copy()
            self.holding = 0
            return out
        else:
            self.holding -= requested_amount
            return requested_amount


b = Bucket(20)
b.pour_in(10)
out = b.pour_out(7)
assert out == 7
print(out)
out = b.pour_out(7)
assert out == 3
print(out)
out = b.pour_out(7)
assert out == 0
print(out)
