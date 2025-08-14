import ast
import copy
import sys

if len(sys.argv) != 2:
    print("Error1")
    sys.exit(1)

#ast.literal_eval() returns the python object    
try:
    matrix = ast.literal_eval(sys.argv[1]) 
except Exception:
    print("Error2")
    sys.exit(2)
        
for i in matrix:
    for j in i:
        if type(j) is not int:
            sys.exit(2)
            
    #If it's not a square matrix            
if len(matrix) != len(matrix[0]):
    print("Error4")
    sys.exit(3)
                
#Define a class for the Matxix
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
            
    #Calculate the cofactor
    def cofactor(self, mat, row):
        cofactors = []
        for col in range(len(mat)):
            sub_matrix = []
            for i in range(len(mat)):
                if i != row:
                    new_row = []
                    for j in range(len(mat[i])):
                        if j != col:
                            new_row.append(mat[i][j])
                    sub_matrix.append(new_row) 
            sign = (-1)**(row + col)
            element = mat[row][col]
            signed_element = sign * element
            cofactors.append((signed_element, sub_matrix))  
        return cofactors                          
            
            
        
    #Determinant of 2x2 matrix
    def det_of_two(self, mat):
        self.mat = mat
        det = (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])
        return det
        
    #Calculate the determinant of the nXn matrix recursively
    def determinant(self, mat):
        if len(mat) == 2:
                return self.det_of_two(mat)   
        cofactors = self.cofactor(mat, 0)
        total_det = 0
        for sign,submatrix in cofactors:
            det_of_cofactor = self.determinant(submatrix)
            total_det += sign*det_of_cofactor    
        return total_det
    
    def inverse_of_two(self, mat):
        if len(mat) != 2:
            print("Error not a 2x2 matrix")
            sys.exit(4)    
        det = self.det_of_two(mat)
        if det == 0:
            print("Error: Matrix is not invertible (determinant = 0)")
            sys.exit(4)
        a, b = mat[0][0], mat[0][1]
        c, d = mat[1][0], mat[1][1]
        
        inverse = [
            [d/det, -b/det],
            [-c/det, a/det]
        ]
        return inverse
    
    #calculat the inverse of NxN matrix using adjugate method
    def inverse(self, mat):
        if len(mat) == 2:
            return self.inverse_of_two(mat)
        deter = self.determinant(mat)
        if deter == 0:
            print("Error: matrix is not invertible, determinant = 0")
            sys.exit(6)
        cofactor_matrix = []
        #Expand the matrix for the number of rows
        for i in range(len(mat)):
            new_row = []
            sub_matrices = self.cofactor(mat, i) #Find the sub_matrices along each row
            for j, (signed_element, sub_matrix) in enumerate(sub_matrices):#Iterate through each of the submatrix
                value = ((-1)**(i+j))*self.determinant(sub_matrix)#Find it's determinant
                new_row.append(value) #Add the value to the new_row
            cofactor_matrix.append(new_row) #Add the row to the transpose matrix  
        adjugate = []     
        for i in range(len(cofactor_matrix)):
            row = []
            for j in range(len(cofactor_matrix[0])):
                row.append(cofactor_matrix[j][i])
            adjugate.append(row)
        inverse = []
        for k in range(len(adjugate)):
            rows = []
            for l in range(len(adjugate[0])):
                rows.append(adjugate[l][k]) 
            inverse.append(rows)
        return inverse                              
                      
                    
        
m = Matrix(matrix)
result = m.determinant(matrix)
inverse = m.inverse(matrix)
print(inverse)
print(result)    
    
    
            
                   
            
                
            
                                               
                        
            
            