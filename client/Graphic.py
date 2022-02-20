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
		self.screen = screen
		self.hud = GameHUD(self.screen)
		self.background_image = pygame.image.load("client/asset/my_uno_bg.png").convert()
		self.clockwise = pygame.image.load(f"client/asset/arrow/uno_clockwise.png")
		self.anticlockwise = pygame.image.load(f"client/asset/arrow/uno_anticlockwise.png")

	def get_player(self):
		for player in self.game.players:
			if self.player_id == player.id:
				return player

	def play(self, cardIdx):
		player = self.get_player()
		if player.should_play and player.deck[cardIdx].playable:
			self.game = self.network.send(str(cardIdx))

	def mainLoop(self, network, player_id):
		self.network = network
		self.player_id = player_id
		while self.isrunning:
			self.clock.tick(60)
			try:
				self.game = self.network.send("get")
			except:
				self.isrunning = False
				print("Couldn't get game")
				break
			self.screen.fill((255, 255, 255))
			self.screen.blit(self.background_image, [0, 0])
			if self.game.play_sense == 1:
				self.screen.blit(self.clockwise, [(self.infoObject.current_w - 244) / 2 , (self.infoObject.current_h - 272) / 2 ])
			else:
				self.screen.blit(self.anticlockwise, [(self.infoObject.current_w - 244) / 2 , (self.infoObject.current_h - 272) / 2 ])

			self.hud.all_players(self.game.players, player_id)
			self.hud.top_stack_card(self.game.topStackCard)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isrunning = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						cardIdx = self.hud.clickOnCard()
						if cardIdx != None:
							self.play(cardIdx)
