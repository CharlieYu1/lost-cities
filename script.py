from game import Game
import random
from colors import Color
from play import PlayToPile, DrawFromDeck, DiscardToPile, DrawFromPile
random.seed(0)

g = Game()
a = g.new_player("A")
b = g.new_player("B")
g.new_game()
print(a.hidden_player_state())
print(b.hidden_player_state())
print(g.open_game_state())
print(a.hand.get_card(1))
a.pick_card(2)
a.set_play(DiscardToPile(Color.BLUE))
a.set_play(DrawFromDeck())
a.send_move_to_game()
print(a.hidden_player_state())
print(b.hidden_player_state())
print(g.open_game_state())
b.pick_card(1)
b.set_play(DiscardToPile(Color.YELLOW))
b.set_play(DrawFromPile(Color.BLUE))
print(a.hidden_player_state())
b.send_move_to_game()
print(b.hidden_player_state())
print(g.open_game_state())