import time
import game

class GameStat:
    def __init__(self, game_level):
        self.game_id = 0
        self.start = time.time()
        self.game_time = 0
        self.round = 0
        self.is_draw = False
        self.game_level = game_level
        self.is_computer_winner = False
        self.is_player_one_winner = False
        # work on user location using IP

    def db_find(self):
        pass # get game_id

    def end_game(self):
        self.game_time = time.time() - self.start
        del self.start

    def declare_winner(self, winner, winner_type):
        if winner == game.Players.one:
            self.is_player_one_winner = True
        if winner_type in game.PlayerOptions._value2member_map_:
            self.is_computer_winner = True

    def declare_draw(self):
        self.is_draw = True

    def update_round(self):
        self.round += 1