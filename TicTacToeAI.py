import copy
import random


def print_game(game):
    counter = 0
    current_line = ""
    print("---------")

    for coordinate in game:
        if counter % 3 == 0 and counter != 0:
            print("|" + current_line + " |")
            current_line = " " + (" " if coordinate == "_" else coordinate)
            counter = 0
        else:
            current_line = current_line + " " + (" " if coordinate == "_" else coordinate)
        counter += 1
    print("|" + current_line + " |")
    print("---------")


def get_full_game(game):
    return [coordinate for coordinate in game]


def move_index(move):
    if move[0] == '1' and move[1] == '1':
        return 6
    if move[0] == '1' and move[1] == '2':
        return 3
    if move[0] == '1' and move[1] == '3':
        return 0
    if move[0] == '2' and move[1] == '1':
        return 7
    if move[0] == '2' and move[1] == '2':
        return 4
    if move[0] == '2' and move[1] == '3':
        return 1
    if move[0] == '3' and move[1] == '1':
        return 8
    if move[0] == '3' and move[1] == '2':
        return 5
    if move[0] == '3' and move[1] == '3':
        return 2


def check_game_state(game, level=None):
    if game[0] == game[1] == game[2] != "_" or game[0] == game[3] == game[6] != "_" \
            or game[0] == game[4] == game[8] != "_":

        if game[0] == "X":
            if level is None:
                print("X wins")
            return "win"
        else:
            if level is None:
                print("O wins")
            return "lose"
    if game[3] == game[4] == game[5] != "_" or game[1] == game[4] == game[7] != "_" \
            or game[2] == game[4] == game[6] != "_":
        if game[4] == "X":
            if level is None:
                print("X wins")
            return "win"
        else:
            if level is None:
                print("O wins")
            return "lose"
    if game[6] == game[7] == game[8] != "_" or game[2] == game[5] == game[8] != "_":
        if game[8] == "X":
            if level is None:
                print("X wins")
            return "win"
        else:
            if level is None:
                print("O wins")
            return "lose"
    if game.count("O") + game.count("X") == 9:
        if level is None:
            print("Draw")
        return "draw"
    else:
        return "none"


def level_easy(the_game):
    print('Making move level "easy"')
    computer_move = random.randint(0, 8)
    while the_game[computer_move] != "_":
        computer_move = random.randint(0, 8)
    return computer_move


def level_medium(the_game):
    print('Making move level "medium"')
    while True:
        if the_game[3] == the_game[6] != '_' or the_game[1] == the_game[2] != '_' or the_game[4] == the_game[8] != '_':
            if the_game[0] == '_':
                return 0
        if the_game[1] == the_game[0] != '_' or the_game[5] == the_game[8] != '_' or the_game[4] == the_game[6] != '_':
            if the_game[2] == '_':
                return 2
        if the_game[3] == the_game[4] != '_' or the_game[2] == the_game[8] != '_':
            if the_game[5] == '_':
                return 5
        if the_game[4] == the_game[5] != '_' or the_game[0] == the_game[6] != '_':
            if the_game[3] == '_':
                return 3
        if the_game[0] == the_game[2] != '_' or the_game[4] == the_game[7] != '_':
            if the_game[1] == '_':
                return 1
        if the_game[3] == the_game[5] != '_' or the_game[1] == the_game[7] != '_' \
                or the_game[0] == the_game[8] != '_' or the_game[6] == the_game[2] != '_':
            if the_game[4] == '_':
                return 4
        if the_game[6] == the_game[8] != '_' or the_game[1] == the_game[4] != '_':
            if the_game[7] == '_':
                return 7
        if the_game[6] == the_game[7] != '_' or the_game[0] == the_game[4] != '_' or the_game[2] == the_game[5] != '_':
            if the_game[8] == '_':
                return 8
        if the_game[0] == the_game[3] != '_' or the_game[7] == the_game[8] != '_' or the_game[2] == the_game[4] != '_':
            if the_game[6] == '_':
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
    if check_game_state(game, "hard") == "win" and move_type == "X":
        return {-1: move}
    elif check_game_state(game, "hard") == "win" and move_type == "O":
        return {1: move}
    elif check_game_state(game, "hard") == "lose" and move_type == "X":
        return {1: move}
    elif check_game_state(game, "hard") == "lose" and move_type == "O":
        return {-1: move}
    elif check_game_state(game, "hard") == "draw":
        return {0: move}
    else:
        max_dict = level_hard(game, "X" if move_type == "O" else "O", all_possible_moves(game), "max")
        return {max(max_dict): move}


