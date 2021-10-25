from sympy import *

A=Matrix([[4,6,-3],[-4,1,6],[0,8,-9]])
print(A)
print(A.T)

B=Matrix([[4,6,-3],[-4,1,6],[0,8,-9]])
A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(A)
print(A.det())
print(B)
print(B.det())

B=Matrix([[4,6,-3],[-4,1,6],[0,8,-9]])
A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(A.rref())
print(B.rref())

B=Matrix([[4,6,-3],[-4,1,6],[0,8,-9]])
A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(A.nullspace())
print(B.nullspace())

B=Matrix([[4,6,-3],[-4,1,6],[0,8,-9]])
A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(A.columnspace())
print(B.columnspace())

B=Matrix([[4,6,-3],[-4,1,6],[0,8,-9]])
A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(A.rank())
print(B.rank())

x,y,z=symbols("x,y,z")
A=Matrix([[3,2,-1],[2,-2,4],[2,-1,2]])
b=Matrix([[3,6,9]])
print(linsolve((A,b),[x,y,z]))

x,y,z=symbols("x,y,z")
A=Matrix([[7,6,-8],[7,-2,2],[7,8,9]])
b=Matrix([[3,6,9]])
print(linsolve((A,b),[x,y,z]))

