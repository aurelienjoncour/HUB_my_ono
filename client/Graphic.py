#!/usr/bin/env python3

import pygame
from client.GameHUD import GameHUD

class Graphic:

	window_width = 1280
	window_height = 720
	isrunning = True
	screen = None 	#Class for window handling
	hud = None 		#Class for game display handling
	network = None  #Class for network handling
	background_image = None
	flags = pygame.RESIZABLE
	clock = pygame.time.Clock()

	def __init__(self, screen) -> None:
		pygame.init()
		self.screen = screen
		self.hud = GameHUD(self.screen)
		self.background_image = pygame.image.load("client/asset/my_uno_bg.png").convert()

	def mainLoop(self, network):
		self.network = network
		test_list = ["uno_y_4.png","uno_r_7.png","uno_g_4.png"]
		while self.isrunning:
			self.clock.tick(60)
			try:
				game = self.network.send("get")
			except:
				self.isrunning = False
				print("Couldn't get game")
				break
			self.screen.fill((255, 255, 255))
			self.screen.blit(self.background_image, [0, 0])
			self.hud.player(game.players[0].deck)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isrunning = False
