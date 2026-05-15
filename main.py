import random
import time

from grid import TicTacToeGrid, board
from player import Player
from win_checker import Winchecker
multiplayer = False
PLAYER_1 = Player('X')
PLAYER_2 = Player('O')

tic_tac_toe_grid = TicTacToeGrid()


print('Welcome to Tic Tac Toe')
print(board)


def turn(player: Player, choice):
    global board
    valid_choice = False
    while not valid_choice:
        if choice in tic_tac_toe_grid.available_choices:
            board = board.replace(choice, player.symbol)
            temp_board = board
            for character in tic_tac_toe_grid.available_choices:
                temp_board = temp_board.replace(character, ' ')
            tic_tac_toe_grid.available_choices.remove(choice)

            player.squares_taken.append(choice)
            game_over = Winchecker(player.squares_taken).result

            print(temp_board)
            if game_over:
                print(f'{player.symbol} has won!!!')
                quit()
            return
        else:
            print('That\'s not a valid option!!!!')
            choice = input(
                'Please select where to put your dingetje (1 - 9)')


game_over = False
while not game_over:
    # player 1
    if not tic_tac_toe_grid.available_choices:
        print('draw!')
        game_over = True
        quit()
    choice = input(
        'PLAYER 1: Please select where to mark your symbol (1 - 9): ')
    turn(player=PLAYER_1, choice=choice)
    time.sleep(1)

    if not tic_tac_toe_grid.available_choices:
        print('draw!')
        game_over = True
        quit()
    if multiplayer:
        choice = input(
            'PLAYER 2: Please select where to mark your symbol (1 - 9): ')
        turn(player=PLAYER_2, choice=choice)
        time.sleep(1)
    else:
        print('computer is choosing....')
        choice = PLAYER_2.ai_choose(
            available_choices=tic_tac_toe_grid.available_choices, squares_taken_opponent=PLAYER_1.squares_taken)
        turn(player=PLAYER_2, choice=choice)
        time.sleep(1)

#  save
