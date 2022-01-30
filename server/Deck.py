from random import shuffle
from Card import Card, Color, Value, Bonus

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(0, 2):
            for c in Color:
                for v in Value:
                    if v == Value.ZERO and i % 2 == 0:
                        self.cards.append(Card(v, c))
                    elif v != Value.ZERO:  
                        self.cards.append(Card(v, c))
                for b in Bonus:
                    if i % 2 == 0:
                        self.cards.append(Card(b, None))
        shuffle(self.cards)
        for card in self.cards:
            print(card.filepath)
        print(len(self.cards))

gameDeck = Deck()