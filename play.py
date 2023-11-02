from colors import Color


class Play:
    pass


class PlayToPile(Play):
    def __init__(self, color: Color):
        self.color = color


class DiscardToPile(Play):
    def __init__(self, color: Color):
        self.color = color


class DrawFromPile(Play):
    def __init__(self, color: Color):
        self.color = color


class DrawFromDeck(Play):
    def __init__(self):
        pass
