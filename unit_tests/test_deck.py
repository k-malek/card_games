'''
Tests for Deck and Card model
'''
import unittest
import card_games.model.deck as d
import card_games.model.card as c

class TestDeck(unittest.TestCase):
    ''' testing class'''
    def test_deck_init(self):
        ''' test for Deck initialization - correct number of cards'''
        deck=d.Deck(start_from='10',amount_of_copies=2,amount_of_jokers=2)
        self.assertEqual(44,len(deck.pile))

        deck2=d.Deck(start_from='4',end_on='6',amount_of_copies=7,amount_of_jokers=1)
        self.assertEqual(91,len(deck2.pile))

    def test_deck_incorrect_init(self):
        ''' test for incorrect inputs for Deck initialization'''
        with self.assertRaises(ValueError):
            d.Deck(start_from='hakuna matata',amount_of_copies=2,amount_of_jokers=2)

        with self.assertRaises(ValueError):
            d.Deck(start_from='9',end_on='6',amount_of_copies=7,amount_of_jokers=1)
        
        with self.assertRaises(ValueError):
            d.Deck(start_from='6',end_on='9',amount_of_copies=7,amount_of_jokers=-1)

        with self.assertRaises(ValueError):
            d.Deck(start_from='6',end_on='7',amount_of_copies=0,amount_of_jokers=1)

    def test_deck_one_card_methods(self):
        ''' test for drawing and returning card to a pile'''
        deck=d.Deck()
        deck.shuffle_pile()
        self.assertEqual(52,len(deck.pile))

        card=deck.draw_cards()[0]
        self.assertIsInstance(card,c.Card)
        self.assertEqual(51,len(deck.pile))

        deck.return_cards(card,'anywhere')
        self.assertEqual(52,len(deck.pile))
        self.assertIn(card,deck.pile)

    def test_deck_multiple_cards_methods(self):
        ''' test for drawing and returning multiple cards to a pile'''
        deck=d.Deck()
        self.assertEqual(52,len(deck.pile))

        hand1=deck.draw_cards(5)
        hand2=deck.draw_cards(5)
        card=deck.draw_cards()[0]
        self.assertEqual(5,len(hand1))
        self.assertEqual(5,len(hand2))
        self.assertEqual(41,len(deck.pile))

        deck.return_cards([hand1,card,hand2])
        self.assertEqual(52,len(deck.pile))
        self.assertEqual(len(deck.pile),len(set(deck.pile))) #check if there are no duplicate cards

    def test_deck_emptied(self):
        ''' test for checking if no card is returned if requested more cards than in a pile'''
        deck=d.Deck(start_from='2',end_on='2')
        self.assertEqual(4,len(deck.pile))

        hand1=deck.draw_cards(5)
        self.assertEqual(0,len(hand1))
        self.assertEqual(4,len(deck.pile))

        hand1=deck.draw_cards(4)
        self.assertEqual(4,len(hand1))
        self.assertEqual(0,len(deck.pile))

    def test_two_decks(self):
        ''' test for multiple decks are independedly handled'''
        deck1=d.Deck()
        deck2=d.Deck()
        deck1.shuffle_pile()
        self.assertEqual(str(c.Card('A','\u2660')),str(deck2.draw_cards()[0]))
        self.assertEqual(52,len(deck1.pile))
        self.assertEqual(51,len(deck2.pile))