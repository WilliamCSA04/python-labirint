class Labirint:

    def __init__(self, size):
        self.size = size
        self.matrix = [["-" if x is 0 or y is 0 or x is size or y is size else "*" for x in range(size)] for y in range(size)]