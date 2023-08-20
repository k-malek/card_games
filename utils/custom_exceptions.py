class HandIndexException(IndexError):
    ''' Exception for incorrect Hand index from a Player'''
    def __init__(self,player,pos,message=''):
        self.message=f'Currently player {player.name} has only {len(player.hands)} hand(s), requested hand id {pos}' if not message else message
        super().__init__(self.message)

class CardIndexException(IndexError):
    ''' Exception for incorrect Card index from a Hand'''
    def __init__(self,hand,pos,message=''):
        self.message=f'Currently there are only {len(hand.cards)} card(s) in hand, requested card id {pos}' if not message else message
        super().__init__(self.message)