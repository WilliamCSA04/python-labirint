class LabirintService:

    def __init__(self, matrix):
        self.matrix = matrix

    def north(self, coordinate):
        if coordinate[0] is 0:
            return None