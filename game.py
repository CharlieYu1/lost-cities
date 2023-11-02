from typing import List, Optional

from gamelogic import GameLogic
from loguru import logger

from colors import Color
from deck import Deck
from discard_pile import DiscardPile
from game_history import GameHistory
from play_details import PlayDetails
from player import Player


class Game:
    def __init__(self):
        self.discard_piles = {color: DiscardPile(color) for color in Color}
        self.deck = Deck()
        self.players: List[Player] = []
        self.current_player_pos: Optional[int] = None
        self.gamelogic = GameLogic(self)
        self.game_ended: bool = False
        self.game_history = GameHistory(self)

    @property
    def current_player(self):
        return self.players[self.current_player_pos]

    def new_player(self, name: str) -> Player:
        if len(self.players) >= 2:
            logger.error("Can't add new player. Too many players.")
            return
        elif len(self.players) == 0:
            new_player = Player(name)
            new_player.connect_to_game(self)
        elif len(self.players) == 1:
            new_player = Player(name)
            new_player.connect_to_game(self)
        self.players.append(new_player)
        return new_player

    def new_game(self) -> None:
        if len(self.players) != 2:
            logger.error("Not enough players to start game")
            return
        self.deck.reset()
        for player in self.players:
            player.hand.reset()
            player.hand.get_new_hand(self.deck.deal_hand())
            for color in Color:
                player.columns[color].reset()
        for color in Color:
            self.discard_piles[color].reset()
        self.game_ended = False
        self.current_player_pos = 0
        
    def discard_state(self) -> str:
        discard_state = f"Discard piles:\n"
        for color in Color:
            discard_state += f"{self.discard_piles[color].open_state()}\n"
        return discard_state
    
    def open_game_state(self) -> str:
        open_game_state = '\n'.join([player.open_player_state() for player in self.players])
        open_game_state += '\n'
        open_game_state += self.discard_state()
        return open_game_state

    def move_to_next_player(self) -> None:
        self.current_player_pos = (self.current_player_pos + 1) % 2

    def receive_player_move(self, player: Player, play_details: PlayDetails):
        self.gamelogic.make_move(player, play_details)
        is_game_ended, message = self.gamelogic.check_end()
        if is_game_ended:
            self.game_ended = True
            for player in self.players:
                player.recieve_success_message(message)
        else:
            self.move_to_next_player()
