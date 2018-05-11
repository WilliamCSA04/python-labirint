import random

def next_step_randomly_without_diagonals(coordinates):
    next_column = random.randint(-1, 1)
    next_row = random.randint(0, 1)
    if next_column is 1 or next_column is -1:
        next_row = 0
    return [next_row, next_column]

def corner_direction(cellNorth, cellSouth, cellEast, cellWest):
    if(cellNorth == cellEast):
        return "NE"
    if(cellNorth == cellWest):
        return "NW"
    if(cellSouth == cellWest):
        return "SW"
    if(cellSouth == cellEast):
        return "SE"
    return None