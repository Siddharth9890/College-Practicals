from math import  sin,cos

def func():
    print("Welcome to Python")

def square(x):
    print(x*x)
    
def f(x):
    r=x*5
    print(r)
func()
a=int(input("enter first number"))
b=int(input("enter second number"))
print(type(a))
print(a+b)
print(a-b)
print(a*b)
print(a**a)
print(a/b)
print(a%b)
print("Sin value of a and sin value of b is",sin(a),sin(a))
print("Cos value of a and b is ",cos(a),cos(b))
square(5)
f("Mumbai")
x=3.0-2j
y=5.0-3j
print(type(x))
print("Complex numbers added are",x+y)
exitkey=input("enter a key to exit")

