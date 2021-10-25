from sympy import *
A=Matrix([[2,1],[1,2]])
B=Matrix([5,7])
A.gauss_jordan_solve(B)
print(A)

A=Matrix([[1,2,1],[2,1,2]])
B=Matrix([[1],[2]])
sol,params=A.gauss_jordan_solve(B)
print(sol)
print(params)

A=Matrix([[3,1,1,1],[5,-1,1,-1]])
B=Matrix([[0],[0]])
sol,params=A.gauss_jordan_solve(B)
print(sol)
print(params)

A=Matrix([[1,2,1,3],[2,1,2,4]])
B=Matrix([[1],[2]])
sol,params=A.gauss_jordan_solve(B)
print(sol)
print(params)

A=Matrix([[1,-1,-1,2],[2,1,4,1],[2,1,3,4]])
L,U,_=A.LUdecomposition()
print(L)
print(U)

from sympy.abc import x,y,z
AB=Matrix([[6,4,3,2],[5,3,4,2],[5,6,7,3]])
print(solve_linear_system_LU(AB,[x,y,z]))
