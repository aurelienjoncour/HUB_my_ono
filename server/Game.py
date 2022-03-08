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
        self.p2_stack = 0
        self.ask_bluff = None #id of the player asked for bluff
        self.ask_p2 = None #id of the player asked for p2
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
            "won": self.won,
            "ask_bluff": self.ask_bluff,
            "ask_p2": self.ask_p2
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

    def handle_p2_res(self): #handle Skip p2
        additional_card = self.deck.getCards(self.p2_stack)
        for card in additional_card:                                #On ajoute les cartes pour nous
            self.players[self.player_idx].deck.append(card)         #On passe au suivant
        self.end_tour(False, [])
        self.update_card()
        self.p2_stack = 0
        self.ask_p2 = None

    def handle_bluff(self, denonce):
        print("Call Handle bluff function")
        self.ask_bluff = None
        if denonce == True:
            if self.is_player_bluff(self.players[self.player_idx]):
                print("Bluff")
                additional_card = self.deck.getCards(4)
                for card in additional_card:
                    self.players[self.player_idx].deck.append(card)
                self.setIndexToNextPlayer(False) 
                self.update_card()
                #donner +4 carte au joueur qui a poser le +4, passer au joueur suivant
            else:
                print("no bluff")
                additional_card = self.deck.getCards(6)
                skip = True
                self.end_tour(skip, additional_card)
                self.update_card()
                #donner +6 carte au joueur qui dénonce, skip le joueur
        else:
            additional_card = self.deck.getCards(4)
            skip = True
            self.end_tour(skip, additional_card)
            self.update_card()
            print("no denonce")

    def is_player_bluff(self, player):
        for card in player.deck:
            if card.playable:
                return True
        return False

    def have_p2(self, player):
        for card in player.deck:
            if type(card.value) == Value and card.value == Value.PLUS_TWO:
                return True
        return False

    def make_only_p2_playable(self, player):
        for card in player.deck:
            if type(card.value) == Value and card.value == Value.PLUS_TWO:
                card.playable = True
            else:
                card.playable = False

    def add_card_if_not_playable(self):
        for player in self.players:
            if player.should_play:
                while not player.isDeckPlayable():
                    card = self.deck.getCards()[0]
                    player.deck.append(card)
                    self.is_player_card_playable()

    def get_next_player(self):
        next_player = None
        if self.play_sense:
            if self.player_idx + 1 == self.nbPlayer:
                next_player = 0
            else:
                next_player = self.player_idx + 1
        else:
            if self.player_idx - 1 == - 1:
                next_player = self.nbPlayer - 1
            else:
                next_player = self.player_idx - 1
        return next_player

    def setIndexToNextPlayer(self, shouldSkip = False):
        self.players[self.player_idx].should_play = False
        self.player_idx = self.get_next_player()
        if not shouldSkip:
            self.players[self.player_idx].should_play = True

    def update_card(self):
        self.is_player_card_playable()                              #On update le status des cartes jouables
        self.add_card_if_not_playable()                             #On ajoute des cartes si le deck n'est pas jouable

    def end_tour(self, skip, additional_card):
        self.setIndexToNextPlayer(skip)                             #On déplace l'index sur le prochain joueur
        for card in additional_card:                                #On ajoute les cartes au prochain joueur
                self.players[self.player_idx].deck.append(card)
        if skip:
            self.setIndexToNextPlayer()

    def play_card(self, card, player_idx, color):
        print("Play Card")
        skip = False
        self.ask_p2 = None
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
            self.p2_stack += 2
            if not self.have_p2(self.players[self.get_next_player()]):
                additional_card = self.deck.getCards(self.p2_stack)
                skip = True
                self.p2_stack = 0
            else:
                self.ask_p2 = self.players[self.get_next_player()].id
                self.make_only_p2_playable(self.players[self.get_next_player()])
                self.end_tour(False, [])
                return

        elif type(card.value) == Bonus and card.value == Bonus.SUPER_JOKER:
            self.ask_bluff = self.players[self.get_next_player()].id
            self.players[self.player_idx].should_play = False
            print("Bluff ?: ", self.is_player_bluff(self.players[player_idx]))
            return
        self.end_tour(skip, additional_card)
        self.update_card()


    def start(self):
        self.isStarted = True
        self.players[self.player_idx].should_play = True
        self.add_card_if_not_playable()
