from win_checker import ALL_POSSIBLE_WINS
import random


class Player():
    def __init__(self, symbol):
        self.symbol = symbol
        self.squares_taken = []

    def ai_choose(self, available_choices, squares_taken_opponent):
        # check available choices
        # check if opponent is about to win
        for possible_win in ALL_POSSIBLE_WINS:
            check_for_win = 0
            free_squares = []
            for place in possible_win:
                if place in squares_taken_opponent:
                    check_for_win += 1
                else:
                    free_squares.append(place)

            if check_for_win > 1:
                choice = free_squares[0]
                if choice in available_choices:
                    return choice

        # check if self is about to win
        for possible_win in ALL_POSSIBLE_WINS:
            check_for_win = 0
            free_squares = []
            for place in possible_win:
                if place in self.squares_taken:
                    check_for_win += 1
                else:
                    free_squares.append(place)

            if check_for_win > 1:
                choice = free_squares[0]
                if choice in available_choices:
                    return choice

        choice = random.choice(available_choices)
        return choice
