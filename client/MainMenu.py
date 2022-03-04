#!/usr/bin/env python3

import pygame
from client.InputField import InputField
from client.Button import Button

from random import randrange

class MainMenu:
    infoObject = pygame.display.Info()
    ip_address = ""
    player_name = str(randrange(9999999999))
    clock = pygame.time.Clock()
    name_field = InputField({"x": (infoObject.current_w - 140) / 2, "y": 400},
    {"width": 140, "height": 32}, "pseudo")
    server_field = InputField({"x": (infoObject.current_w - 140) / 2, "y": 500},
    {"width": 140, "height": 32}, "127.0.0.1")
    button_click = Button({"x": (infoObject.current_w - 140) / 2, "y": 600},
    {"width": 140, "height": 32}, "play")
    text_fields = [name_field, server_field]
    join_button = None
    create_button = None
    quit_button = None
    run = True
    win = None
    should_exit = False

    def __init__(self, win) -> None:
        self.win = win
        self.background_image = pygame.image.load("asset/my_uno_bg.png").convert()
        self.logo = pygame.image.load("asset/ono_logo.png")
        #self.join_button = button(pygame.Color('chartreuse4'), 10, 10, 100, 20, "TEST")

    def menuLoop(self) -> None:
        while self.run:
            # TODO: display text, input for player name, server address
            # TODO: button join game, create game, quit
            if self.button_click.button_state:
                self.run = False
                self.player_name = self.name_field.text
                self.ip_address = self.server_field.text
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.should_exit = True
                    self.run = False
                for field in self.text_fields:
                    field.event_handler(event)
                self.button_click.event_handler(event)

            for field in self.text_fields:
                field.update()
            self.win.fill((128, 128, 128))
            self.win.blit(self.background_image, [0, 0])
            self.win.blit(self.logo, [(self.infoObject.current_w - 128) / 2, 150])
            for field in self.text_fields:
                field.draw(self.win)
            self.button_click.draw(self.win)
            pygame.display.flip()
