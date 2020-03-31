"""A linked list instead of being an array it has a reference to the next element"""


class LinkedList(object):
    pass


class EmptyList(LinkedList):

    def __init__(self):
        return

    def length(self):
        return 0


class NonEmptyList(LinkedList):

    def __init__(self, item, li: LinkedList):
        self.item = item
        self.rest = li

    def length(self):
        return 1 + self.rest.length()

    def __str__(self):
        return "{}, {}".format(self.item, self.rest)


li = EmptyList()
print(li.length())
li = NonEmptyList(1, li)
li = NonEmptyList(2, li)
li = NonEmptyList(3, li)
print(li.length())
print(li)
print(NonEmptyList(0, li))
