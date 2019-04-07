class Card(object):

    valueTable = {'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
    valueTable.update({str(i): i for i in range(2, 11)})

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.valueTable[self.rank]

    def __repr__(self):
        return self.rank + ' of ' + self.suit
