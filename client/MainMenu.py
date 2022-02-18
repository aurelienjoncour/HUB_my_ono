#!/usr/bin/env python3

import pygame
# from Button import button

class MainMenu:
    ip_address = ""
    player_name = ""
    clock = pygame.time.Clock()
    join_button = None
    create_button = None
    quit_button = None
    run = True
    win = None
    should_exit = False

    def __init__(self, win) -> None:
        self.win = win
        # self.join_button = button(pygame.Color('chartreuse4'), 10, 10, 100, 20, "TEST")

    def menuLoop(self) -> None:
        while self.run:
            self.win.fill((128, 128, 128))
            pygame.display.flip()
            
            # TODO: display text, input for player name, server address
            # TODO: button join game, create game, quit

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.should_exit = True
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run = False
