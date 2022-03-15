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

    def isnull(self):
        for row in range(self.row):
            for col in range(self.col):
                if self.matrix[row][col] != 0: return False
        return True

    def isdiagonal(self):
        if self.issquare:
            dig_ele = False
            for row in range(self.row):
                for col in range(self.col):
                    if row != col:
                        if self.matrix[row][col] !=0: return False
                    else:
                        dig_ele = True if (self.matrix[row][col] != 0) else False
            return dig_ele
        return False

    def isidentity(self):
        if self.issquare:
            iden = False
            for row in range(self.row):
                for col in range(self.col):
                    if row != col:
                        if self.matrix[row][col] != 0 : return False
                    else:
                        if self.matrix[row][col] != 1: return False
                        else: iden = True
            return iden
        return False

    def isscalar(self):
        if self.isnull(): return True
        if self.isdiagonal():
            value = self.matrix[0][0]
            for index in range(self.row):
                if self.matrix[index][index] != value: return False
            return True
        else: return False

    def islowertri(self):
        if self.issquare and not self.isnull():
            for row in range(self.row):
                for col in range(self.col):
                    if (col>row and self.matrix[row][col] != 0) or (col<=row and self.matrix[row][col] == 0): return False
            return True
        else: return False

    def isuppertri(self):
        if self.issquare and not self.isnull():
            for row in range(self.row):
                for col in range(self.col):
                    if (col<row and self.matrix[row][col] != 0) or (col>=row and self.matrix[row][col] == 0): return False
            return True
        else: return False

    def issymmetric(self): return self == self.__invert__() if self.issquare else False

    def det(self):
        if self.row > 3 and self.col>3:
            raise Exception("Only 3 x 3 size matrix allowed")
        if self.row==1 and self.col==1: return self.matrix[0][0]
        if self.issquare:
            index = 0
            index2 =  1
            x1 = x2 = 1
            pos = 0
            neg = 0
            for row in range(self.row):
                x1 = x2 = 1;index=row
                for col in range(self.col):
                    x1 *= self.matrix[col][index]
                    x2 *= self.matrix[index][index2]
                    index += 1
                    index2 -= 1
                    if index>self.col-1: index=0
                    if index2<0: index2=self.col-1
                pos += x1;neg+=x2
            return pos-neg
        else: return False

mat1 = Matrix(4,4,[[4,3,2,2],[0,1,-3,3],[0,-1,3,3],[0,3,1,1]])
# mat2 = Matrix(2,2,[[3,8],[4,6]])
# mat3 = mat1-mat2
# mat1.det()
print(mat1.det())
for arr in mat1.matrix: print(arr)
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
