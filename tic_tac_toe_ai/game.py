import copy
import random
from enum import Enum

# Constants
COOR = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
BLANK = '_'
BOARD_WIDTH = 3


class PlayerOptions(Enum):
    Random = 'Random'
    Dummy = 'Dummy'
    AI = 'AI'


class GameStatus(Enum):
    lose = "lose"
    draw = "draw"
    win = "win"
    none = "none"


class Players(Enum):
    one = "X"
    two = "O"


def check_game_state(game):
    if game[0] == game[1] == game[2] != BLANK or game[0] == game[3] == game[6] \
            != BLANK or game[0] == game[4] == game[8] != BLANK:
        if game[0] == Players.one.value:
            return GameStatus.win.value
        else:
            return GameStatus.lose.value
    if game[3] == game[4] == game[5] != BLANK or game[1] == game[4] == game[7] \
            != BLANK or game[2] == game[4] == game[6] != BLANK:
        if game[4] == Players.one.value:
            return GameStatus.win.value
        else:
            return GameStatus.lose.value
    if game[6] == game[7] == game[8] != BLANK or game[2] == game[5] == game[8] \
            != BLANK:
        if game[8] == Players.one.value:
            return GameStatus.win.value
        else:
            return GameStatus.lose.value
    if game.count(Players.two.value) + game.count(Players.one.value) == 9:
        return GameStatus.draw.value
    else:
        return GameStatus.none.value


def level_easy(the_game):
    computer_move = random.randint(0, 8)
    while the_game[computer_move] != "_":
        computer_move = random.randint(0, 8)
    return computer_move


def level_medium(the_game):
    while True:
        if the_game[3] == the_game[6] != BLANK or the_game[1] == the_game[2] \
                != BLANK or the_game[4] == the_game[8] != BLANK:
            if the_game[0] == BLANK:
                return 0
        if the_game[1] == the_game[0] != BLANK or the_game[5] == the_game[8] \
                != BLANK or the_game[4] == the_game[6] != BLANK:
            if the_game[2] == BLANK:
                return 2
        if the_game[3] == the_game[4] != BLANK or the_game[2] == the_game[8] \
                != BLANK:
            if the_game[5] == BLANK:
                return 5
        if the_game[4] == the_game[5] != BLANK or the_game[0] == the_game[6] \
                != BLANK:
            if the_game[3] == BLANK:
                return 3
        if the_game[0] == the_game[2] != BLANK or the_game[4] == the_game[7] \
                != BLANK:
            if the_game[1] == BLANK:
                return 1
        if the_game[3] == the_game[5] != BLANK or the_game[1] == the_game[7] \
                != BLANK or the_game[0] == the_game[8] != BLANK or the_game[6] \
                == the_game[2] != BLANK:
            if the_game[4] == BLANK:
                return 4
        if the_game[6] == the_game[8] != BLANK or the_game[1] == the_game[4] \
                != BLANK:
            if the_game[7] == BLANK:
                return 7
        if the_game[6] == the_game[7] != BLANK or the_game[0] == the_game[4] \
                != BLANK or the_game[2] == the_game[5] != BLANK:
            if the_game[8] == BLANK:
                return 8
        if the_game[0] == the_game[3] != BLANK or the_game[7] == the_game[8] \
                != BLANK or the_game[2] == the_game[4] != BLANK:
            if the_game[6] == BLANK:
                return 6
        computer_move = random.randint(0, 8)
        while the_game[computer_move] != "_":
            computer_move = random.randint(0, 8)
        return computer_move


def level_hard(game, move_type, update, min_max):
    if len(all_possible_moves(game)) == 9:
        return {1: random.choice([0, 2, 6, 8])}
    move_dict = {}
    if min_max == "min":
        while len(update) != 0:
            temp_game = copy.deepcopy(game)
            move_dict.update(minimum(temp_game, move_type, update[0]))
            update.pop(0)
    else:
        while len(update) != 0:
            temp_game = copy.deepcopy(game)
            move_dict.update(maximum(temp_game, move_type, update[0]))
            update.pop(0)
    return move_dict


def all_possible_moves(game):
    return [counter for counter in range(len(game)) if game[counter] == "_"]


def minimum(game, move_type, move):
    game[move] = move_type
    if check_game_state(game) == GameStatus.win.value and move_type == Players.one.value:
        return {-1: move}
    elif check_game_state(game) == GameStatus.win.value and move_type == Players.two.value:
        return {1: move}
    elif check_game_state(game) == GameStatus.lose.value and move_type == Players.one.value:
        return {1: move}
    elif check_game_state(game) == GameStatus.lose.value and move_type == Players.two.value:
        return {-1: move}
    elif check_game_state(game) == GameStatus.draw.value:
        return {0: move}
    else:
        max_dict = level_hard(game, Players.one.value if move_type == Players.two.value else
                              Players.two.value, all_possible_moves(game), "max")
        return {max(max_dict): move}


def maximum(game, move_type, move):
    game[move] = move_type
    if check_game_state(game) == GameStatus.win.value and move_type == Players.one.value:
        return {1: move}
    elif check_game_state(game) == GameStatus.win.value and move_type == Players.two.value:
        return {-1: move}
    elif check_game_state(game) == GameStatus.lose.value and move_type == Players.one.value:
        return {-1: move}
    elif check_game_state(game) == GameStatus.lose.value and move_type == Players.two.value:
        return {1: move}
    elif check_game_state(game) == GameStatus.draw.value:
        return {0: move}
    else:
        min_dict = level_hard(game, Players.one.value if move_type == Players.two.value else
                              Players.two.value, all_possible_moves(game), "min")
        return {min(min_dict): move}


def start_game(user: str, player: str, game):
    if user == PlayerOptions.Random.value:
        move = level_easy(game)
    elif user == PlayerOptions.Dummy.value:
        move = level_medium(game)
    else:
        level_hard_result = level_hard(game, player, all_possible_moves(game),
                                       "max")
        move = level_hard_result.get(max(level_hard_result.keys()))
    return COOR[move]


def initialize(user: str, player: str, game_grid: list):
    if user in PlayerOptions._value2member_map_:
        return start_game(user, player, game_grid)
    else:
        raise Exception("invalid parameters")
