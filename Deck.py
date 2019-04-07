from Card import *

class Deck():

    def __init__(self):
        self.deck = []
        suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for s in suit:
            for v in value:
                self.deck.append(Card(s,v))

    def shuffle(self):
        import random
        return random.shuffle(self.deck)

    def deal_card(self):
        import random
        if self.deck == []:
            self.deck = Deck().deck
            random.shuffle(self.deck)
        c = self.deck[0]
        self.deck.remove(c)
        return c

    def get_size(self):
        return len(self.deck)
