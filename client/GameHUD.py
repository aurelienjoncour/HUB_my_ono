from Cards import Cards

class GameHUD:
    def __init__(self, screen) -> None:
        self.cards = Cards(screen)

    def card_indicator(self):
        #TODO: display 2 overlapping cards icons and a number
        print("card indicator")

    def player_name(self):
        #TODO: display player name inside a rectangle
        print("player name")

    def opponent_card_deck(self):
        #TODO: display hidden deck
        print("card hidden")

    def player_card_deck(self, filepathList):
        y = 50
        x = 10
        for card in filepathList:
            self.cards.display(card, (x, y))
            x = x + 40

    def opponent(self):
        #TODO: display all components of the oponent
        self.player_name()
        self.card_indicator()
        self.opponent_card_deck()

    def player(self, cardList):
        #TODO: display actual player
        #self.player_name()
        #self.card_indicator()
        self.player_card_deck(cardList)
    
    def draw_arrow(self):
        #TODO: display arrow that show
        print("draw arrow")