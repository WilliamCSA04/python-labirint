import random
class Labirint:

    __MIN_SIZE = 10

    def __init__(self, size):
        self.__validate_size(size)
        self.matrix = self.__generate_matrix()

    def print_labirint(self):
        for x in self.matrix:
            row = ""
            for y in x:
                row += y + " "
            print(row)

    def __validate_size(self, size):
        if(size < self.__MIN_SIZE):
            size = self.__MIN_SIZE
        self.size = size
    
    def __generate_matrix(self):
        matrix = self.__generate_external_walls()
        matrix = self.__generate_beginning_ending_of_labirint(matrix)
        return matrix

    def __generate_external_walls(self):
        size = self.size
        border = size - 1
        matrix = [["%" if x is 0 or y is 0 or x is border or y is border else " " for x in range(size)] for y in range(size)]
        return matrix

    def __generate_beginning_ending_of_labirint(self, matrix):
        border = self.size - 1
        beginning_done = False
        for index_row, x in enumerate(matrix):
            for index_column, y in enumerate(x):
                should_generate = random.random() > 0.9
                not_a_corner = (index_row != 0 or index_column != 0) and (index_row != 0 or index_column != border) and (index_row != border or index_column != 0) and (index_row != border or index_column != border) 
                is_a_valid_position = (index_row is 0 or index_column is 0 or index_row is border or index_column is border) and not_a_corner                
                can_generate_a_initial_ending_position = is_a_valid_position and should_generate
                if can_generate_a_initial_ending_position:
                    if beginning_done:
                        matrix[index_column][index_row] = "E"
                        return matrix
                    else:
                        matrix[index_row][index_column] = "B"
                        beginning_done = True
        if not beginning_done:           
            matrix[0][1] = "B"
        matrix[border-1][border] = "E"
        return matrix

