from colors import Color
from loguru import logger

class Column:
    def __init__(self, color: Color):
        self.column = []
        self.color = color

    def reset(self):
        self.column = []

    def play(self, card: "Card"):               
        self.column.append(card)
    
    @property
    def top_card_value(self):
        if self.length() > 0:
            return self.column[-1].value
        else:
            return 0

    def length(self):
        return len(self.column)

    @property
    def is_empty(self):
        return self.length() == 0

    @property
    def score(self):
        if self.is_empty:
            return 0
        base_value = sum(card.value for card in self.column) - 20
        multiplier = sum(card.multiplier for card in self.column) + 1
        bonus = (self.length() >= 8) * 20
        return base_value * multiplier + bonus
    
    def __str__(self) -> str:
        return str([card.value for card in self.column])
