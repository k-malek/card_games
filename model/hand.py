''' Model for hand (of cards) object'''
from card_games.model.card import Card

class Hand():
    def __init__(self,cards=None):
        self.cards=cards if cards else []
        self.value=0

    def __add__(self,cards):
        if isinstance(cards,Card):
            self.cards.append(cards)
        elif isinstance(cards,list):
            self.cards.extend(cards)
        else:
            raise TypeError("You can only add card or list of cards!")

    def __subs__(self,cards):
        if isinstance(cards,Card):
            self.cards.remove(cards)
        elif isinstance(cards,list):
            for card in cards:
                self.cards.remove(card)
        else:
            raise TypeError("You can only remove card or list of cards!")
        
    def __str__(self):
        return " ".join(self.cards)
    
    def __len__(self):
        return len(self.cards)

    def set_value(self,value):
        self.value=value

    def add_cards(self,cards):
        ''' adds cards to a hand'''
        self.cards+=cards

    def return_cards(self,positions):
        ''' returns cards by a given {positions}'''
        positions.sort(reverse=True)
        print(positions)
        print(positions[0]>len(self.cards))
        if positions[0]>len(self.cards):
            print("Wrong card position provided!")
            return []
        returning_cards=[]
        for pos in positions:
            returning_cards.append(self.cards[pos])
            del self.cards[pos]
        return returning_cards

    def return_all_cards(self):
        ''' removes all cards from a hand'''
        cards=self.cards
        self.cards=[]
        return cards
