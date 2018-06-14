from helper import invert_zero_one
import copy

class LabirintService:

    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

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

    def southwest(self, coordinate):
        if coordinate[0] is len(self.matrix)-1 or coordinate[1] is 0:
            return None
        return self.cell_value(coordinate[0]+1, coordinate[1]-1)

    def southeast(self, coordinate):
        if coordinate[0] is len(self.matrix)-1 or coordinate[1] is len(self.matrix)-1:
            return None
        return self.cell_value(coordinate[0]+1, coordinate[1]+1)

    def northwest(self, coordinate):
        if coordinate[0] is 0 or coordinate[1] is 0:
            return None
        return self.cell_value(coordinate[0]-1, coordinate[1]-1) 

    def northeast(self, coordinate):
        if coordinate[0] is 0 or coordinate[1] is len(self.matrix)-1:
            return None
        return self.cell_value(coordinate[0]-1, coordinate[1]+1)

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
            is_valid = self.__validate_possible_new_coordinate(actual_coordinate, 1, -1)
            if(is_valid):
                north = [-1, 0]
                possibilities.append(north)
        if(cell_west == empty_cell):
            is_valid = self.__validate_possible_new_coordinate(actual_coordinate, 0, -1)
            if(is_valid):
                west = [0, -1]
                possibilities.append(west)
        if(cell_east == empty_cell):
            is_valid = self.__validate_possible_new_coordinate(actual_coordinate, 0, 1)
            if(is_valid):
                east = [0, 1]
                possibilities.append(east)
        if(cell_south == empty_cell):
            is_valid = self.__validate_possible_new_coordinate(actual_coordinate, 1, 1)
            if(is_valid):
                south = [1, 0]
                possibilities.append(south)
        return possibilities

    #TOFIX: Sometimes causes infinity loop
    def __validate_possible_new_coordinate(self, actual_coordinate, coordinate_index, side):
        empty_cell = " "
        wall_cell = "%"
        first_next_neighbor_index = actual_coordinate[coordinate_index] + 1
        second_next_neighbor_index = actual_coordinate[coordinate_index] - 1
        valid_first_neighbor = first_next_neighbor_index >= 0 and first_next_neighbor_index < len(self.matrix)
        valid_second_neighbor = second_next_neighbor_index >= 0 and second_next_neighbor_index < len(self.matrix)
        coordinate = actual_coordinate
        inverted_index = invert_zero_one(coordinate_index)
        if(valid_first_neighbor and valid_second_neighbor):
            coordinate[coordinate_index] = first_next_neighbor_index
            coordinate[inverted_index] += side
            first_neighbor = self.cell_value(coordinate[0], coordinate[1])
            coordinate[coordinate_index] = second_next_neighbor_index
            coordinate[inverted_index] += side         
            second_neighbor = self.cell_value(coordinate[0], coordinate[1])
            first_neighbor_is_valid = first_neighbor == empty_cell or first_neighbor == wall_cell
            second_neighbor_is_valid = second_neighbor == empty_cell or second_neighbor == wall_cell
            is_valid = first_neighbor_is_valid and second_neighbor_is_valid
            return is_valid
        if(valid_first_neighbor):
            coordinate[coordinate_index] = first_next_neighbor_index
            coordinate[inverted_index] += side         
            first_neighbor = self.cell_value(coordinate[0], coordinate[1])
            is_valid = empty_cell == first_neighbor or wall_cell == first_neighbor
            return is_valid
        if(valid_second_neighbor):
            coordinate[coordinate_index] = second_next_neighbor_index
            coordinate[inverted_index] += side         
            second_neighbor = self.cell_value(coordinate[0], coordinate[1])
            is_valid = empty_cell ==  second_neighbor or wall_cell == second_neighbor
            return is_valid
        return False