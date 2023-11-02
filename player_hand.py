from typing import List

class PlayerHand:
    def __init__(self):
        self.hand = []

    def add_card(self, card: "Card"):
        self.hand.append(card)
        self.hand.sort()

    def get_card(self, card_pos: int):
        return self.hand[card_pos]

    def get_new_hand(self, hand: List["Card"]):
        self.hand = hand

    def reset(self):
        self.hand = []

    def pop_card(self, pos: int):
        return self.hand.pop(pos)

    def length(self):
        return len(self.hand)
    
    def __str__(self):
        return str(self.hand)
