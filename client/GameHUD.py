from client.Cards import Cards
import pygame

class GameHUD:
    def __init__(self, screen) -> None:
        self.card_w = 64
        self.card_h = 96
        self.cards = Cards(screen)
        self.card_pos = []
        self.infoObject = pygame.display.Info()
        self.screen = screen
        self.font_name = pygame.font.SysFont('Arial', 25)
        self.font_nb_card = pygame.font.SysFont('Arial', 50)
        pygame.display.set_caption('Box Test')

    def card_indicator(self, nb):
        self.screen.blit(self.font_nb_card.render(str(nb), True, (255,255,255)), (10, 150))

    def player_name(self, name):
        self.screen.blit(self.font_name.render(name, True, (255,255,255)), (50, 150))

    def opponent_card_deck(self, cardList):
        y = self.infoObject.current_h - self.card_h -50
        x = 10
        for card in cardList:
            self.cards.display("uno_back.png", (x, y))
            x = x + 40

    def player_card_deck(self, cardList):
        y = 50
        x = 10
        self.card_pos.clear()
        for card in cardList:
            self.cards.display(card.filepath, (x, y))
            self.card_pos.append(pygame.Rect(x, y, x + self.card_w, y + self.card_h))
            x = x + 40

    def top_stack_card(self, card):
        self.cards.display(card.filepath, ((self.infoObject.current_w - self.card_w) / 2 , (self.infoObject.current_h - self.card_h) / 2 ))

    def opponent(self, oponent):
        self.player_name(oponent.name)
        self.card_indicator(len(oponent.deck))
        self.opponent_card_deck(oponent.deck)

    def player(self, player):
        self.player_name(player.name)
        self.card_indicator(len(player.deck))
        self.player_card_deck(player.deck)

    def draw_arrow(self):
        #TODO: display arrow that show
        print("draw arrow")

    def clickOnCard(self):
        print("Click !")
        for i in range(len(self.card_pos)):
            if self.card_pos[i].collidepoint(pygame.mouse.get_pos()):
                print(i)

