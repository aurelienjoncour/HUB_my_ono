#!/usr/bin/env python3

from ntpath import join
import pygame
from Button import button

class MainMenu:
    join_button =None
    create_button =None
    quit_button =None

    def __init__(self) -> None:
        self.join_button = button(pygame.Color('chartreuse4'), 10, 10, 100, 20, "TEST")

