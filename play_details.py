from typing import Optional, Tuple

from play import DiscardToPile, DrawFromDeck, DrawFromPile, Play, PlayToPile


class PlayDetails:
    def __init__(self):
        self.reset()

    def reset(self):
        self.chosen_card_pos: Optional[int] = None
        self.plays: Tuple[Optional["Play"], Optional["Play"]] = [None, None]

    def set_card_pos(self, card_pos: int):
        if card_pos < 0 or card_pos > 7:
            raise Exception("Card position out of range")
        self.chosen_card_pos = card_pos

    def set_play(self, play: "Play"):
        if self.plays[0] is None:
            self.plays[0] = play
        elif self.plays[1] is None:
            self.plays[1] = play
        else:
            raise Exception("Already chosen two plays")

    def validate(self):
        # only validate everything is chosen
        if self.chosen_card_pos is None:
            raise Exception("No card is chosen")
        if self.plays[0] is None or self.plays[1] is None:
            raise Exception("You need to choose two plays")
        
    def __repr__(self):
        return f'PlayDetails(chosen_card_pos={self.chosen_card_pos}, plays=[{self.plays}])'
