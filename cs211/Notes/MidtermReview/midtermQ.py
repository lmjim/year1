"""
Understand classes (subclasses) and objects
how to override classes
be good with recursion (even across classes)

Example Question:
"""


class Node:
    """Nodes in a tree"""

    def count_leaves(self):
        raise NotImplementedError('You better override this')


class Leaf(Node):
    def __init__(self, val):
        self.val = val

    def count_leaves(self):
        # FIXME   <-- This would be part of the question
        return 1  # This is the base case    <-- This is part of the answer


class Interior(Node):
    def __init__(self, left, right):
        """Left and right should be nodes"""
        self.left = left
        self.right = right

    def count_leaves(self):
        # FIXME   <-- This would be part of the question
        # This is the inductive case
        return self.left.count_leaves() + self.right.count_leaves()   # This is part of the answer


assert Interior(Interior(Leaf(7), Leaf(8)), Leaf(9)).count_leaves() == 3   # This is part of the question
print(Interior(Interior(Leaf(7), Leaf(8)), Leaf(9)).count_leaves())   # This is a test to see if answer works
print(Interior(Interior(Leaf(7), Leaf(8)),
               Interior(Leaf(3), Leaf(4))).count_leaves())   # This is a test to see if answer works

"""
            I
         /      \
         I      L=9
      /     \
    L=7     L=8
Graphical way to think through the question   <--Part of the answer (or rather help to get to answer)
"""


"""
You should also be able to the following:
Instead of number of leaves:
Give me a list of all the leaves
Add up all the values of the leaves
"""