class Matrix:
    def __init__(self,row=1,col=1):
        self.row = row
        self.col = col
        self.matrix = [[0 for col in range(self.col)]for row in range(self.row)]


mat = Matrix()
print(mat.matrix)
