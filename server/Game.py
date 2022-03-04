from server.Deck import Deck
from server.Player import Player
from server.Card import Value
from server.Card import Bonus
from server.Card import Color

class Game:

    def __init__(self, id) -> None:
        self.players = []
        self.nbPlayer = 1
        self.deck = Deck()
        self.topStackCard = None
        self.gameId = id
        self.isStarted = False
        self.won = False
        self.play_sense = 1
        self.player_idx = 0
        self.setTopStackCard()

    def gameToDict(self):
        players = []
        for player in self.players:
            players.append(player.playerToDict())

        return {
            "players": players,
            "topStackCard": {
                "filepath": self.topStackCard.filepath
            },
            "play_sense": self.play_sense,
            "won": self.won
        }

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
        self.players[self.player_idx].should_play = False
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
        if not shouldSkip:
            self.players[self.player_idx].should_play = True

    def play_card(self, card, player_idx, color):
        print("Play Card")
        skip = False
        additional_card = []
        self.topStackCard.reset_bonus_color()
        self.deck.addCard(self.topStackCard)                    #On ajoute la carte joué dans le deck commun
        self.players[player_idx].deck.remove(card)              #On supprime la carte joué du deck du joueur
        if len(self.players[player_idx].deck) == 0:
            print(self.players[player_idx].name + " won !")
            self.won = True
            return

        if type(card.value) == Bonus and card.color == None:    #Si la carte est une bonus on change ça couleur
            card.change_bonus_color(Color(color))
        self.topStackCard = card
        
        if type(card.value) == Value and card.value == Value.REVERSE:
            self.play_sense = not self.play_sense
        elif type(card.value) == Value and card.value == Value.SKIP:
            skip = True
        elif type(card.value) == Value and card.value == Value.PLUS_TWO:
            additional_card = self.deck.getCards(2)
            skip = True
        elif type(card.value) == Bonus and card.value == Bonus.SUPER_JOKER:
            additional_card = self.deck.getCards(4)
            skip = True
        self.setIndexToNextPlayer(skip)                             #On déplace l'index sur le prochain joueur
        for card in additional_card:                                #On ajoute les cartes au prochain joueur
                self.players[self.player_idx].deck.append(card)
        if skip:
            self.setIndexToNextPlayer()
        self.is_player_card_playable()                              #On update le status des cartes jouables
        self.add_card_if_not_playable()                             #On ajoute des cartes si le deck n'est pas jouable


    def start(self):
        self.isStarted = True
        self.players[self.player_idx].should_play = True
        self.add_card_if_not_playable()
