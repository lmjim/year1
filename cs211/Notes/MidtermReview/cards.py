"""Personal Practice for Midterm"""


class DeckOfCards(object):
    pass


class Cards(DeckOfCards):
    def __init__(self):
        self.cards = []
        self.values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.suits = ["Spade", "Diamond", "Heart", "Club"]

    def add_cards(self):
        # card = ["3", "Diamond]    cards = [[],[],[]]
        for suit in self.suits:
            for value in self.values:
                card = [suit, value]
                self.cards.append(card)
        return self.cards



