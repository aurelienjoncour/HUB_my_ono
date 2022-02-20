class Player:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        self.should_play = False
        self.deck = []

    def isDeckPlayable(self):
        for card in self.deck:
            if card.playable:
                return True
        return False

    def updatePlayableCard(self, top_card):
        for card in self.deck:
            card.is_playable(top_card)