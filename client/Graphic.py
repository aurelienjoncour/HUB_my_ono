#!/usr/bin/env python3

import pygame
from printCards import print_deck
from Cards import Cards

class Graphic:

	window_width = 1280
	window_height = 720
	isrunning = True
	screen = None
	cards = None
	background_image = None
	flags = pygame.RESIZABLE
	clock = pygame.time.Clock()

	def __init__(self, screen) -> None:
		pygame.init()
		self.screen = screen
		self.cards = Cards(self.screen)
		self.background_image = pygame.image.load("asset/my_uno_bg.png").convert()

	def mainLoop(self):
		test_list = ["uno_y_4.png","uno_r_7.png","uno_g_4.png"]
		while self.isrunning:
			self.screen.fill((255, 255, 255))
			self.screen.blit(self.background_image, [0, 0])
			print_deck(test_list, self.cards)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isrunning = False
