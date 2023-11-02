from colors import Color


class DiscardPile:
    def __init__(self, color: Color):
        self.discard_pile = []
        self.color = color

    def reset(self):
        self.discard_pile = []

    def discard(self, card: "Card"):
        if card.color != self.color:
            raise Exception("Card discarded to wrong pile")
        self.discard_pile.append(card)

    def draw_top(self):
        return self.discard_pile.pop()
    
    def length(self):
        return len(self.discard_pile)
    
    @property
    def is_empty(self):
        return self.length() == 0
    
    def open_state(self):
        if self.is_empty:
            return f'{self.color}: Empty'
        else:
            top_card_value = self.discard_pile[-1].value
            return f'{self.color}: Top card is {top_card_value}'
        