def maximum(game, move_type, move):
    game[move] = move_type
    if check_game_state(game, "hard") == "win" and move_type == "X":
        return {1: move}
    elif check_game_state(game, "hard") == "win" and move_type == "O":
        return {-1: move}
    elif check_game_state(game, "hard") == "lose" and move_type == "X":
        return {-1: move}
    elif check_game_state(game, "hard") == "lose" and move_type == "O":
        return {1: move}
    elif check_game_state(game, "hard") == "draw":
        return {0: move}
    else:
        min_dict = level_hard(game, "X" if move_type == "O" else "O", all_possible_moves(game), "min")
        return {min(min_dict): move}


def user_move(check_game):
    while True:
        print("Enter the coordinates: ")
        move = input().split()

        if move[0] in ['1', '2', '3'] and move[1] in ['1', '2', '3']:
            game_index = move_index(move)
            if check_game[game_index] == 'X' or check_game[game_index] == 'O':
                print("This cell is occupied! Choose another one!")
            else:
                if check_game.count('X') <= check_game.count('O'):
                    check_game[game_index] = 'X'
                else:
                    check_game[game_index] = 'O'
                game = ''.join(check_game)
                print_game(game)
                break
        elif move[0] in ['one', 'two', 'three'] or move[1] in ['one', 'two', 'three']:
            print("You should enter numbers!")
        else:
            print("Coordinates should be from 1 to 3!")



def start_game(opponent_1, opponent_2):
    print("Enter cells: ")
    game = "_________"
    print_game(game)
    check_game = get_full_game(game)

    if opponent_1 in ["easy", "medium", "hard"] and opponent_2 in ["easy", "medium", "hard"]:
        while True:
            if check_game_state(check_game) != "none":
                break
            check_game[level_easy(check_game) if opponent_1 == "easy" else (
                level_medium(check_game) if opponent_1 == "medium" else level_hard(check_game, "X",
                                                                                   all_possible_moves(check_game),
                                                                                   "max").get(
                    max(level_hard(check_game, "X", all_possible_moves(check_game), "max").keys())))] = "X"
            game = ''.join(check_game)
            print_game(game)
            if check_game_state(check_game) != "none":
                break
            check_game[level_easy(check_game) if opponent_2 == "easy" else (
                level_medium(check_game) if opponent_2 == "medium" else level_hard(check_game, "O",
                                                                                   all_possible_moves(check_game),
                                                                                   "max").get(
                    max(level_hard(check_game, "O", all_possible_moves(check_game), "max").keys())))] = "O"
            game = ''.join(check_game)
            print_game(game)
    else:
        while True:
            if opponent_1 == "easy" or opponent_1 == "medium" or opponent_1 == "hard":
                if check_game_state(check_game) != "none":
                    break
                check_game[level_easy(check_game) if opponent_1 == "easy" else (
                    level_medium(check_game) if opponent_1 == "medium" else level_hard(check_game, "X",
                                                                                       all_possible_moves(check_game),
                                                                                       "max").get(
                        max(level_hard(check_game, "X", all_possible_moves(check_game), "max").keys())))] = "X"
                game = ''.join(check_game)
                print_game(game)
                if check_game_state(check_game) != "none":
                    break
                user_move(check_game)
            elif opponent_1 == opponent_2:
                if check_game_state(check_game) != "none":
                    break
                user_move(check_game)
                if check_game_state(check_game) != "none":
                    break
                user_move(check_game)
            else:
                if check_game_state(check_game) != "none":
                    break
                user_move(check_game)
                if check_game_state(check_game) != "none":
                    break
                check_game[level_easy(check_game) if opponent_2 == "easy" else (
                    level_medium(check_game) if opponent_2 == "medium" else level_hard(check_game, "O",
                                                                                       all_possible_moves(check_game),
                                                                                       "max").get(
                        max(level_hard(check_game, "O", all_possible_moves(check_game), "max").keys())))] = "O"
                game = ''.join(check_game)
                print_game(game)


def main():
    while True:
        print("Input command:")
        input_command = input().split()
        if input_command[0] == "exit":
            break
        elif len(input_command) < 3 or len(input_command) > 3:
            print("Bad parameters!")
        elif input_command[0] == "start" and input_command[1] in ["easy", "user", "medium", "hard"] \
                and input_command[2] in ["easy", "user", "medium", "hard"]:
            input_command.remove("start")
            start_game(input_command[0], input_command[1])
        else:
            print("Bad parameters!")


if __name__ == "__main__":
    main()
