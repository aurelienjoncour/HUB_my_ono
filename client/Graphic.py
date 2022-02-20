#!/usr/bin/env python3

import pygame
from client.GameHUD import GameHUD

class Graphic:
	card_w = 64
	card_h = 96
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
		self.infoObject = pygame.display.Info()
		self.player_pos = (10, 10)
		self.opponents_pos = [
			(self.infoObject.current_w - self.card_w - 10, 10),
			(self.infoObject.current_w - self.card_w - 10, self.infoObject.current_h - self.card_h - 50),
			(10, self.infoObject.current_h - self.card_h - 50)
		]
		self.screen = screen
		self.hud = GameHUD(self.screen)
		self.background_image = pygame.image.load("client/asset/my_uno_bg.png").convert()
		self.clockwise = pygame.image.load(f"client/asset/arrow/uno_clockwise.png")
		self.anticlockwise = pygame.image.load(f"client/asset/arrow/uno_anticlockwise.png")

	def mainLoop(self, network, player_id):
		self.network = network
		self.player_id = player_id
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
			if game.play_sense == 1:
				self.screen.blit(self.clockwise, [(self.infoObject.current_w - 244) / 2 , (self.infoObject.current_h - 272) / 2 ])
			else:
				self.screen.blit(self.anticlockwise, [(self.infoObject.current_w - 244) / 2 , (self.infoObject.current_h - 272) / 2 ])
			for player in game.players:
				if player_id == player.id:
					self.hud.player(player, self.player_pos)
				else:
					self.hud.opponent(player, self.opponents_pos[0])
					self.hud.opponent(player, self.opponents_pos[1])
					self.hud.opponent(player, self.opponents_pos[2])

			self.hud.top_stack_card(game.topStackCard)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isrunning = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					#if event.button == 1:
					cardIdx = self.hud.clickOnCard()
					if cardIdx != None:
						for player in game.players:
							if player_id == player.id:
								print(player.deck[cardIdx].playable)