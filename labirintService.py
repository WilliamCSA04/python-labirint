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