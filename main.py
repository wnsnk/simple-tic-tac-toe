import time

from modules.grid import TicTacToeGrid, board
from modules.player import Player
from modules.win_checker import Winchecker
multiplayer = False
PLAYER_1 = Player('X')
PLAYER_2 = Player('O')

tic_tac_toe_grid = TicTacToeGrid()
fresh_board = board


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
                ask_for_new_round()

            return
        else:
            print('That\'s not a valid option!!!!')
            choice = input(
                'Please select where to put your dingetje (1 - 9)')


def check_for_draw():
    if not tic_tac_toe_grid.available_choices:
        print('draw!')
        ask_for_new_round()


def ask_for_new_round():
    valid_option = False
    while not valid_option:
        try_again = input(
            'Would you like to play another game? (Y/N) \n').lower()
        if try_again != 'y' and try_again != 'n':
            print('Not a valid character. Try again.')
        else:
            if try_again == 'y':
                game()
            else:
                quit()


def reset():
    clear_screen()
    global board
    global PLAYER_1, PLAYER_2
    tic_tac_toe_grid.available_choices = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('Welcome to Tic Tac Toe')
    print(fresh_board)
    board = fresh_board
    PLAYER_1.squares_taken = []
    PLAYER_2.squares_taken = []


def clear_screen():
    print('\n' * 50)


def game():
    reset()
    game_over = False
    while not game_over:
        # player 1
        check_for_draw()
        choice = input(
            'PLAYER 1: Please select where to mark your symbol (1 - 9): ')
        turn(player=PLAYER_1, choice=choice)
        time.sleep(1)

        check_for_draw()
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


game()
