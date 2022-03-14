class Matrix:
    def __init__(self,row=1,col=1,elements=None):
        self.row = row
        self.col = col
        self.order = "%d x %d"%(row,col)
        self.matrix = []
        if elements==None:
            self.matrix = [[0 for col in range(self.col)] for row in range(self.row)]
        else:
            if not isinstance(elements,list):
                    raise ValueError("Expecting type \"list\" but got type \"%s\""%type(elements))
            self.matrix = [[elements[row][col] for col in range(self.col)] for row in range(self.row)]

        self.issquare = self.row==self.col

    def update(self,new_mat:list):
        if not isinstance(new_mat,list):
            raise ValueError("Expecting type \"list\" but got type \"%s\""%type(new_mat))
        else:
            self.matrix = [[new_mat[row][col] for col in range(self.col)] for row in range(self.row)]

    def isidentity(self):
        value = 0
        for row in range(self.row):
            for col in range(self.col):
                if row != col:
                    if self.matrix[row][col] != 0 : return False
                else:
                    if self.matrix[row][col] != 1: return False
                    else: value += 1
        return True if value==self.row else False

    def isdiagonal(self):
        if self.issquare:
            dig_ele = 0
            for row in range(self.row):
                for col in range(self.col):
                    if row != col:
                        if self.matrix[row][col] !=0: return False
                    else:
                        dig_ele += 1 if (row==col and self.matrix[row][col] != 0) else 0
            return True if dig_ele>0  else False
        return False


mat = Matrix(3,3)
print("Old Matrix")
for arr in mat.matrix: print(arr)
print("Square Matrix : %s\nIdentity Matrix : %s\nOrder : %s"%(mat.issquare,mat.isidentity(),mat.order))
print("Diagonal Matrix: %s"%(mat.isdiagonal()))
print()
mat.update([[1 if row==col else 0 for col in range(mat.col)]for row in range(mat.row)])
print("New Matrix")
for arr in mat.matrix: print(arr)
print("Square Matrix : %s\nIdentity Matrix : %s\nOrder : %s"%(mat.issquare,mat.isidentity(),mat.order))
print("Diagonal Matrix: %s"%(mat.isdiagonal()))
