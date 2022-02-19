from distutils.log import info
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

    def is_right_side(self, pos):
        if pos[0] < (self.infoObject.current_w / 2):
            return False
        return True

    def card_indicator(self, nb, pos):
        if self.is_right_side(pos):
            self.screen.blit(self.font_nb_card.render(str(nb), True, (255,255,255)), (pos[0] + 32, pos[1] + 100))
        else:
            self.screen.blit(self.font_nb_card.render(str(nb), True, (255,255,255)), (pos[0], pos[1] + 100))

    def player_name(self, name, pos):
        if self.is_right_side(pos):
            self.screen.blit(self.font_name.render(name, True, (255,255,255)), (pos[0] - 200, pos[1] + 100))
        else:
            self.screen.blit(self.font_name.render(name, True, (255,255,255)), (pos[0] + 40, pos[1] + 100))

    def opponent_card_deck(self, cardList, pos):
        _pos = list(pos)
        for card in cardList:
            self.cards.display("uno_back.png", _pos)
            if self.is_right_side(pos):
                _pos[0] = _pos[0] - 40
            else:
                _pos[0] = _pos[0] + 40

    def player_card_deck(self, cardList, pos):
        _pos = list(pos)
        self.card_pos.clear()
        for card in cardList:
            self.cards.display(card.filepath, _pos)
            self.card_pos.append(pygame.Rect(_pos[0], _pos[1], self.card_w, self.card_h))
            _pos[0] += 40

    def top_stack_card(self, card):
        self.cards.display(card.filepath, ((self.infoObject.current_w - self.card_w) / 2 , (self.infoObject.current_h - self.card_h) / 2 ))

    def opponent(self, oponent, pos):
        self.player_name(oponent.name, pos)
        self.card_indicator(len(oponent.deck), pos)
        self.opponent_card_deck(oponent.deck, pos)

    def player(self, player, pos):
        self.player_name(player.name, pos)
        self.card_indicator(len(player.deck), pos)
        self.player_card_deck(player.deck, pos)

    def draw_arrow(self):
        #TODO: display arrow that show
        print("draw arrow")

    def clickOnCard(self):
        carte_idx = None
        print("Click !")
        for i in range(len(self.card_pos)):
            if self.card_pos[i].collidepoint(pygame.mouse.get_pos()):
                carte_idx = i
        return carte_idx
