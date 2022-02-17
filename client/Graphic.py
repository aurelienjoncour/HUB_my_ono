#!/usr/bin/env python3

import pygame
from printCards import print_deck

class Graphic:

	window_width = 1280
	window_height = 720
	isrunning = True
	screen = None
	background_image = None
	flags = pygame.RESIZABLE
	clock = pygame.time.Clock()
	screens = 0

	def __init__(self) -> None:
		pygame.init()
		infoObject = pygame.display.Info()
		self.screen = pygame.display.set_mode([infoObject.current_w, infoObject.current_h], pygame.RESIZABLE)
		self.background_image = pygame.image.load("asset/my_uno_bg.png").convert()

	def mainLoop(self):
		test_list = ["uno_y_4.png","uno_r_7.png","uno_g_4.png"]
		while self.isrunning:
			self.screen.fill((255, 255, 255))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isrunning = False
			if self.screens == 0:
				self.screen.blit(self.background_image, [0, 0])
				print_deck(test_list,self.screen)
				pygame.display.flip()

			elif self.screens == 1:
				pass
