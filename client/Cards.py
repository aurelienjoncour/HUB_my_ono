import pygame

class Cards:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.cards = {
            "uno_b_0.png": None, "uno_b_1.png": None, "uno_b_2.png": None,
            "uno_b_3.png": None, "uno_b_4.png": None, "uno_b_5.png": None,
            "uno_b_6.png": None, "uno_b_7.png": None, "uno_b_8.png": None,
            "uno_b_9.png": None, "uno_b_p2.png": None, "uno_b_reverse.png": None,
            "uno_b_stop.png": None, "uno_back.png": None, "uno_g_0.png": None,
            "uno_g_1.png": None, "uno_g_2.png": None, "uno_g_3.png": None,
            "uno_g_4.png": None, "uno_g_5.png": None, "uno_g_6.png": None,
            "uno_g_7.png": None, "uno_g_8.png": None, "uno_g_9.png": None,
            "uno_g_p2.png": None, "uno_g_reverse.png": None, "uno_g_stop.png": None,
            "uno_m_p4.png": None, "uno_m_p4_b.png": None, "uno_m_p4_g.png": None,
            "uno_m_p4_r.png": None, "uno_m_p4_y.png": None, "uno_m_s.png": None,
            "uno_m_s_b.png": None, "uno_m_s_g.png": None, "uno_m_s_r.png": None,
            "uno_m_s_y.png": None, "uno_r_0.png": None, "uno_r_1.png": None,
            "uno_r_2.png": None, "uno_r_3.png": None, "uno_r_4.png": None,
            "uno_r_5.png": None, "uno_r_6.png": None, "uno_r_7.png": None,
            "uno_r_8.png": None, "uno_r_9.png": None, "uno_r_p2.png": None,
            "uno_r_reverse.png": None, "uno_r_stop.png": None, "uno_y_0.png": None,
            "uno_y_1.png": None, "uno_y_2.png": None, "uno_y_3.png": None,
            "uno_y_4.png": None, "uno_y_5.png": None, "uno_y_6.png": None,
            "uno_y_7.png": None, "uno_y_8.png": None, "uno_y_9.png": None,
            "uno_y_p2.png": None, "uno_y_reverse.png": None, "uno_y_stop.png": None,
        }
        self.load_assets()

    def create_card(self, card):
        print(f"Load {card}")
        return pygame.image.load(f"client/asset/cards/{card}")

    def load_assets(self):
        for e in list(self.cards):
            self.cards[e] = self.create_card(e)

    def display(self, filepath, pos):
        self.screen.blit(self.cards[str(filepath)], pos)

    def display_player(self, card, pos):
        if card.playable:
            self.screen.blit(self.cards[str(card.filepath)], pos)
        else:
            bad_card = self.cards[str(card.filepath)].copy()
            bad_card.fill((180, 180, 180), special_flags=pygame.BLEND_RGB_SUB)
            self.screen.blit(bad_card, pos)
