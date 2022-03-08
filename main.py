#!/usr/bin/env python3
#  pyinstaller.exe --clean --log-level DEBUG --noconsole --onefile --windowed ./main.spec


import pygame

# pygame.init()

import os, sys

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

from client.MainMenu import MainMenu
from client.Graphic import Graphic
from client.Network import Network

infoObject = pygame.display.Info()
screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.SCALED)

menu = MainMenu(screen)
Main = Graphic(screen)

menu.menuLoop()

if not menu.should_exit:
    network = Network(menu.ip_address, 8080)
    res = network.connect(menu.player_name)
    playerId = int(res)
    Main.mainLoop(network, playerId)
