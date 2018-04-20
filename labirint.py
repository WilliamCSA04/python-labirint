class Labirint:

    def __init__(self, size):
        self.size = size
        self.matrix = [["-" if x is 0 or y is 0 or x is size-1 or y is size-1 else "*" for x in range(size)] for y in range(size)]


    def printLabirint(self):
        for x in self.matrix:
            print(x)