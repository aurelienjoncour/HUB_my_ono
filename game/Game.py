from game.Deck import Deck
from game.Player import Player

class Game:

    def __init__(self, id) -> None:
        self.players = []
        self.nbPlayer = 1
        self.deck = Deck()
        self.topStackCard = None
        self.gameId = id
        self.isStarted = False
        self.play_sense = 1
        self.player_idx = 0
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

    def setIndexToNextPlayer(self, shouldSkip = False):
        if self.play_sense:
            if self.player_idx + 1 == self.nbPlayer:
                self.player_idx = 0
            else:
                self.player_idx += 1
        else:
            if self.player_idx + 1 == - 1:
                self.player_idx = self.nbPlayer - 1
            else:
                self.player_idx -= 1
        if shouldSkip:
            self.setIndexToNextPlayer()
        self.players[self.player_idx] = True

    def start(self):
        self.isStarted = True
