class Labirint:

    def __init__(self, size):
        self.__validate_size(size)
        last_position = size-1
        self.matrix = [["-" if x is 0 or y is 0 or x is last_position or y is last_position else " " for x in range(size)] for y in range(size)]


    def print_labirint(self):
        for x in self.matrix:
            print(x)

    def __validate_size(self, size):
        if(size < 10):
            size = 10
        self.size = size
