#!/usr/bin/env python3

import pygame
from MainMenu import MainMenu
from Graphic import Graphic
from Network import Network

pygame.init()

infoObject = pygame.display.Info()
screen = pygame.display.set_mode([infoObject.current_w, infoObject.current_h], pygame.RESIZABLE)

menu = MainMenu(screen)
Main = Graphic(screen)

menu.menuLoop()

if not menu.should_exit:
    network = Network(menu.ip_address, 8080)
    ret = network.getRet()
    Main.mainLoop()
