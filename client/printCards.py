#!/usr/bin/env python3
import imp


import pygame

def create_card(filepath):
    return pygame.image.load(filepath)

def print_deck(filepathList, cards):
    y = 50
    x = 10
    cardList = []
    for i in range(len(filepathList)):
        cards.display(filepathList[i], (x, y))
        x = x + 40
    return cardList
