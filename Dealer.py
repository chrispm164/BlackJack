from Player import *


class Dealer(Player):

    def __init__(self):
        Player.__init__(self)

    def dealer_turn(self, card):
        while self.hand_value() < 17:
            self.add_card(card)
