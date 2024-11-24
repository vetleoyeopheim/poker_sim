# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 07:07:36 2024

@author: Vetle
"""


import random



class Card:

    def __init__(self, rank, suit):
        

        self.rank = rank
        self.suit = suit
        
        

        

class Deck:
    

    """
    Craete a standard deck of 52 cards with 13 ranks and 4 suits
    """
    

    def __init__(self):
        
        self.create_deck()
        
        
    def create_deck(self):
        
        ranks = 13      #Rank is 0-12, with 0=2 and 12 = ace
        suits = 4       #suits are 0:Clubs, 1:Diamonds, 2:Hearts, 3:Spades
        self.deck = []
        
        for i in range(ranks):
            for j in range(suits):
                card = Card(i,j)
                self.deck.append(card)
                
                
                
    def shuffle_deck(self):
        
        random.shuffle(self.deck)
        
    def list_form(self):
        """
        Get a list of tuples of numerical values instead of card object
        """
        
        card_list = [(self.deck[i].rank,self.deck[i].suit) for i in range(len(self.deck))]
        
        return card_list
        
