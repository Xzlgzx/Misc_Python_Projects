# import gamestat
import streamlit as st
import numpy as np
import game


def change_player():
    if st.session_state.cur_player == game.Players.one.value:
        st.session_state.cur_player = game.Players.two.value
    else:
        st.session_state.cur_player = game.Players.one.value


def process_game(column, row, clicked=False):
    if clicked:
        st.session_state.is_user = True
    if st.session_state.board[column, row] != game.BLANK:
        st.warning("You have already selected this box.")
    elif st.session_state.end_of_game:
        st.warning("Game is already over.")
    else:
        st.session_state.board[column, row] = st.session_state.cur_player
        check = game.check_game_state(list(st.session_state.board.flatten()))
        if check == game.GameStatus.none.value:
            change_player()
        else:
            st.session_state.end_of_game = True
            if check == game.GameStatus.draw.value:
                st.warning("Tie game!")
            else:
                st.warning("There is a winner!")
            # game_stat.end_game()


def button(refresh_button=False):
    for col in range(3):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button(
                      label=st.session_state.board[col, 0],
                      key=f"{col}, {0}",
                      on_click=process_game,
                      args=(col, 0, True)
                     )
        with col2:
            st.button(
                      label=st.session_state.board[col, 1],
                      key=f"{col}, {1}",
                      on_click=process_game,
                      args=(col, 1, True)
                     )
            if refresh_button and col == 2:
                st.button(label="Click me to update.")
        with col3:
            st.button(
                      label=st.session_state.board[col, 2],
                      key=f"{col}, {2}",
                      on_click=process_game,
                      args=(col, 2, True)
                     )


st.write("[Source code for the game](https://github.com/Xzlgzx/Py_Projects/blob"
         "/master/tic_tac_toe_ai/game.py)")
st.write("[Source code for the frontend](https://github.com/Xzlgzx/Py_Projects/"
         "blob/master/tic_tac_toe_ai/stgame.py)")

if "initialize" not in st.session_state:
    st.title("Tic-Tac-Toe.")
    st.text("1. Select 'User' if you would like to play the game.")
    st.text("2. Select 'Random' if you like randomness.")
    st.text("3. Select 'Dummy' if you like playing against a 'dumb' computer.")
    st.text("4. Select 'AI' if you think you want a serious challenge.")
    first_selection = st.selectbox(
        'User 1:', ('User', 'Random', 'Dummy', 'AI'))
    second_selection = st.selectbox(
        'User 2:', ('User', 'Random', 'Dummy', 'AI'))
    st.session_state.player1 = first_selection
    st.session_state.player2 = second_selection
    st.write("You selected: ", first_selection, second_selection)
    confirmation = st.button("confirm")
    # game_stat = gamestat.GameStat()

if "board" not in st.session_state:
    board = np.empty((game.BOARD_WIDTH, game.BOARD_WIDTH), dtype=str)
    board.fill(game.BLANK)
    st.session_state.board = board
    st.session_state.end_of_game = False
    st.session_state.cur_player = game.Players.one.value
    st.session_state.counter = 1
    st.session_state.is_user = False

if "initialize" in st.session_state or confirmation:
    st.session_state.initialize = True
    if st.session_state.player1 in game.PlayerOptions._value2member_map_ and \
            st.session_state.player2 in game.PlayerOptions._value2member_map_:
        button(refresh_button=True)
        if not st.session_state.end_of_game:
            user1_move = game.initialize(st.session_state.player1,
                                         st.session_state.cur_player,
                                         list(st.session_state.board.flatten()))
            process_game(*user1_move)
        if not st.session_state.end_of_game:
            user2_move = game.initialize(st.session_state.player2,
                                         st.session_state.cur_player,
                                         list(st.session_state.board.flatten()))
            process_game(*user2_move)
    elif st.session_state.player1 == st.session_state.player2 == "User":
        button()
    elif st.session_state.player1 == "User":
        button(refresh_button=True)
        if not st.session_state.end_of_game and st.session_state.is_user:
            user2_move = game.initialize(st.session_state.player2,
                                         st.session_state.cur_player,
                                         list(st.session_state.board.flatten()))
            process_game(*user2_move)
            st.session_state.is_user = False
    else:
        if not st.session_state.end_of_game:
            user1_move = game.initialize(st.session_state.player1,
                                         st.session_state.cur_player,
                                         list(st.session_state.board.flatten()))
            process_game(*user1_move)
        button()
