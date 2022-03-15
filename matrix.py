class Matrix:
    def __init__(self,row=1,col=1,elements=None):
        self.row = row
        self.col = col
        self.order = "%d x %d"%(row,col)
        self.matrix = []
        self.issquare = self.row==self.col
        if elements==None:
            self.matrix = [[0 for col in range(self.col)] for row in range(self.row)]
        else:
            if not isinstance(elements,list):
                    raise TypeError("Expecting type \"list\" but got type \"%s\""%type(elements))
            self.matrix = [[elements[row][col] for col in range(self.col)] for row in range(self.row)]

    def __add__(self,matrix):
        if not isinstance(matrix,Matrix):
            raise TypeError("Expecting a Matrix but got \"%s\""%matrix)
        if (self.row == matrix.row and self.col == matrix.col):
            new_matrix = Matrix(self.row,self.col,[[self.matrix[row][col]+matrix.matrix[row][col] for col in range(self.col)] for row in range(self.row)])
        else:
            raise ValueError("The two matrices must be the same size, i.e. the rows must match in size, and the columns must match in size.")
        return new_matrix

    def __sub__(self,matrix):
        if not isinstance(matrix,Matrix):
            raise TypeError("Expecting a Matrix but got \"%s\""%matrix)
        if (self.row == matrix.row and self.col == matrix.col):
            new_matrix = Matrix(self.row,self.col,[[self.matrix[row][col]-matrix.matrix[row][col] for col in range(self.col)] for row in range(self.row)])
        else:
            raise ValueError("The two matrices must be the same size, i.e. the rows must match in size, and the columns must match in size.")
        return new_matrix

    def __neg__(self):
        return Matrix(self.row,self.col,[[-self.matrix[row][col] for col in range(self.col)] for row in range(self.row)])

    def __invert__(self):
        return Matrix(self.col,self.row,[[self.matrix[col][row] for col in range(self.row)] for row in range(self.col)])

    def __eq__(self,matrix):
        if not isinstance(matrix,Matrix):
            raise TypeError("Expecting a Matrix but got \"%s\""%matrix)
        return self.matrix == matrix.matrix if (self.row == matrix.row and self.col == matrix.col) else False

    def __mul__(self,const):
        if isinstance(const,Matrix):
            const = ~const
            if self.col == const.col:
                new_matrix = Matrix(self.row,const.row)
                for row in range(new_matrix.row):
                    for col in range(new_matrix.col):
                        for index in range(self.col):
                            new_matrix.matrix[row][col] += self.matrix[row][index]*const.matrix[col][index]
                return new_matrix
            else:
                raise TypeError("To multiply an 'm x n' matrix by an 'n x p' matrix, the n's must be the same, and the result is an 'm x p' matrix.")

        else:
            new_matrix = Matrix(self.row,self.col,[[const*self.matrix[row][col] for col in range(self.col)] for row in range(self.row)])
        return new_matrix


    def update(self,new_mat:list):
        if not isinstance(new_mat,list):
            raise TypeError("Expecting type \"list\" but got type \"%s\""%type(new_mat))
        else:
            self.matrix = [[new_mat[row][col] for col in range(self.col)] for row in range(self.row)]

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

    def isidentity(self):
        if self.issquare:
            value = 0
            for row in range(self.row):
                for col in range(self.col):
                    if row != col:
                        if self.matrix[row][col] != 0 : return False
                    else:
                        if self.matrix[row][col] != 1: return False
                        else: value += 1
            return True if value==self.row else False
        return False

mat1 = Matrix(2,2,[[3,8],[4,6]])
mat2 = Matrix(2,2,[[1,8],[4,6]])
mat3 = mat1 - mat2
print(mat1 != mat2)
for arr in mat3.matrix: print(arr)
# print("Old Matrix")
# for arr in mat.matrix: print(arr)
# print("Square Matrix : %s\nIdentity Matrix : %s\nOrder : %s"%(mat.issquare,mat.isidentity(),mat.order))
# print("Diagonal Matrix: %s"%(mat.isdiagonal()))
# print()
# mat.update([[1 if row==col else 0 for col in range(mat.col)]for row in range(mat.row)])
# print("New Matrix")
# for arr in mat.matrix: print(arr)
# print("Square Matrix : %s\nIdentity Matrix : %s\nOrder : %s"%(mat.issquare,mat.isidentity(),mat.order))
# print("Diagonal Matrix: %s"%(mat.isdiagonal()))
