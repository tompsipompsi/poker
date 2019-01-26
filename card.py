class Card():
    '''
    Represents a single card which will be placed into a deck.
    '''
    def __init__(self, suit, rank):
        '''
        Constructs the card with the given suit and rank.
        '''
        self.suit = suit
        self.rank = rank
        