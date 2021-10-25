from sympy import *
A=Matrix([[1,2,1],[2,1,2],[2,2,1]])
print(A.eigenvals())

A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(A.eigenvals())

A=Matrix([[1,2,2],[2,1,2],[2,2,1]])
print(A.eigenvals())

A=Matrix([[1,2,1],[2,1,2],[2,2,1]])
print(A.eigenvects())

A=Matrix([[1,2,1],[2,1,2],[2,2,1]])
P,D=A.diagonalize()
print(P)

A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
P,D=A.diagonalize()
print(P)

A=Matrix([[1,1,1],[0,1,1],[0,0,1]])
print(A.is_diagonalizable())

A=Matrix([[1,2,1],[2,1,2],[2,2,1]])
print(A.is_diagonalizable())





