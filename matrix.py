import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def dot_product(vector_one, vector_two):
        s=0
        print("\nvect1 dot vect2: \n" + str(vector_one) +"  "+ str(vector_two))
        for r in range(len(vector_one)):
            s = s + vector_one[r]*vector_two[r]
        return s

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
 
        elif self.h == 1 and self.w == 1:
            self.det = self.g[0][0]
            return self.det

        else:
            self.a = self.g[0][0]
            self.b = self.g[0][1]
            self.c = self.g[1][0]
            self.d = self.g[1][1]
            self.det = self.a*self.d - self.b*self.c
            return self.det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        if self.h == 1 and self.w == 1:
            trace = self.g[0][0]
            return trace
        else:
            n = len(self.g)
            print("In trace function: \n")
            print("Current matrix: \n" + str(self))
            trace = 0
            for i in range(n):
                trace = trace + self.g[i][i]
            
            return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        if self.h == 1 and self.w == 1:
            matrix_Inv = Matrix([[0]])
            matrix_Inv.g[0][0] = 1/self.g[0][0]
            
            return matrix_Inv
        
        else:
            self_factor = 1/self.determinant()
            print("\nself_factor: " + str(self_factor))
            
            self_tr = self.trace()
            print("self_tr: " + str(self_tr))
            
            self_I = identity(2)        
            print("self_I: \n" + str(self_I))
            
            self_trAI = self_tr*self_I
            print("self_trAI: \n" + str(self_trAI))
          
            self_sub = self_trAI-self
            print("self_sub: \n" + str(self_sub))
            
            self_Inv = self_factor*self_sub
            print("self_factor: " + str(self_factor))
     
            return self_Inv                     
                          

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        
        if self.h == 1 and self.w == 1:
            return self.g[0]
        
        else:
            w = self.w
            h = self.h
            matrix_T = zeroes(w,h)#flips the matrix dimensions
            
            print("Zero matrix ready for transformation matrix: \n" + str(matrix_T))
            
            for r in range(matrix_T.h):
                for c in range(matrix_T.w):
                    matrix_T.g[r][c]=self.g[c][r]#added .g
            print("\nType of object leaving transform function:\n" + str(type(matrix_T)))  
            return matrix_T

        
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        print("I'm in the add overloaded operator")

        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        else:

            print("Here are the add matrices: \n" + str(self)+ '\n'+str(other))
            
            
            added_matrix = zeroes(self.h, self.w)
            
            for i in range(self.h):
                for j in range(self.w):
                    self.g[i][j] = self.g[i][j] - other.g[i][j]
            
            return added_matrix
            
            """added_matrix = Matrix([
                                  [self.g[0][0] + other.g[0][0],
                                   self.g[0][1] + other.g[0][1]],
                                  [self.g[1][0] + other.g[1][0],
                                   self.g[1][1] + other.g[1][1]]
                                  ])
            return added_matrix"""
       

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        neg_Matrix  = Matrix([
                            [self.g[0][0] *-1,
                             self.g[0][1] *-1],
                            [self.g[1][0] *-1,
                             self.g[1][1] *-1]
                            ])
        
        return neg_Matrix
                

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        
        else:
            
            subtracted_matrix = zeroes(self.h, self.w)
            
            for i in range(self.h):
                for j in range(self.w):
                    self.g[i][j] = self.g[i][j] - other.g[i][j]
            
            return subtracted_matrix
        
            """subtracted_matrix = Matrix([
                              [self.g[0][0] - other.g[0][0],
                              self.g[0][1] - other.g[0][1]],
                              [self.g[1][0] - other.g[1][0],
                              self.g[1][1] - other.g[1][1]]
                              ])

            return subtracted_matrix"""

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        print("In mul function")
        print("self matrix: " + str(self.g))
        print("\nother matrix: \n" + str(other))
        print("other type: \n" + str(type(other)))
        other_T = other.T()
        print("other_T: \n" + str(other_T))
        print("other_T type: \n" + str(type(other_T)))

        #matrix_mul = zeroes(self.h,self.h) worked for test()
        matrix_mul = zeroes(self.h, other.w)#provides better zero matrix than (self.h other.h) for 1 x 2 self.h matrix
        print("zeros matrix for dot product: \n" + str(matrix_mul.g))
        
        for r in range(self.h):
            for t in range(other_T.h): #or self.h
                dot_prod = dot_product(self.g[r], other_T.g[t])
                print("\ndot_prod: " + str(dot_prod))
                matrix_mul.g[r][t] = dot_prod
                
        return matrix_mul

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        
        if isinstance(other, numbers.Number):
   
            self_rmul = zeroes(self.h,self.w)
            
            for i in range(self.h):
                for j in range(self.w):
                    self_rmul.g[i][j] = self.g[i][j]*other
            
            
            return self_rmul
            
              