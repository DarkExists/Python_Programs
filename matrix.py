class Matrix:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.matrix = [[0 for col in range(self.col)]for row in range(self.row)]
