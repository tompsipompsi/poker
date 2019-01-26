class Hand():
    '''
    Represents a single hand of cards, contains five card objects.
    '''
    def __init__(self, card_list):
        '''
        Constructs the hand with the given set of cards. 
        Also presets any poker hands the hand may contain as false.
        '''
        self.hand = card_list 
        self.two_pairs = False
        self.straight = False
        self.flush = False
        self.straightflush = False
        
    def check_poker_hands(self):
        '''
        Checks if the hand contains any poker hands by using helper functions.
        '''
        suits = []
        ranks = []
        for card in self.hand:
            suits.append(card.suit)
            ranks.append(card.rank)
        
        #check_straight and check_two_pairs functions require sorted list.
        #This sort does not modify the original hand, which will stay untouched.
        ranks.sort()
        
        #Checks the hand for two pairs.
        self.two_pairs = self.check_two_pairs(ranks)
        
        #Checks the hand for straight.
        self.straight = self.check_straight(ranks)
        
        #Checks the hand for flush.
        self.flush = self.check_flush(suits)
        
        #Checks straight flush.
        #Sets straight and flush as false to avoid confusion.
        if self.straight and self.flush:
            self.straightflush = True
            self.straight = False
            self.flush = False
    
    def check_two_pairs(self, ranks):
        '''
        Checks the hand for two pairs.
        "ranks" list is sorted, so this function compares every value in the list to 
        previous value starting from index one. 
        Returns True if two pairs have been found, else returns False.
        '''
        i = 1
        pair_count = 0
        
        #used_values represent values in the ranks list that have been identified as pair. 
        #Every time pair is found, the value of the pair is saved to either used_value1 or 2.
        used_value1 = 0
        used_value2 = 0
        
        while i < 5:
            if ranks[i] == ranks[i-1]:
                pair_count += 1
                
                #Value of the found pair is saved to the used_value variable that have not been yet used.
                if used_value1 == 0:
                    used_value1 = ranks[i]
                else:
                    used_value2 = ranks[i]
            i += 1

        #used_values need to be compared here in order to identify poker hand that contain three of a kind.
        #One pair and full house are identified by using the pair_count.
        if pair_count == 2 and used_value1 != used_value2:
            return True
        else:
            return False
    
    def check_straight(self, ranks):
        '''
        Checks the hand for straight. 
        "ranks" list is sorted, so this function compares every value in the list 
        subtracted by one to previous value starting from index one. 
        Returns False if any value is not one lower than previous value, else returns True.
        '''
        i = 1
        while i < 5:
            if ranks[i] - 1 != ranks[i-1]:
                return False
            i += 1
        return True
    
    def check_flush(self, suits):
        '''
        Checks the hand for flush.
        Compares first value in the "suits" list to every value in the same list. If any
        value is different than first, returns False. Else returns True.
        '''
        for suit in suits:
            if suits[0] != suit:
                return False
        return True
        
    def save_to_file(self, n):
        '''
        Saves the hand to file named analysis.txt 
        with the info about the poker hands the hand may contain.
        File is opened in the append mode so that possible savings 
        from other hands are not removed.
        '''
        file = open("analysis.txt", "a")
        file.write("The hand number " + str(n) + " is: \n")
        
        for card in self.hand:
            file.write(card.suit)
            file.write(str(card.rank))
            file.write(" ")
        file.write("\n")
        
        if self.two_pairs or self.straight or self.straight or self.straightflush:
            file.write("This hand contains following poker hand: \n")
            
            if self.two_pairs:
                file.write("Two pairs\n")
            elif self.straight: 
                file.write("Straight\n")
            elif self.flush:
                file.write("Flush\n")
            elif self.straightflush:
                file.write("Straight flush\n")
        else:
            file.write("This hand does not contain any poker hands.\n")
        
        file.write("\n")
        file.close()
    