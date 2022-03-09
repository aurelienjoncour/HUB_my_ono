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
    FONT = pygame.font.SysFont('Arial', 22)
    color = pygame.Color("white")
    button_click = Button({"x": (infoObject.current_w - 140) / 2, "y": 600},
    {"width": 140, "height": 32}, "Play")
    button_exit = Button({"x": (infoObject.current_w - 140) / 2, "y": 700},
    {"width": 140, "height": 32}, "Quit")
    stacking_icon = pygame.image.load("asset/stacking_button.png")
    stacking_rect = pygame.Rect((infoObject.current_w - 64) / 12, (infoObject.current_h - 96) / 2, 64, 96)
    text_fields = [name_field, server_field]
    join_button = None
    create_button = None
    quit_button = None
    run = True
    win = None
    should_exit = False
    isActivate = False

    def __init__(self, win) -> None:
        self.win = win
        self.background_image = pygame.image.load("asset/my_uno_bg.png").convert()
        self.logo = pygame.image.load("asset/ono_logo.png")

    def menuLoop(self, error_msg) -> None:
        while self.run:
            # TODO: button join game, create game, quit
            if self.button_exit.button_state:
                self.should_exit = True
                self.run = False
            if self.button_click.button_state:
                self.run = False
                self.player_name = self.name_field.text
                self.ip_address = self.server_field.text
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.should_exit = True
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.should_exit = True
                        self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.isActivate = self.eventButtonStacking()
                for field in self.text_fields:
                    field.event_handler(event)
                self.button_click.event_handler(event)
                self.button_exit.event_handler(event)

            for field in self.text_fields:
                field.update()
            self.win.fill((128, 128, 128))
            self.win.blit(self.background_image, [0, 0])
            self.win.blit(self.logo, [(self.infoObject.current_w - 128) / 2, 150])
            self.Stacking()
            if error_msg != None:
                text_surface = self.FONT.render(error_msg, True, self.color)
                self.win.blit(text_surface, ((self.infoObject.current_w - 140) / 2, 540))
            for field in self.text_fields:
                field.draw(self.win)
            self.button_click.draw(self.win)
            self.button_exit.draw(self.win)
            pygame.display.flip()

    def Stacking(self):
        if self.isActivate:
            bad_card = self.stacking_icon.copy()
            bad_card.fill((80, 80, 80), special_flags=pygame.BLEND_RGB_SUB)
            self.win.blit(bad_card, [(self.infoObject.current_w - 64) / 12, (self.infoObject.current_h - 96) / 2])
        else:
            self.win.blit(self.stacking_icon, [(self.infoObject.current_w - 64) / 12, (self.infoObject.current_h - 96) / 2])

    def eventButtonStacking(self):
        if self.stacking_rect.collidepoint(pygame.mouse.get_pos()):
            return not self.isActivate