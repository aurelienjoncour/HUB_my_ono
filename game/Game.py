from game.Deck import Deck
from game.Player import Player

class Game:

    def __init__(self, id) -> None:
        self.players = []
        self.nbPlayer = 0
        self.deck = Deck()
        self.topStackCard = None
        self.gameId = id
        self.isStarted = False
        self.setTopStackCard()

    def addPlayer(self, name, player_id):
        player = Player(name, player_id)
        player.deck = self.deck.getCards(7)
        self.players.append(player)
        self.nbPlayer = len(self.players)
        self.is_player_card_playable()

    def setTopStackCard(self):
        tmpCard = None
        while self.topStackCard == None or self.topStackCard.color == None:
            if tmpCard != None:
                self.deck.addCard(tmpCard)
            tmpCard = self.deck.getCards()[0]
            self.topStackCard = tmpCard
        self.is_player_card_playable()

    def is_player_card_playable(self):
        for player in self.players:
            player.updatePlayableCard(self.topStackCard)

    def start(self):
        self.isStarted = True
