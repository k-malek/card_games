''' Model of playing card object'''
class Card:
    def __init__(self, rank, suit=None, value=None):
        self.rank=rank
        self.suit=suit
        self.value=value

    def __str__(self):
        return self.rank+self.suit if self.suit else self.rank
    
    def __repr__(self):
        return self.rank+self.suit if self.suit else self.rank