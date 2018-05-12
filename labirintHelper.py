import random

def next_step_randomly_without_diagonals(coordinates):
    if coordinates is None:
        next_column = random.randint(-1, 1)
        next_row = random.randint(0, 1)
        if next_column is 1 or next_column is -1:
            next_row = 0
        return [next_row, next_column]
    return random.choice(coordinates)

def new_valid_coordinates(cell_north, cell_south, cell_east, cell_west):
    validator_character = "@"
    is_a_vertical_path = validator_character == cell_north == cell_south
    is_a_horizontal_path = validator_character == cell_west == cell_east
    is_a_path =  is_a_vertical_path or is_a_horizontal_path
    if is_a_path:
        return None
    possibilities = []
    empty_cell = " "
    if(cell_north == empty_cell):
        north = [-1, -1]
        possibilities.append(north)
    if(cell_west == empty_cell):
        west = [0, -1]
        possibilities.append(west)
    if(cell_west == empty_cell):
        east = [0, 1]
        possibilities.append(east)
    if(cell_south == cell_east):
        south = [1, 1]
        possibilities.append(south)
    return possibilities