from sympy import *

A=Matrix([[1,2,3]])
print(A)

M = Matrix([[1,0,0], [0,0,0]])
print(M)

A=Matrix([[1],[2],[3]])
print(A)

u=Matrix([[2],[5],[-3]])
v=Matrix([[1],[0],[-2]])
print(u+v)
print(u-v)
print(2*u+3*v)

m=Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(m)
print(m.shape)

m=eye(3)
print(m)
n=eye(3)
print(n)

a=Matrix([[1,2,3],[4,5,6],[7,8,9]])
b=Matrix([[1,3,4],[2,4,5],[5,3,1]])
v=Matrix([[1],[5],[6]])
print(a+b)
print(a-b)
print(a*b)
print(a**3)


a=Matrix([[2,1,1],[1,2,1],[1,1,2]])
b=Matrix([[1,1,1],[0,1,1],[0,0,1]])
c=a.row(0)
print("c=",c)
c=a.row(-1)
print("c=",c)

a=Matrix([[2,1,1],[1,2,1],[1,1,2]])
b=a.col_del(1)
print(b)


a=Matrix([[2,1,1],[1,2,1],[1,1,2]])
a=a.row_insert(1,Matrix([[0,5,4]]))
a=a.col_insert(0,Matrix([[0],[5],[6],[4]]))
print(a)



