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

    def add_card(self,card):
        ''' adding a card to a hand'''
        self.cards.append(card)

    def add_cards(self,cards):
        ''' adding multiple cards to a hand'''
        self.cards+=cards

    def draw_card(self,deck):
        ''' adding a card to a hand from a deck'''
        self.cards.append(deck.draw_card())

    def draw_cards(self,deck,amount_of_cards):
        ''' adding multiple cards to a hand from a deck'''
        self.cards+=deck.draw_cards(amount_of_cards)

    def return_card(self,pos):
        ''' removes card from a hand by its {pos}ition'''
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

    def return_card_to_deck(self,deck,pos):
        ''' removes card from a hand to a deck by its {pos}ition'''
        try:
            card=self.cards[pos]
            self.cards.remove(card)
        except IndexError:
            print(f'Currently player has only {len(self.cards)} cards in this hand!')
        deck.return_card(card)

    def return_cards_to_deck(self,deck):
        ''' removes all cards from a hand to a deck'''
        cards=self.cards
        self.cards=[]
        deck.return_cards(cards)
