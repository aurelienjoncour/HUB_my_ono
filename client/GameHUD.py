from client.Cards import Cards
from client.Button import Button
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
        self.clockwise = pygame.image.load(f"asset/arrow/uno_clockwise.png")
        self.anticlockwise = pygame.image.load(f"asset/arrow/uno_anticlockwise.png")
        self.icon = pygame.image.load(f"asset/logo.png")
        pygame.display.set_caption('My Ono')
        pygame.display.set_icon(self.icon)
        self.posY = self.infoObject.current_h / 2 - 50
        self.posX = self.infoObject.current_w / 2 - 50
        self.button_denounce = Button({"x": self.infoObject.current_w / 2 - 180, "y": (self.infoObject.current_h - 272) / 2 - 40}, {"width": 180, "height": 32}, "Dénoncer !")
        self.button_skip = Button({"x": self.infoObject.current_w / 2 + 20, "y": (self.infoObject.current_h - 272) / 2 - 40}, {"width": 180, "height": 32}, "Passer !")
        self.rect_red = pygame.Rect(self.posX, self.posY, 50, 50)
        self.rect_green = pygame.Rect(self.posX + 50, self.posY, 50, 50)
        self.rect_blue = pygame.Rect(self.posX, self.posY + 50, 50, 50)
        self.rect_yellow = pygame.Rect(self.posX + 50, self.posY + 50, 50, 50)

    def get_color_choice(self):
        if self.rect_red.collidepoint(pygame.mouse.get_pos()):
            return 0
        if self.rect_green.collidepoint(pygame.mouse.get_pos()):
            return 1
        if self.rect_blue.collidepoint(pygame.mouse.get_pos()):
            return 2
        if self.rect_yellow.collidepoint(pygame.mouse.get_pos()):
            return 3
        return None

    def color_choice(self):
        red = pygame.Color("red")
        green = pygame.Color("green")
        yellow = pygame.Color("yellow")
        blue = pygame.Color("blue")
        pygame.draw.rect(self.screen, red, self.rect_red)
        pygame.draw.rect(self.screen, green, self.rect_green)
        pygame.draw.rect(self.screen, blue, self.rect_blue)
        pygame.draw.rect(self.screen, yellow, self.rect_yellow)

    def is_right_side(self, pos):
        if pos[0] < (self.infoObject.current_w / 2):
            return False
        return True

    def chose_color(self):
        self.screen.blit(self.chose_frame, [(self.infoObject.current_w - 140) / 2 , (self.infoObject.current_h - 140) / 2 ])
        pygame.draw.rect(self.screen,(255,255,0),((self.infoObject.current_w - 131) / 2, (self.infoObject.current_h - 128) / 2, 64, 64))


    def card_indicator(self, nb, pos):
        if self.is_right_side(pos):
            if nb >= 10:
                self.screen.blit(self.font_nb_card.render(str(nb), True, (255,255,255)), (pos[0], pos[1] + 100))
            else:
                self.screen.blit(self.font_nb_card.render(str(nb), True, (255,255,255)), (pos[0] + 32, pos[1] + 100))
        else:
            self.screen.blit(self.font_nb_card.render(str(nb), True, (255,255,255)), (pos[0], pos[1] + 100))

    def show_win(self, players):
        for player in players:
            if player["should_play"]:
                self.screen.blit(self.font_name.render(player["name"] + " as won the game !", True, (0, 0, 0)), (500, 10))

    def player_name(self, player, pos):
        color = (255, 255, 255)
        if player["should_play"]:
            color = (0, 0, 255)

        if self.is_right_side(pos):
            self.screen.blit(self.font_name.render(player["name"], True, color), (pos[0] - 200, pos[1] + 100))
        else:
            self.screen.blit(self.font_name.render(player["name"], True, color), (pos[0] + 64, pos[1] + 100))

    def opponent_card_deck(self, cardList, pos):
        _pos = list(pos)
        for card in cardList:
            self.cards.display("uno_back.png", _pos)
            if self.is_right_side(pos):
                _pos[0] = _pos[0] - 20
            else:
                _pos[0] = _pos[0] + 20

    def player_card_deck(self, cardList, pos):
        _pos = list(pos)
        self.card_pos.clear()
        for card in cardList:
            self.cards.display_player(card, _pos)
            self.card_pos.append(pygame.Rect(_pos[0], _pos[1], self.card_w, self.card_h))
            _pos[0] += 40

    def top_stack_card(self, card):
        self.cards.display(card["filepath"], ((self.infoObject.current_w - self.card_w) / 2 , (self.infoObject.current_h - self.card_h) / 2 ))

    def opponent(self, oponent, pos):
        self.player_name(oponent, pos)
        self.card_indicator(len(oponent["deck"]), pos)
        self.opponent_card_deck(oponent["deck"], pos)

    def player(self, player, pos):
        self.player_name(player, pos)
        self.card_indicator(len(player["deck"]), pos)
        self.player_card_deck(player["deck"], pos)

    def all_players(self, players, playerId):
        player_pos = (10, 10)
        opponents_pos = [
            (self.infoObject.current_w - self.card_w - 10, 10),
            (self.infoObject.current_w - self.card_w - 10, self.infoObject.current_h - self.card_h - 50),
            (10, self.infoObject.current_h - self.card_h - 50)
        ]
        j = 0
        for i in range(len(players)):
            if players[i]["id"] == playerId:
                j = i
                break
        self.player(players[j], player_pos)
        j += 1
        for i in range(len(players) - 1):
            if (j == len(players)):
                j = 0
            self.opponent(players[j], opponents_pos[i])
            j += 1

    def draw_arrow(self, play_sense):
        if play_sense == 1:
            self.screen.blit(self.clockwise, [(self.infoObject.current_w - 244) / 2, (self.infoObject.current_h - 272) / 2])
        else:
            self.screen.blit(self.anticlockwise, [(self.infoObject.current_w - 244) / 2, (self.infoObject.current_h - 272) / 2])

    def draw_game_button(self, ask_bluff):
        if ask_bluff:
            self.button_denounce.draw(self.screen)
            self.button_skip.draw(self.screen)

    def event_handler(self, event, ask_bluff):
        if ask_bluff:
            self.button_denounce.event_handler(event)
            self.button_skip.event_handler(event)
            state = {
                "denounce": self.button_denounce.button_state,
                "skip": self.button_skip.button_state
            }
            self.button_denounce.button_state = False
            self.button_skip.button_state = False
            return state
        return None

    def clickOnCard(self):
        carte_idx = None
        print("Click !")
        for i in range(len(self.card_pos)):
            if self.card_pos[i].collidepoint(pygame.mouse.get_pos()):
                carte_idx = i
        return carte_idx
