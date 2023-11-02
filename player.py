from loguru import logger

from colors import Color
from columns import Column
from play_details import PlayDetails
from player_hand import PlayerHand


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = PlayerHand()
        self.columns = dict()
        for color in Color:
            self.columns[color] = Column(color)
        self.play_details = PlayDetails()

    def connect_to_game(self, game: "Game"):
        self.connected_game = game

    def reset_play_details(self):
        self.chosen_card_pos = None
        self.plays = [None, None]

    def pick_card(self, card_pos: int):
        try:
            self.play_details.set_card_pos(card_pos)
        except Exception as e:
            self.display_error_message(e)

    def set_play(self, play: "Play"):
        try:
            self.play_details.set_play(play)
        except Exception as e:
            self.display_error_message(e)

    def send_move_to_game(self):
        # try:
        self.play_details.validate()
        self.connected_game.gamelogic.check_move_is_valid(self, self.play_details)
        # except Exception as e:
        #     self.display_error_message(e)
        #     return
        self.connected_game.receive_player_move(self, self.play_details)
        self.play_details.reset()

    def display_error_message(self, message: str):
        logger.error(f"Player {self.name}: {message}")

    def display_success_message(self, message: str):
        logger.success(f"Player {self.name}: {message}")

    def __repr__(self) -> str:
        return f'Player("{self.name}")'

    def hidden_player_state(self) -> str:
        return f"{self.name}'s hand: {self.hand}"
    
    def open_player_state(self) -> str:
        player_score = self.connected_game.gamelogic.player_score(self)
        open_game_state = f"{self.name}'s board:\n"
        for color in Color:
            open_game_state += f"{color}: {self.columns[color]}\n"
        open_game_state += f"{self.name}'s score: {player_score}"
        return open_game_state