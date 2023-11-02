import random

from cards import AceCard, NumberCard, NumberRanks
from colors import Color


class Deck:
    def __init__(self):
        self.deck = []
        self.reset()

    def seed(self, seed: int):
        random.seed(seed)

    def reset(self):
        self.deck = []
        for color in Color:
            self.deck.append(AceCard(color))
            self.deck.append(AceCard(color))
            self.deck.append(AceCard(color))
            for number_rank in NumberRanks:
                self.deck.append(NumberCard(color, number_rank))

        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

    def deal_hand(self):
        self.deck, new_hand = self.deck[:-8], self.deck[-8:]
        new_hand.sort()
        return new_hand

    def length(self):
        return len(self.deck)

    def is_empty(self):
        return len(self.deck) == 0
