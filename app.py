import streamlit as st
import numpy as np


if 'board' not in st.session_state:
    st.session_state['board'] = np.full((3, 3), '', dtype=str)
    st.session_state['current_player'] = 'X'
    st.session_state['game_over'] = False
    st.session_state['message'] = "Player X's turn"


def reset_game():
    st.session_state['board'] = np.full((3, 3), '', dtype=str)
    st.session_state['current_player'] = 'X'
    st.session_state['game_over'] = False
    st.session_state['message'] = "Player X's turn"


def check_winner():
    board = st.session_state['board']
    for player in ['X', 'O']:
        
        if any(all(board[i, :] == player) for i in range(3)) or \
           any(all(board[:, j] == player) for j in range(3)) or \
           all(board[i, i] == player for i in range(3)) or \
           all(board[i, 2 - i] == player for i in range(3)):
            st.session_state['message'] = f"Player {player} wins!"
            st.session_state['game_over'] = True
            return True
    if '' not in board:
        st.session_state['message'] = "It's a draw!"
        st.session_state['game_over'] = True
        return True
    return False


def make_move(i, j):
    if st.session_state['board'][i, j] == '' and not st.session_state['game_over']:
        st.session_state['board'][i, j] = st.session_state['current_player']
        if check_winner():
            return
        
        st.session_state['current_player'] = 'O' if st.session_state['current_player'] == 'X' else 'X'
        st.session_state['message'] = f"Player {st.session_state['current_player']}'s turn"

st.title("Tic Tac Toe")
st.write(st.session_state['message'])


for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            if st.button(st.session_state['board'][i, j] or " ", key=f"{i}-{j}"):
                make_move(i, j)


if st.button("Reset Game"):
    reset_game()
