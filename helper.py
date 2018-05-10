import random

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 == 1

def next_step_randomly_without_diagonals(coordinates):
    next_column = random.randint(-1, 1)
    next_row = random.randint(0, 1)
    if next_column is 1 or next_column is -1:
        next_row = 0
    return [next_row, next_column]
