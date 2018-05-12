class LabirintService:

    def __init__(self, matrix):
        self.matrix = matrix

    def north(self, coordinate):
        if coordinate[0] is 0:
            return None
        return self.cell_value(coordinate[0]-1, coordinate[1])

    def south(self, coordinate):
        if coordinate[0] is len(self.matrix)-1:
            return None
        return self.cell_value(coordinate[0]+1, coordinate[1])

    def east(self, coordinate):
        if coordinate[1] is len(self.matrix)-1:
            return None
        return self.cell_value(coordinate[0], coordinate[1]+1)

    
    def west(self, coordinate):
        if coordinate[1] is 0:
            return None
        return self.cell_value(coordinate[0], coordinate[1]-1)

    def cell_value(self, row, column):
        return self.matrix[row][column]
    
    def new_valid_coordinates(self, actual_coordinate):
        validator_character = "@"
        cell_north = self.north(actual_coordinate)
        cell_south = self.south(actual_coordinate)
        cell_east = self.east(actual_coordinate)
        cell_west = self.west(actual_coordinate)
        is_a_vertical_path = validator_character == cell_north == cell_south
        is_a_horizontal_path = validator_character == cell_west == cell_east
        is_a_path =  is_a_vertical_path or is_a_horizontal_path
        if is_a_path:
            return None
        possibilities = []
        empty_cell = " "
        if(cell_north == empty_cell):
            is_valid = self.__validate_possible_new_coordinate(actual_coordinate, 0, -2)
            if(is_valid):
                north = [-1, 0]
                possibilities.append(north)
        if(cell_west == empty_cell):
            is_valid = self.__validate_possible_new_coordinate(actual_coordinate, 1, -2)
            if(is_valid):
                west = [0, -1]
                possibilities.append(west)
        if(cell_east == empty_cell):
            is_valid = self.__validate_possible_new_coordinate(actual_coordinate, 1, 2)
            if(is_valid):
                east = [0, 1]
                possibilities.append(east)
        if(cell_south == empty_cell):
            is_valid = self.__validate_possible_new_coordinate(actual_coordinate, 1, 2)
            if(is_valid):
                south = [1, 0]
                possibilities.append(south)
        return possibilities

    def __validate_possible_new_coordinate(self, actual_coordinate, coordinate_index, number_of_position):
        empty_cell = " "
        next_neighbor_index = actual_coordinate[coordinate_index] + number_of_position
        is_a_matrix_index = next_neighbor_index >= 0 and next_neighbor_index < len(self.matrix)
        if(is_a_matrix_index):
            return empty_cell == self.cell_value(actual_coordinate[0], next_neighbor_index)
        return False