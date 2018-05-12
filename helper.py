import random

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 == 1

def invert_zero_one(number):
    return int(not bool(number))