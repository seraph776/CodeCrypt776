
from collections import namedtuple


Card = namedtuple('Card', ['rank', 'suit'])

class CardDeck:
    ranks = [str(n) for n in range(2, 11 )] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.__cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position):
        return self.__cards[position]
