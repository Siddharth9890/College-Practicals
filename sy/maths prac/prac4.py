from math import tan,sin,log,pi


a=32
print(type(a))
a=3.14
print(type(a))
a='pune'
print(type(a))
a=[2,9,1]
print(type(a))
a=(1,5,6,-1)
print(type(a))
a={'a':1,'b':2,'c':3}
print(type(a))
a={'a','b','c','d','e','f'}
print(type(a))

a=3
print(id(a))
a='mumbai'
print(id(a))

a='122'
print(int(a))
a=3.142
print(int(a))
a=-32
print(int(a))

a=range(1,20)
print(list(a))
a=range(1,7)
print(tuple(a))
a='pune university'
print(list(a))


y=tan(sin(pi))
print(y)
c=log(sin(90))
print(c)

def f(x):
    r=x*5
    print(r)
f(20)
f('pune')
