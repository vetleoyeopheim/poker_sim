# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 08:57:39 2024

@author: Vetle
"""

import numpy as np
import game
import deck
from itertools import combinations



N = 100000

ref_deck = deck.Deck()
deck_list = ref_deck.list_form()
combos = list(combinations(deck_list,2))
scores = {hand: {"wins": 0, "losses": 0} for hand in combos}

for n in range(N):

    gm = game.Game(5)
    gm.play_game()
    winning_hand = gm.winning_hand
    winning_hand = [(winning_hand[i].rank,winning_hand[i].suit) for i in range(len(winning_hand))]
    winning_hand = tuple(sorted(winning_hand))
    scores[(winning_hand)]['wins'] += 1
    
    
    
sorted_scores = sorted(scores.items(), key=lambda item: item[1]["wins"], reverse=True)

wins_array = np.array([hand_info["wins"] for hand_info in scores.values()])