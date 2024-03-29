import pygame

class Button:

    def __init__(self, pos, size, text = "") -> None:
        self.FONT = pygame.font.SysFont('Arial', 22)
        self.text = text
        self.rect = pygame.Rect(pos["x"], pos["y"],
                                size["width"], size["height"])
        self.color = pygame.Color("white")
        self.text_surface = self.FONT.render(text, True, self.color)
        self.button_state = False

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.button_state = not self.button_state

    def draw(self, screen):
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
        if self.button_state:
            pygame.draw.rect(screen, self.color, self.rect, 2)
        else:
            pygame.draw.rect(screen, pygame.Color("white"), self.rect, 2)