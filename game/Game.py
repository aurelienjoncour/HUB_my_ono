from game.Deck import Deck
from game.Player import Player

class Game:

    def __init__(self) -> None:
        self.players = []
        self.deck = Deck()

    def initPlayerCards(self):
        for player in self.players:
            player.deck = self.deck.getCards(7)

    def addPlayer(self, name):
        self.players.append(Player(name))
        