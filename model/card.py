''' Model of playing card object'''
class Card:
    def __init__(self, rank, suit=None, value=None,is_hidden=False):
        self.rank=rank
        self.suit=suit
        self.value=value
        self.is_hidden=is_hidden

    def __str__(self):
        if self.is_hidden:
            return "HIDDEN"
        return self.rank+self.suit if self.suit else self.rank
    
    def __repr__(self):
        return self.rank+self.suit if self.suit else self.rank