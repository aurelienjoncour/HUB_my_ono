#!/usr/bin/env python3
#  pyinstaller.exe --clean --log-level DEBUG --onefile --windowed ./main.spec

import pygame
import platform

# pygame.init()

import os, sys

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

from client.MainMenu import MainMenu
from client.Graphic import Graphic
from client.Network import Network

infoObject = pygame.display.Info()

if platform.system() == "Windows":
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.RESIZABLE)

menu = MainMenu(screen)
Main = Graphic(screen)

menu.menuLoop()

if not menu.should_exit:
    network = Network(menu.ip_address, 8080)
    res = network.connect(menu.player_name)
    playerId = int(res)
    Main.mainLoop(network, playerId)
