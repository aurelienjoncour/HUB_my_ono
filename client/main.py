#!/usr/bin/env python3

import pygame

class graphic:

	window_width = 1280
	window_height = 720
	isrunning = True
	screen = None
	background_image = None
	flags = pygame.RESIZABLE
	def setup(self):
		pygame.init()
		infoObject = pygame.display.Info()
		self.window_width = infoObject.current_w
		self.window_height = infoObject.current_h
		self.screen = pygame.display.set_mode([self.window_width, self.window_height], self.flags)
		self.background_image = pygame.image.load("my_uno_bg.png").convert()

	def mainLoop(self):
		while self.isrunning:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isrunning = False
				self.screen.blit(self.background_image, [0, 0])
				pygame.display.flip()


# Driver code
# Object instantiation
Rodger = graphic()

# Accessing class attributes
# and method through objects
print(Rodger.window_width)
Rodger.setup()
Rodger.mainLoop()
