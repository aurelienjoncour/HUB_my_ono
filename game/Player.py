class Player:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        self.deck = []

    def updatePlayableCard(self, top_card):
        for card in self.deck:
            card.is_playable(top_card)