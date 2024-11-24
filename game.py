# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 07:17:15 2024

@author: Vetle
"""


import numpy as np
from itertools import combinations

import deck

class Player:
    
    
    def __init__(self, hand):
        
        self.hand = hand
        
        
    def set_rank(self):
        
        """
        Ranks the hand in a game of Texas Hold'em
        """

class Game:
    
    def __init__(self, player_num):
        
        
        self.player_num = player_num
        self.create_deck()
        
    
    def deal_cards(self):
        
        """
        Instantiate players
        """
        self.players = []
        
        for i in range(self.player_num):
            card1 = self.deck.deck[0] #Take card out from the deck
            self.deck.deck.pop(0)
            card2 = self.deck.deck[0]
            self.deck.deck.pop(0)
            player = Player([card1, card2])
            self.players.append(player)
    
    def create_deck(self):
        """
        Create a deck and shuffle it        
        
        """
        self.deck = deck.Deck()
        self.deck.shuffle_deck()
    
    def play_game(self):
        
        self.deal_cards()
        
        #Create list of community cards
        self.comm_cards = [self.deck.deck[i] for i in range(5)]
        
        #Create list to store player rankings
        rankings = []
        
        for i in range(self.player_num):
            #Update hand of each player with community cards
            full_hand = self.players[i].hand + self.comm_cards
            #full_hand_list = [[full_hand[i].rank,full_hand[i].suit] for i in range(7)]
            combos = list(combinations(full_hand, 5))
            high_rank = -1
            for hand in combos:
                rank = self.determine_hand(hand)
                if rank[0] > high_rank:
                    high_rank = rank[0]
            rankings.append(high_rank)
            
            
            
        #Next find out which player and hand won the game
        max_rank = rankings.index(max(rankings))
        #If two players has the same rank, determine which one has the highest card
        winning_player = self.players[max_rank]
        self.winning_hand = winning_player.hand
        
            
    def determine_hand(self,hand):
        
        ranks = [hand[i].rank for i in range(len(hand))]
        suits = [hand[i].suit for i in range(len(hand))]
            
        is_flush = len(set(suits)) == 1
        is_straight = all(ranks[i] - 1 == ranks[i + 1] for i in range(len(ranks) - 1))
        
        # Special case for Ace-low straight
        if ranks == [12, 3, 2, 1, 0]:
            is_straight = True
            ranks = [4, 3, 2, 1, 0]
        
        rank_count = {rank: ranks.count(rank) for rank in ranks}
        sorted_counts = sorted(rank_count.values(), reverse=True)
        
        #Find the rank of the highest card
        # Add a small number to the highest score to distinguish high cards from low cards
        max_rank = max(ranks)
        rank_add = max_rank * 0.01
        
        # Determine hand type
        if is_flush and is_straight:
            return (9+rank_add if ranks[0] == 12 else 8+rank_add, ranks)  # Royal Flush or Straight Flush
        elif sorted_counts == [4, 1]:
            return (7+rank_add, ranks)  # Four of a Kind
        elif sorted_counts == [3, 2]:
            return (6+rank_add, ranks)  # Full House
        elif is_flush:
            return (5+rank_add, ranks)  # Flush
        elif is_straight:
            return (4+rank_add, ranks)  # Straight
        elif sorted_counts == [3, 1, 1]:
            return (3+rank_add, ranks)  # Three of a Kind
        elif sorted_counts == [2, 2, 1]:
            return (2+rank_add, ranks)  # Two Pair
        elif sorted_counts == [2, 1, 1, 1]:
            return (1+rank_add, ranks)  # One Pair
        else:
            return (0+rank_add, ranks)  # High Card
    
