#!/usr/bin/env python3

import pygame

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
		self.background_image = pygame.image.load("my_uno_bg.png").convert()

	def mainLoop(self):
		while self.isrunning:
			self.screen.fill((255, 255, 255))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isrunning = False
			if self.screens == 0:
				self.screen.blit(self.background_image, [0, 0])
				pygame.display.flip()
			elif self.screens == 1:
				pass
