class LabirintService:

    def __init__(self, matrix):
        self.matrix = matrix

    def north(self, coordinate):
        if coordinate[0] is 0:
            return None
        return self.matrix[coordinate[0]-1, self.matrix[1]]

    def south(self, coordinate):
        if coordinate[0] is len(self.matrix)-1:
            return None
        return self.matrix[coordinate[0]+1, self.matrix[1]]

    def east(self, coordinate):
        if coordinate[1] is len(self.matrix)-1:
            return None
        return self.matrix[coordinate[0], self.matrix[1]+1]

    
    def west(self, coordinate):
        if coordinate[1] is 0:
            return None
        return self.matrix[coordinate[0], self.matrix[1]-1]

    
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