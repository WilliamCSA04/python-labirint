import random

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 == 1

def next_step_randomly(coordinates):
     next_column = random.randint(-1, 1)
     next_row = random.randint(0, 1)
     return [next_row, next_column]
