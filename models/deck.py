''' Model for deck of playing cards deck object'''
from card_games.models.card import Card
from random import shuffle,randint

class Deck:
    ranks=[str(x) for x in range(2,11)]+['J','Q','K','A']
    suits=['\u2666','\u2665','\u2663','\u2660']

    def __init__(self,start_from='2',end_on='A',no_of_jokers=0,no_of_copies=1):
        self.pile=[]
        self.fill_with_cards(start_from,end_on,no_of_jokers,no_of_copies)

    def fill_with_cards(self,start_from,end_on,no_of_jokers,no_of_copies):
        '''
            Setup for a pile of cards in deck:
            1) Adds regular cards with ranks ranging from start_from to end_on
            2) Adds jokers (no_of_jokers)
            3) Adds copies of itself (no_of_copies) 
        '''
        self.pile=[Card(rank,suit)
                   for rank in Deck.ranks[Deck.ranks.index(start_from):Deck.ranks.index(end_on)+1]
                   for suit in Deck.suits]
        self.pile+=[Card('Joker') for i in range(no_of_jokers)]
        for i in range(no_of_copies-1): 
            self.pile.extend(self.pile[:])

    def shuffle_pile(self):
        '''Shuffles the pile of cards (randomizes positions of cards in a deck)'''
        shuffle(self.pile)

    def draw_card(self):
        '''Returns and removes the topmost (last) card from a pile'''
        return self.pile.pop()

    def return_card(self,card,position='b'):
        '''
            Returns a card to a pile.
            Required parameter:
                card - a Card object to place in a deck
            Optional parameter:
                position ('b','t') - indicates wheather the card is to placed on (t)op or on (b)ottom of a pile.
                                    if anything else given - places a card on a random place in a deck
        '''
        if position=='b':
            self.pile.insert(0,card)
        elif position=='t':
            self.pile.append(card)
        else:
            self.pile.insert(randint(0,len(self.pile)-1),card)
