class Labirint(object):

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
        if(size < 10):
            size = 10
        self.size = size
    
    def __generate_matrix(self):
        size = self.size
        matrix = [[" " for x in range(size)] for y in range(size)]
        return matrix
