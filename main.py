import random
import time


multiplayer = False
PLAYER_1 = 'X'
PLAYER_2 = 'O'

available_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
marked_x = []
marked_o = []

board = '''
1|2|3
-----
4|5|6
-----
7|8|9
'''


print('Welcome to Tic Tac Toe')
print(board)


def turn(player, choice):
    global board
    valid_choice = False
    while not valid_choice:
        if choice in available_choices:
            board = board.replace(choice, player)
            available_choices.remove(choice)
            if player == 'X':
                marked_x.append(choice)
                game_over = check_for_win(marked_x)
            else:
                marked_o.append(choice)
                game_over = check_for_win(marked_o)
            print(board)
            if game_over:
                print(f'{player} has won!!!')
                quit()
            return
        else:
            print('That\'s not a valid option!!!!')
            choice = input(
                'Please select where to put your dingetje (1 - 9)')


def check_for_win(marked_boxes):
    wins = [['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['1', '4', '7'],
            ['2', '5', '8'],
            ['3', '6', '9'],
            ['1', '5', '9'],
            ['3', '5', '7']]

    for possible_win in wins:
        win = False
        for place in possible_win:
            if place not in marked_boxes:
                win = False
                break
            else:
                win = True
        if win == True:
            break

    return win


game_over = False
while not game_over:
    # player 1
    choice = input(
        'PLAYER 1: Please select where to put your dingetje (1 - 9)')
    turn(player=PLAYER_1, choice=choice)

    if multiplayer:
        choice = input(
            'PLAYER 2: Please select where to put your dingetje (1 - 9)')
        turn(player=PLAYER_2, choice=choice)
        time.sleep(1)
    else:
        print('computer is choosing....')
        choice = random.choice(available_choices)
        turn(player=PLAYER_2, choice=choice)
        time.sleep(1)
