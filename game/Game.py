from game.Deck import Deck
from game.Player import Player

class Game:

    def __init__(self) -> None:
        self.players = []
        self.deck = Deck()
        self.topStackCard = None

    def initPlayerCards(self):
        for player in self.players:
            player.deck = self.deck.getCards(7)

    def addPlayer(self, name):
        self.players.append(Player(name))

    def setTopStackCard(self):
        tmpCard = None
        while self.topStackCard == None or self.topStackCard.color == None:
            if tmpCard != None:
                self.deck.addCard(tmpCard)
            tmpCard = self.deck.getCards()[0]
            self.topStackCard = tmpCard


    def start(self):
        self.initPlayerCards()
        self.setTopStackCard()