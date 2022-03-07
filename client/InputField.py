import pygame

class InputField:

    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')

    def __init__(self, pos, size, text = "") -> None:
        self.FONT = pygame.font.SysFont('Arial', 22)
        self.text = text
        self.size = size
        self.rect = pygame.Rect(pos["x"], pos["y"],
                                size["width"], size["height"])
        self.color = self.COLOR_INACTIVE
        self.text_surface = self.FONT.render(text, True, self.color)
        self.active = False

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            if self.active:
                self.color = self.COLOR_ACTIVE
            else:
                self.color = self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN and self.active == True:
            if event.key == pygame.K_RETURN:
                print(self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.text_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        self.rect.w = max(self.size["width"], self.text_surface.get_width()+10)

    def draw(self, screen):
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)