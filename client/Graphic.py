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
	choose_color = False
	color = None
	cardIdx = None
	flags = pygame.RESIZABLE
	clock = pygame.time.Clock()

	def __init__(self, screen) -> None:
		# pygame.init()
		self.screen = screen
		self.hud = GameHUD(self.screen)
		self.background_image = pygame.image.load("asset/my_uno_bg.png").convert()

	def get_player(self):
		for player in self.game["players"]:
			if self.player_id == player["id"]:
				return player

	def play(self):
		player = self.get_player()
		if player["should_play"] and player["deck"][self.cardIdx]["playable"]:
			if self.choose_color == True:
				self.network.send(str(self.cardIdx) + ":" + str(self.color))
				self.color = None
				self.choose_color = False
			elif player["deck"][self.cardIdx]["color"] == None:
				self.choose_color = True
			else:
				self.game = self.network.send(str(self.cardIdx))

	def mainLoop(self, network, player_id, stack_p2):
		self.network = network
		self.player_id = player_id
		if stack_p2:
			self.network.send("gamerule:stack_p2")
		else:
			self.network.send("gamerule:dont_stack_p2")
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
			self.hud.draw_arrow(self.game["play_sense"])
			self.hud.all_players(self.game["players"], player_id)
			self.hud.top_stack_card(self.game["topStackCard"])
			ask_bluff = self.game["ask_bluff"] == self.player_id
			ask_p2 = self.game["ask_p2"] == self.player_id
			self.hud.draw_game_button(ask_bluff, ask_p2, self.game["won"])
			self.hud.counter()
			if self.choose_color:
				self.hud.color_choice()
			if self.game["won"]:
				self.hud.show_win(self.game["players"])
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.isrunning = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.isrunning = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						if self.choose_color:
							self.color = self.hud.get_color_choice()
							if self.color != None:
								print("Color choice: ", self.color)
								self.play()
						else:
							self.cardIdx = self.hud.clickOnCard()
							if self.cardIdx != None:
								self.play()
				buttons_state = self.hud.event_handler(event, ask_bluff, ask_p2, self.game["won"])
				if self.hud.eventButtonCounter(event):
					self.network.send("uno")
				if buttons_state != None:
					if ask_bluff:
						if buttons_state["denounce"]:
							self.game = self.network.send("denounce")
						elif buttons_state["skip"]:
							self.game = self.network.send("dontdenonce")
					elif ask_p2:
						if buttons_state["skip"]:
							self.game = self.network.send("skipp2")
					elif self.game["won"]:
						if buttons_state["restart"]:
							self.game = self.network.send("reset")
