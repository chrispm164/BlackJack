class Player:

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        total = 0
        for c in self.hand:
            total += c.value
        while any(c.rank == 'Ace' for c in self.hand) and total <= 11:
            total += 10
        return total
