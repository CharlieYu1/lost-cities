from play import DiscardToPile, DrawFromDeck, DrawFromPile, Play, PlayToPile
from colors import Color
from loguru import logger
from typing import Tuple


class GameLogic:
    def __init__(self, game: "Game"):
        self._game = game

    def check_move_is_valid(self, player: "Player", play_details: "PlayDetails"):
        current_player = self._game.current_player
        if self._game.game_ended:
            raise Exception("Game already ended")
        if player != current_player:
            raise Exception("Not current player")
        card_pos = play_details.chosen_card_pos
        card = player.hand.get_card(card_pos)
        first_play, second_play = play_details.plays
        if not isinstance(first_play, (PlayToPile, DiscardToPile)):
            raise Exception("The first play has to be played or discarded to a pile")
        if card.color != first_play.color:
            raise Exception("Card played or discarded to wrong pile")
        if isinstance(first_play, PlayToPile):
            pile_top_card_value = player.columns[card.color].top_card_value
            if card.value < pile_top_card_value:
                raise Exception("Can't play a card with value lower than top card")
        if not isinstance(second_play, (DrawFromPile, DrawFromDeck)):
            raise Exception("The second play has to be draw a card")
        if isinstance(first_play, DiscardToPile) and isinstance(second_play, DrawFromPile):
            if first_play.color == second_play.color:
                raise Exception("Can't discard and draw from the same pile")
        if isinstance(second_play, DrawFromPile):
            if self._game.discard_piles[second_play.color].is_empty:
                raise Exception("Can't draw from empty pile")
            
    def make_move(self, player: "Player", play_details: "PlayDetails"):
        chosen_card_pos = play_details.chosen_card_pos
        card = player.hand.pop_card(chosen_card_pos)
        first_play, second_play = play_details.plays
        if isinstance(first_play, PlayToPile):
            player.columns[card.color].play(card)
        elif isinstance(first_play, DiscardToPile):
            self._game.discard_piles[card.color].discard(card)
        if isinstance(second_play, DrawFromPile):
            card = self._game.discard_piles[second_play.color].draw_top()
            player.hand.add_card(card)
        elif isinstance(second_play, DrawFromDeck):
            card = self._game.deck.draw()
            player.hand.add_card(card)
            
    def player_score(self, player: "Player") -> int:
        return sum(player.columns[color].score for color in Color)
    
    def check_end(self) -> Tuple[bool, str]:
        if not self._game.deck.is_empty():
            return [False, '']
        else:
            player_scores = [self.player_score(player) for player in self._game.players]
            if player_scores[0] > player_scores[1]:
                return [True, f'{self._game.players[0]} win!']
            elif player_scores[0] < player_scores[1]:
                return [True, f'{self._game.players[1]} win!']
            else:
                return [True, 'Game ends in a draw']
        
        
