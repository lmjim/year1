"""CIS 211 Midterm Question"""


class Tree(object):
    """Abstract base class"""
    def max_leaf(self):
        raise NotImplementedError


class Leaf(Tree):
    """Leaves of tree hold positive integers"""
    def __init__(self, val):
        assert val > 0
        self.val = val

    def max_leaf(self):
        #FixMe
        return self.val


class Interior(Tree):
    """Interior node has two subtrees"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def max_leaf(self):
        #FixMe
        return max(self.left.max_leaf(), self.right.max_leaf())


t = Interior(Leaf(4), Interior(Leaf(5), Leaf(3)))
assert t.max_leaf() == 5
print(t.max_leaf())