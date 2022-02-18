from client.Cards import Cards
import pygame

class GameHUD:
    def __init__(self, screen) -> None:
        self.card_w = 64
        self.card_h = 96
        self.cards = Cards(screen)
        self.infoObject = pygame.display.Info()
        self.screen = screen
        self.font_name = pygame.font.SysFont('Arial', 25)
        self.font_nb_card = pygame.font.SysFont('Arial', 50)
        pygame.display.set_caption('Box Test')

    def card_indicator(self):
        self.screen.blit(self.font_nb_card.render('7', True, (255,255,255)), (10, 150))
        print("card indicator")

    def player_name(self):
        self.screen.blit(self.font_name.render('Jaajeur', True, (255,255,255)), (50, 150))
        print("player name")

    def opponent_card_deck(self, cardList):
        y = self.infoObject.current_h - self.card_h -50
        x = 10
        for card in cardList:
            self.cards.display("uno_back.png", (x, y))
            x = x + 40
        #TODO: display hidden deck
        print("card hidden")

    def player_card_deck(self, cardList):
        y = 50
        x = 10
        for card in cardList:
            self.cards.display(card.filepath, (x, y))
            x = x + 40

    def top_stack_card(self, card):
        self.cards.display(card.filepath, (self.infoObject.current_w / 2 - self.card_w, self.infoObject.current_h / 2 - self.card_h))

    def opponent(self):
        #TODO: display all components of the oponent
        self.player_name()
        self.card_indicator()
        self.opponent_card_deck()

    def player(self, cardList):
        #TODO: display actual player
        self.player_name()
        self.card_indicator()
        self.player_card_deck(cardList)

    def draw_arrow(self):
        #TODO: display arrow that show
        print("draw arrow")

