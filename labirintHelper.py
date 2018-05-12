import random

# - Define next_step_randomly_without_diagonals: Randomly choose one of arrays inside of 
# coordinate parameter. If None or a empty array is pass as paramenter, it will randomly
# generate a coordenade of any combination other than [-1, 1] or [1, -1]
# - Parameter => Coordinate(optional): An array of multiple coordinates. Example: [[1, 0],[-1, 0]]
# - Return: A coordenate as an array of integer of two positions where the first element is the
# and the second is the column
def next_step_randomly_without_diagonals(coordinate = None):
    if coordinate is None or len(coordinate) is 0:
        next_column = random.randint(-1, 1)
        next_row = random.randint(0, 1)
        if next_column is 1 or next_column is -1:
            next_row = 0
        return [next_row, next_column]
    return random.choice(coordinate)