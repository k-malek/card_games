''' Model for deck of player object'''
from card_games.model.hand import Hand
from card_games.utils.custom_exceptions import HandIndexException

class Player():
    def __init__(self,name,start_points=0,amount_of_hands=1):
        if len(name) not in range(3,15):
            raise ValueError("Name has to contain 3-14 characters")
        if amount_of_hands < 1:
            raise ValueError("Amount of hands has to be greater than zero")
        self.name=name
        self._points=start_points
        self.hands=[Hand() for i in range(amount_of_hands)]
        self.amount_of_hands=amount_of_hands

    @property
    def points(self):
        ''' property for storing amount of points/cash of a player'''
        return str(self._points)

    @points.setter
    def points(self,new_points):
        self._points=new_points

    def add_hand(self,cards=None,pos=None):
        ''' 
            adds new hand for a player with a given {cards} 
            (or an empty hand if None cards provided)
            hand can be set to a specific position in players hands list ({pos})
        '''
        pos = pos if pos else len(cards)
        self.hands.insert(pos,Hand(cards))

    def add_cards_to_hand(self,cards,hand_pos=0):
        ''' add {cards} to the players hand with id of {hand_pos}'''
        if hand_pos<0 or hand_pos>=len(self.hands):
            raise HandIndexException(self,hand_pos)
        self.hands[hand_pos].add_cards(cards)

    def return_cards_from_hand(self,positions,hand_pos=0):
        ''' returns {cards} from the players hand with id of {hand_pos} and with {positions} in hand'''
        if hand_pos<0 or hand_pos>=len(self.hands):
            raise HandIndexException(self,hand_pos)
        cards=[]
        cards = self.hands[hand_pos].return_cards(positions)
        return cards
    
    def return_all_cards_from_hand(self,hand_pos=0):
        ''' returns {cards} from the players hand with id of {hand_pos} and with {positions} in hand'''
        if hand_pos<0 or hand_pos>=len(self.hands):
            raise HandIndexException(self,hand_pos)
        return self.hands[hand_pos].return_all_cards()

    def return_all_cards(self):
        ''' 
            returns all cards from all hands to a deck,
            deck is shuffled (may be ommited with optional argument do_shuffle=False)
            hands are reset to expected amount
        '''
        all_cards=[]
        for hand in self.hands:
            all_cards+=hand.return_all_cards()
        self.hands=[Hand() for i in range(self.amount_of_hands)]
        return all_cards


    def show_hand(self,hand_pos=0):
        ''' returns string of cards in players hand with id of {hand_pos}'''
        if hand_pos<0 or hand_pos>=len(self.hands):
            raise HandIndexException(self,hand_pos)
        return str(self.hands[hand_pos])