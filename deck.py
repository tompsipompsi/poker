from card import Card
from hand import Hand
from random import shuffle

class Deck():
    '''
    Represents a deck that contains 52 card objects.
    '''
    def __init__(self):
        '''
        Constructs the deck and shuffles it.
        '''
        #List suits contains all four suits used in card deck. 
        #The suits are Hearts, Diamonds, Clubs and Spades.
        self.suits = ['H', 'D', 'C', 'S'] 
        
        #List ranks contains all 13 ranks used in card deck.
        #Ranks are numbers from two to ten, Jack (11), Queen (12), King (13) and Ace (14).
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        
        #Creates the deck. Deck must be saved into variable in order to use it elsewhere.
        self.deck = self.create_deck()
        
        #Shuffles the deck.
        self.shuffle_deck()
        
    def create_deck(self):
        '''
        Creates a deck of cards which contains one card of each suit and each rank.
        This created deck will be in order.
        '''
        deck = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        return deck
    
    def shuffle_deck(self):
        '''
        Shuffles the previously created deck.
        '''
        shuffle(self.deck)
        
    def create_hand(self, lower_limit, upper_limit):
        '''
        Creates a hand of cards from the deck between the given limits.
        '''
        hand = self.deck[lower_limit:upper_limit]
        return Hand(hand)
