#!/usr/bin/env python3
import imp


import pygame

def create_card(filepath):
    return pygame.image.load(filepath)

def print_deck(filepathList, screen):
    y = 50
    x = 10
    cardList = []
    for i in range(len(filepathList)):
        cardList.append(create_card(f"asset/cards/{filepathList[i]}"))
        screen.blit(cardList[i], (x,y))
        print(filepathList[i])
        x = x + 40
    return cardList
