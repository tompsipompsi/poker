import unittest
from hand import Hand
from card import Card

class TestPokerHand(unittest.TestCase):
    '''
    Small set of tests for the functions that look for poker hands.
    '''
    def test_two_pairs_correct_list(self):
        '''
        Tests check_two_pairs -function from hand.py with correct input list.
        '''
        card_list = [Card("C", 2), Card("D", 2), Card("S", 6), Card("D", 6), Card("H", 13)]
        
        hand = Hand(card_list)
        hand.check_poker_hands()
        
        self.assertEqual(True, hand.two_pairs, "check_two_pairs with correct list not working")

    def test_two_pairs_incorrect_list(self):
        '''
        Tests check_two_pairs -function from hand.py with incorrect input list.
        '''
        card_list = [Card("C", 2), Card("D", 5), Card("S", 6), Card("D", 6), Card("H", 13)]
        
        hand = Hand(card_list)
        hand.check_poker_hands()
        
        self.assertEqual(False, hand.two_pairs, "check_two_pairs with incorrect list not working")
    
    def test_two_pairs_three_same_in_list(self):
        '''
        Tests check_two_pairs -function from hand.py with incorrect input list 
        that contains three same values.
        '''
        card_list = [Card("C", 2), Card("H", 6), Card("S", 6), Card("D", 6), Card("H", 13)]
        
        hand = Hand(card_list)
        hand.check_poker_hands()
        
        self.assertEqual(False, hand.two_pairs, "check_two_pairs with three same values in a list not working")
        
    def test_two_pairs_full_house_list(self):
        '''
        Tests check_two_pairs -function from hand.py with incorrect input list 
        that contains full house.
        The check_two_pairs -function works also if the three of a kind are first and then pair.
        '''
        card_list = [Card("C", 2), Card("D", 2), Card("S", 6), Card("D", 6), Card("H", 6)]
        
        hand = Hand(card_list)
        hand.check_poker_hands()
        
        self.assertEqual(False, hand.two_pairs, "check_two_pairs with full house in a list not working")
    
    def test_straight_correct_list(self):
        '''
        Tests check_straight -function from hand.py with correct input list.
        '''
        card_list = [Card("C", 2), Card("D", 3), Card("S", 4), Card("D", 5), Card("H", 6)]
        
        hand = Hand(card_list)
        hand.check_poker_hands()
        
        self.assertEqual(True, hand.straight, "check_straight with correct list not working")

    def test_straight_incorrect_list(self):
        '''
        Tests check_straight -function from hand.py with incorrect input list.
        '''
        card_list = [Card("C", 2), Card("D", 3), Card("S", 4), Card("D", 6), Card("H", 6)]
        
        hand = Hand(card_list)
        hand.check_poker_hands()
        
        self.assertEqual(False, hand.straight, "check_straight with incorrect list not working")

    def test_flush_correct_list(self):
        '''
        Tests check_flush -function from hand.py with correct input list.
        '''
        card_list = [Card("C", 2), Card("C", 3), Card("C", 6), Card("C", 10), Card("C", 12)]
        
        hand = Hand(card_list)
        hand.check_poker_hands()
        
        self.assertEqual(True, hand.flush, "check_flush with correct list not working")

    def test_flush_incorrect_list(self):
        '''
        Tests check_flush -function from hand.py with incorrect input list.
        '''
        card_list = [Card("C", 2), Card("D", 5), Card("S", 6), Card("D", 10), Card("H", 12)]
        
        hand = Hand(card_list)
        hand.check_poker_hands()
        
        self.assertEqual(False, hand.flush, "check_flush with incorrect list not working")
        
    def test_straightflush_correct_list(self):
        '''
        Tests if straight flush is found. 
        Finding straight flush uses functions tested in other test functions so no need to test incorrect list.
        '''
        card_list = [Card("C", 2), Card("C", 3), Card("C", 4), Card("C", 5), Card("C", 6)]
        
        hand = Hand(card_list)
        hand.check_poker_hands()
        
        self.assertEqual(True, hand.straightflush, "Straight flush was not found")

if __name__ == '__main__':
    unittest.main(verbosity=2)
    