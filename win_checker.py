ALL_POSSIBLE_WINS = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7']]


class Winchecker():
    def __init__(self, taken_squares: list):

        for possible_win in ALL_POSSIBLE_WINS:
            win = False
            for place in possible_win:
                if place not in taken_squares:
                    win = False
                    break
                else:
                    win = True
            if win == True:
                break

        self.result = win
