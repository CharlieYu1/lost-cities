from enum import Enum

from typing import Self

class Color(Enum):
    YELLOW = 0
    BLUE = 1
    WHITE = 2
    GREEN = 3
    RED = 4

    def __lt__(self, other: Self):
        return self.value < other.value