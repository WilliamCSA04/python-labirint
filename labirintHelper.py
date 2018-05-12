import random

def next_step_randomly_without_diagonals(coordinate = None):
    if coordinate is None:
        next_column = random.randint(-1, 1)
        next_row = random.randint(0, 1)
        if next_column is 1 or next_column is -1:
            next_row = 0
        return [next_row, next_column]
    return random.choice(coordinate)