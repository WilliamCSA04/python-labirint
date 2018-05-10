import random
from helper import *
class Labirint:

    __MIN_SIZE = 11

    def __init__(self, size):
        self.size = self.__validate_size(size)
        self.matrix = self.__generate_matrix()

    def print_labirint(self):
        for x in self.matrix:
            row = ""
            for y in x:
                row += y + " "
            print(row)

    def __validate_size(self, size):
        is_lower_than_min_size = size < self.__MIN_SIZE
        if(is_lower_than_min_size): 
            size = self.__MIN_SIZE
        elif is_even(size):  
            size += 1
        return size
    
    def __generate_matrix(self):
        matrix = self.__generate_matrix_with_external_walls()
        matrix = self.__generate_beginning_ending_positions_of_labirint(matrix)
        matrix = self.__generate_paths(matrix)
        matrix = self.__generate_internal_walls(matrix)
        return matrix

    def __generate_matrix_with_external_walls(self):
        size = self.size
        border = size - 1
        matrix = [["%" if x is 0 or y is 0 or x is border or y is border else " " for x in range(size)] for y in range(size)]
        return matrix

    def __generate_beginning_ending_positions_of_labirint(self, matrix):
        border = self.size - 1
        beginning_done = False
        for index_row, x in enumerate(matrix):
            for index_column, y in enumerate(x):
                should_generate = random.random() > 0.9
                not_a_corner = (index_row != 0 or index_column != 0) and (index_row != 0 or index_column != border) and (index_row != border or index_column != 0) and (index_row != border or index_column != border) 
                is_a_valid_position = (index_row is 0 or index_column is 0 or index_row is border or index_column is border) and not_a_corner and (is_odd(index_row) or is_odd(index_column))               
                can_generate_a_initial_ending_position = is_a_valid_position and should_generate
                if can_generate_a_initial_ending_position:
                    if beginning_done:
                        matrix[index_column][index_row] = "E"
                        return matrix
                    else:
                        matrix[index_row][index_column] = "B"
                        beginning_done = True
        has_to_create_beginning = not beginning_done
        matrix = self.__generate_default_beginning_ending_positions(matrix, has_to_create_beginning)
        return matrix

    def __generate_default_beginning_ending_positions(self, matrix, has_to_create_beginning):
        border = self.size - 1
        if has_to_create_beginning:           
            matrix[0][1] = "B"
            matrix[border-1][border] = "E"
        else:
            value = matrix[border-1][border]
            is_beginning = value == "B"
            if is_beginning:
                matrix[border][border-1] = "E"
            else:
                matrix[border-1][border] = "E"
        return matrix

    # TODO: Update this method to always generate a valid B to E path
    def __generate_paths(self, matrix):
        initial = 1
        final = self.size - 1
        increment_by = 2
        for i in range(initial, final, increment_by):
            beginning_column = i
            beginning_row = 1
            coordinate = [beginning_row, beginning_column]
            cell_value = matrix[coordinate[0]][coordinate[1]]
            should_interate = cell_value == " "
            while(should_interate):
                matrix[coordinate[0]][coordinate[1]] = "@"
                new_coordinate = next_step_randomly_without_diagonals(coordinate)
                coordinate = [new_coordinate[0] + coordinate[0], new_coordinate[1] + coordinate[1]]                    
                cell_value = matrix[coordinate[0]][coordinate[1]]
                should_interate = cell_value is " " or cell_value is "@"
        return matrix

    def __generate_internal_walls(self, matrix):
        for index_row, row in enumerate(matrix):
            for index_column, cell in enumerate(row):
                if cell == " ":
                    matrix[index_row][index_column] = "%"
                elif cell == "@":
                    matrix[index_row][index_column] = " "
        return matrix