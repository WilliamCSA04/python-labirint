class Labirint(object):

    def __init__(self, size):
        self.__validate_size(size)
        self.matrix = [["-" if x is 0 or y is 0 or x is self.size-1 or y is self.size-1 else " " for x in range(self.size)] for y in range(self.size)]

    def print_labirint(self):
        for x in self.matrix:
            print(x)

    def __validate_size(self, size):
        if(size < 10):
            size = 10
        print(size)
        self.size = size
