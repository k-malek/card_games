''' Model for deck of player object'''
from card_games.model.hand import Hand

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

    def draw_card(self,deck,hand_pos=1):
        ''' draw one card from given {deck} to the players hand with id of {hand_pos}'''
        try:
            self.hands[hand_pos-1]+deck.draw_card()
        except IndexError:
            print(f'Currently player {self.name} has only {len(self.hands)} hands!')

    def draw_cards(self,deck,amount=1,hand_pos=1):
        ''' draw {amount} of cards from given {deck} to the players hand with id of {hand_pos}'''
        if amount<1:
            raise ValueError('Please, pick more cards than that!')
        try:
            self.hands[hand_pos-1]+deck.draw_cards(amount)
        except IndexError:
            print(f'Currently player {self.name} has only {len(self.hands)} hands!')

    def return_card(self,deck,hand_pos=1,card_pos=-1,deck_pos='b'):
        '''
            Returns a card to a {deck} from a hand.
            Card is indicated by hand id (hand_pos) and its position in that hand (card_pos).
            By default card is picked as a last card from the main hand (first hand).
            Additional optional parameter:
                deck_pos ('b','t') - indicates wheather the card is to placed on 
                        (t)op or on (b)ottom of a {deck} pile. If anything else 
                        given - places a card on a random place in a {deck}}
        '''
        card=None
        try:
            card=self.hands[hand_pos-1].return_card(card_pos)
        except IndexError:
            print(f'Currently player {self.name} has only {len(self.hands)} hands!')
        if card:
            deck.return_card(card,deck_pos)

    def return_all_cards(self,deck,do_shuffle=True):
        ''' 
            returns all cards from all hands to a deck,
            deck is shuffled (may be ommited with optional argument do_shuffle=False)
            hands are reset to expected amount
        '''
        all_cards=[]
        for hand in self.hands:
            all_cards+=hand.return_cards()
        deck.return_cards(all_cards,do_shuffle)
        self.hands=[Hand() for i in range(self.amount_of_hands)]


    def show_hand(self,hand_pos=1):
        ''' returns string of cards in players hand with id of {hand_pos}'''
        try:
            return str(self.hands[hand_pos-1])
        except IndexError:
            print(f'Currently player {self.name} has only {len(self.hands)} hands!')