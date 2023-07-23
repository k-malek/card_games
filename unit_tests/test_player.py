'''
Tests for Player model
'''
import unittest
from card_games.model.deck import Deck
from card_games.model.hand import Hand
from card_games.model.player import Player

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
        player.draw_card(deck)
        self.assertEqual(1,len(player.hands[0]))

        player.draw_cards(deck,amount=4)
        self.assertEqual(5,len(player.hands[0]))

        #draw a card to a second - non existant - hand (exception handled)
        player.draw_card(deck,hand_pos=2)
        #deck and hand are unaffected
        self.assertEqual(47,len(deck.pile))
        self.assertEqual(5,len(player.hands[0]))

    def test_player_one_hand_return(self):
        ''' test for player with one hand returning a cards'''
        deck=Deck()

        player=Player("Vinny")
        player.draw_cards(deck,amount=10)
        self.assertEqual(10,len(player.hands[0]))

        player.return_card(deck,card_pos=1,deck_pos='t')
        self.assertEqual(9,len(player.hands[0]))
        self.assertEqual(43,len(deck.pile))

        #return a card from a second - non existant - hand (exception handled)
        player.return_card(deck,hand_pos=2)
        self.assertEqual(9,len(player.hands[0]))
        self.assertEqual(43,len(deck.pile))

        #return a card with index higher than amount of cards (exception handled)
        player.return_card(deck,card_pos=10)
        self.assertEqual(9,len(player.hands[0]))
        self.assertEqual(43,len(deck.pile))

        player.return_all_cards(deck)
        self.assertEqual(1,len(player.hands))
        self.assertEqual(52,len(deck.pile))

    def test_player_multiple_hands(self):
        ''' test for player with multiple hands'''
        player=Player("Astroid",amount_of_hands=3)
        self.assertEqual(3,len(player.hands))
        
        deck=Deck()
        deck.shuffle_pile()
        for hand in player.hands:
            for _ in range(5):
                hand.draw_card(deck)
            self.assertEqual(5,len(hand))
            hand.draw_cards(deck,2)
            self.assertEqual(7,len(hand))
        self.assertEqual(31,len(deck.pile))
        
        player.draw_cards(deck,3,1)
        self.assertEqual(7,len(player.hands[0]))
        self.assertEqual(10,len(player.hands[1]))
        self.assertEqual(7,len(player.hands[2]))
        self.assertEqual(28,len(deck.pile))
        
        player.return_card(deck)
        self.assertEqual(6,len(player.hands[0]))
        self.assertEqual(10,len(player.hands[1]))
        self.assertEqual(7,len(player.hands[2]))
        self.assertEqual(29,len(deck.pile))

        player.hands[0].return_cards_to_deck(deck)
        self.assertEqual(0,len(player.hands[0]))
        self.assertEqual(10,len(player.hands[1]))
        self.assertEqual(7,len(player.hands[2]))
        self.assertEqual(35,len(deck.pile))

        player.return_all_cards(deck)
        self.assertEqual(3,len(player.hands))
        self.assertEqual(0,len(player.hands[0]))
        self.assertEqual(0,len(player.hands[1]))
        self.assertEqual(0,len(player.hands[2]))
        self.assertEqual(52,len(deck.pile))