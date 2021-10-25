import math

def multi5(a):
    if a%5==0:
        print(a,'is a multiple of 5')

multi5(5)
multi5(7)

def isdivisible(x,y):
    if x%y==0:
        print(x,'is divisble by ',y)

isdivisible(15,5)
isdivisible(25,3)

def f(x):
    if x>=100 and x%5==0:
        print(x,'is divisible by 5 and greater than 100')
f(100)
f(10)

def func(x):
    if x%2==0:
        print(x,'is even')
    else:
        print(x,'is odd')

func(2)
func(3)

def f(x):
    if x>0:
        print(x,'is positive')
    else:
        if x<0:
            print(x,'is negative')
        else:
            print(x,'is zero')
f(1)
f(0)
f(-10)

def compare(x,y):
    if x<y:
        print(x,'is less than ',y)
    elif x>y:
        print(x,'is greater than ',y)
    else:
        print(x,'is equal to ',y)

compare(10,100)
compare(-1,-2)
compare(0,0)

def clgmarks(x):
    if x<=39:
        print(x,'Fail')
    elif x<=49:
        print(x,'Second Class')
    elif x<=59:
        print(x,'Higher Second Class')
    elif x<=75:
        print(x,'First Class')
    else:
        print(x,'Distinction')

clgmarks(60)
clgmarks(80)
