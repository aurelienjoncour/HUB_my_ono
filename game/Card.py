from enum import IntEnum

class Color(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3

class Value(IntEnum):
    ZERO = 0,
    ONE = 1,
    TWO = 2,
    THREE = 3,
    FOUR = 4,
    FIVE = 5,
    SIX = 6,
    SEVEN = 7,
    HEIGHT = 8,
    NINE = 9,
    SKIP = 10,
    REVERSE = 11,
    PLUS_TWO = 12

class Bonus(IntEnum):
    JOKER = 1,
    SUPER_JOKER = 2

class Card:
    colors = ["r", "g", "b", "y"]
    regular = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "stop", "reverse", "p2"]
    special = [None, "m_s", "m_p4"]

    def __init__(self, card, color) -> None:
        if (type(card) != Bonus and type(card) != Value):
            raise Exception("Card: ctor type error for card argument")
        if (type(color) != Color and type(card) != Bonus):
            raise Exception("Card: ctor type error for color argument")
        
        if type(card) == Bonus:
            self.value = card
            self.color = None
            self.filepath = f"uno_{self.special[card]}.png"
        else:
            self.value = card
            self.color = color
            self.filepath = f"uno_{self.colors[color]}_{self.regular[card]}.png"
        self.playable = False

    def is_playable(self, card):
        if self.color == card.color or self.value == card.value:
            print("True: ", self.filepath)
            self.playable = True
        elif self.color == None:
            print("True: ", self.filepath)
            self.playable = True
        else:
            print("False: ", self.filepath)
            self.playable = False