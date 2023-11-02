from abc import abstractmethod
from typing import Literal, Self

from colors import Color

class RankClass:
    def __init__(self, value: ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        self.value = value
    
    def __eq__(self, other: Self) -> bool:
        return self.value == other.value
    
    def __lt__(self, other: Self) -> bool:
        if self.value == other.value:
            return False
        if self.value == 'A':
            return True
        if other.value == 'A':
            return False
        return self.value < other.value
    
    def __str__(self):
        return str(self.value)

AceRank = RankClass("A")
NumberRanks = [RankClass(i) for i in range(2, 11)]

class Card:
    def __init__(self, color: Color, rank: RankClass):
        self.color = color
        self.rank = rank

    @property
    def value(self):
        if self.rank != AceRank:
            return self.rank.value
        else:
            return 0

    @property
    def multiplier(self):
        if self.rank == AceRank:
            return 1
        else:
            return 0

    def __repr__(self) -> str:
        return f"Card({self.color}, {self.rank})"

    def __hash__(self) -> int:
        return hash(repr(self))

    def __eq__(self, other) -> bool:
        return (self.color, self.rank) == (other.color, other.rank)

    def __lt__(self, other) -> bool:
        return (self.color, self.rank) < (other.color, other.rank)


class AceCard(Card):
    def __init__(self, color: Color):
        super().__init__(color, AceRank)


class NumberCard(Card):
    def __init__(self, color: Color, rank: RankClass):
        super().__init__(color, rank)
