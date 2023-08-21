''' Model for deck of playing cards deck object'''

from random import shuffle
import card_games.model.card as c

class Deck:
    ranks=[str(x) for x in range(2,11)]+['J','Q','K','A']
    suits=['\u2666','\u2665','\u2663','\u2660']

    def __init__(self,start_from='2',end_on='A',amount_of_jokers=0,amount_of_copies=1):
        if start_from not in Deck.ranks or end_on not in Deck.ranks or Deck.ranks.index(end_on)<Deck.ranks.index(start_from):
            raise ValueError("Proper starting and ending point consist of string - from '2' to 'A'")
        if amount_of_jokers<0 or amount_of_copies<=0:
            raise ValueError("Number of jokers must be positive, number of copies must be more than 0")
        self.pile=[]
        self.fill_with_cards(start_from,end_on,amount_of_jokers,amount_of_copies)

    def fill_with_cards(self,start_from,end_on,amount_of_jokers,amount_of_copies):
        '''
            Setup for a pile of c.Cards in deck:
            1) Adds regular c.Cards with ranks ranging from start_from to end_on
            2) Adds jokers (amount_of_jokers)
            3) Adds copies of itself (amount_of_copies) 
        '''
        self.pile=[c.Card(rank,suit)
                   for rank in Deck.ranks[Deck.ranks.index(start_from):Deck.ranks.index(end_on)+1]
                   for suit in Deck.suits]
        self.pile+=[c.Card('Joker') for i in range(amount_of_jokers)]
        pile=self.pile[:]
        for i in range(amount_of_copies-1): 
            self.pile.extend(pile)

    def shuffle_pile(self):
        '''Shuffles the pile of card (randomizes positions of card.in a deck)'''
        shuffle(self.pile)

    def draw_cards(self,amount=1):
        '''
            Returns and removes <amount> of topmost (last) cards from a pile
            If there are not enough cards in hand, returns empty list
        '''
        if amount>len(self.pile):
            raise IndexError("There's not enough cards in a deck!")
        cards=self.pile[-amount:]
        del self.pile[-amount:]
        return cards

    def return_cards(self,cards,do_shuffle=True):
        '''
            Returns all provided cards (as list, which may contain single cards 
            as well as list of cards (ex. hands)) to the pile
            than the pile is shuffled (may be ommited with optional argument do_shuffle=False)
        '''
        if isinstance(cards,c.Card):
            self.pile.append(cards)
        else:
            for card_group in cards:
                if isinstance(card_group,list):
                    self.pile+=card_group
                else:
                    self.pile.append(card_group)
        
        if do_shuffle:
            self.shuffle_pile()
