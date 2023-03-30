# connect 4 inthe terminal via python 
# starts around the 1 hour 35 min mark
# # https://www.youtube.com/watch?v=XGf2GcyHPhc
# left off at 1hr 46 min

import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece():
    pass

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row():
    pass


board = create_board()
game_over = False
turn = 0

# run as long as game over is false
while not game_over: 
    # Ask for player 1 input
    if turn == 0:
        selection = int(input("Player 1 make your selection (0-6): "))

        print(selection)
        print(type(selection))


    # ask for player 2 input
    else:
        selection = int(input("Player 2 make your selection (0-6): "))

# swapping between player 1 and 2
turn += 1
turn = turn % 2



