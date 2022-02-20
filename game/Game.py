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

    def is_player_card_playable(self):
        for player in self.players:
            player.updatePlayableCard(self.topStackCard)

    def add_card_if_not_playable(self):
        for player in self.players:
            if player.should_play:
                while not player.isDeckPlayable():
                    card = self.deck.getCards()[0]
                    player.deck.append(card)
                    self.is_player_card_playable()

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
        self.players[self.player_idx].should_play = True
        self.add_card_if_not_playable()

    def play_card(self, card, player_idx):
        print("Play Card")
        self.deck.addCard(self.topStackCard)
        self.deck.addCard(card)
        print("After Add Card")
        self.topStackCard = card
        self.is_player_card_playable()
        print("Before remove")
        self.players[player_idx].deck.remove(card)
        print("AFter remove")
        self.setIndexToNextPlayer()


    def start(self):
        self.isStarted = True
        self.players[self.player_idx].should_play = True
