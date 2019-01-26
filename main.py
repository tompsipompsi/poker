'''
This program creates a shuffled deck of 52 cards, picks three hands from the deck each
containing five cards, and analyzes these hands for the following poker hands:
two pairs, straight, flush and straight flush.
'''

from deck import Deck
from os import remove

def main():
    #Removes any previously created file where poker hands have been saved.
    #This needs to be done because function that saves hands uses append mode when writing to file,
    #otherwise the file could contain information from previous runs and cause confusion.
    try:
        remove("analysis.txt")
    except OSError:
        pass

    #Creates the deck.
    deck = Deck()
    
    #Creates three hands from the deck.
    hand1 = deck.create_hand(0, 5)
    hand2 = deck.create_hand(5, 10)
    hand3 = deck.create_hand(10, 15)

    #Checks the hands for any poker hands.
    hand1.check_poker_hands()
    hand2.check_poker_hands()
    hand3.check_poker_hands()
    
    #Saves hands to file.
    hand1.save_to_file(1)
    hand2.save_to_file(2)
    hand3.save_to_file(3)

if __name__ == '__main__':
    main()

