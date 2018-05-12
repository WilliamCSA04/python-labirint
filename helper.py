import random

# Define is_even: Check if the number is even
# Parameter => number: A integer value
# Return: True if is even, false otherwise
def is_even(number):
    return number % 2 == 0

# Define is_odd: Check if the number is odd.
# Parameter => number: A integer value.
# Return: True if is odd, false otherwise.
def is_odd(number):
    return number % 2 == 1

def invert_zero_one(number):
    return int(not bool(number))