class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @classmethod
    def from_string(cls, s):
        words = s.split()
        return cls(words[0], words[1])

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __repr__(self):
        return "Card({},{})".format(self.rank, self.suit)


class FaceCard(Card):
    pass


c = FaceCard.from_string("Ace spades")
print(c)


class DeckOfCards(object):
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def __str__(self):
        elements = [str(x) for x in self.cards]
        return str(elements)


c = Card("5", "Diamonds")
print(c)

deck = DeckOfCards(["Spades", "Diamonds", "Hearts", "Clubs"], [x for x in range(1, 13)])
print(deck)

