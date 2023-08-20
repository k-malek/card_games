'''
Tests for Player model
'''
import unittest
from card_games.model.deck import Deck
from card_games.model.hand import Hand
from card_games.model.player import Player
from card_games.utils.custom_exceptions import HandIndexException,CardIndexException

class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        ''' test for player object initialization'''
        player_1=Player('Mark')
        self.assertEqual('Mark',player_1.name)
        self.assertEqual('0',player_1.points)
        self.assertEqual(1,len(player_1.hands))
        self.assertIsInstance(player_1.hands[0],Hand)
        player_2=Player('Bob',1000)
        self.assertEqual('Bob',player_2.name)
        self.assertEqual('1000',player_2.points)
        self.assertEqual(1,len(player_2.hands))
        player_3=Player('Wade',2000,3)
        self.assertEqual('Wade',player_3.name)
        self.assertEqual('2000',player_3.points)
        self.assertEqual(3,len(player_3.hands))
        self.assertIsInstance(player_3.hands[1],Hand)
        self.assertIsInstance(player_3.hands[2],Hand)

    def test_player_incorrect_init(self):
        ''' test for player object initialization with incorrect input'''
        with self.assertRaises(ValueError):
            Player("")
        with self.assertRaises(ValueError):
            Player("daujisdhoahodihasohdaosdhi")

    def test_player_one_hand_draw(self):
        ''' test for player with one hand drawing a cards'''
        deck=Deck()
        deck.shuffle_pile()
        player=Player("Sean")
        player.add_cards_to_hand(deck.draw_cards())
        self.assertEqual(1,len(player.hands[0]))

        player.add_cards_to_hand(deck.draw_cards(4))
        self.assertEqual(5,len(player.hands[0]))

        # accessing incorrect index for a hand raises exception
        with self.assertRaises(HandIndexException):
            player.add_cards_to_hand(deck.draw_cards(5),1)

    def test_player_one_hand_return(self):
        ''' test for player with one hand returning a cards'''
        deck=Deck()

        player=Player("Vinny")
        player.add_cards_to_hand(deck.draw_cards(10))
        self.assertEqual(10,len(player.hands[0]))
        self.assertEqual(42,len(deck.pile))

        deck.return_cards(player.return_cards_from_hand([0]))
        self.assertEqual(9,len(player.hands[0]))
        self.assertEqual(43,len(deck.pile))

        deck.return_cards(player.return_cards_from_hand([5,0,2]))
        self.assertEqual(6,len(player.hands[0]))
        self.assertEqual(46,len(deck.pile))

        # accessing a card with incorrect id raises exception
        with self.assertRaises(CardIndexException):
            deck.return_cards(player.return_cards_from_hand([1,100]))
        self.assertEqual(6,len(player.hands[0]))
        self.assertEqual(46,len(deck.pile))

        deck.return_cards(player.return_all_cards())
        self.assertEqual(1,len(player.hands))
        self.assertEqual(0,len(player.hands[0]))
        self.assertEqual(52,len(deck.pile))

    def test_player_multiple_hands(self):
        ''' test for player with multiple hands'''
        player=Player("Astroid",amount_of_hands=3)
        self.assertEqual(3,len(player.hands))
        
        deck=Deck()
        deck.shuffle_pile()
        for hand in player.hands:
            hand.add_cards(deck.draw_cards(5))
            self.assertEqual(5,len(hand))
        self.assertEqual(37,len(deck.pile))
        
        player.add_cards_to_hand(deck.draw_cards(3),1)
        self.assertEqual(5,len(player.hands[0]))
        self.assertEqual(8,len(player.hands[1]))
        self.assertEqual(5,len(player.hands[2]))
        self.assertEqual(34,len(deck.pile))
        
        deck.return_cards(player.return_cards_from_hand([1]))
        self.assertEqual(4,len(player.hands[0]))
        self.assertEqual(8,len(player.hands[1]))
        self.assertEqual(5,len(player.hands[2]))
        self.assertEqual(35,len(deck.pile))

        deck.return_cards(player.return_all_cards_from_hand(0))
        self.assertEqual(0,len(player.hands[0]))
        self.assertEqual(8,len(player.hands[1]))
        self.assertEqual(5,len(player.hands[2]))
        self.assertEqual(39,len(deck.pile))

        deck.return_cards(player.return_all_cards())
        self.assertEqual(3,len(player.hands))
        self.assertEqual(0,len(player.hands[0]))
        self.assertEqual(0,len(player.hands[1]))
        self.assertEqual(0,len(player.hands[2]))
        self.assertEqual(52,len(deck.pile))