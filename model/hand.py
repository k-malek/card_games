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
        ''' value setter'''
        self.value=value

    def return_card(self,pos):
        ''' removes card from a hand by its {pos}ition'''
        pos=pos if pos<0 else pos-1
        try:
            card=self.cards[pos]
            self.cards.remove(card)
        except IndexError:
            print(f'Currently player has only {len(self.cards)} cards in this hand!')
            return None
        return card

    def return_cards(self):
        ''' removes all cards from a hand'''
        cards=self.cards
        self.cards=[]
        return cards