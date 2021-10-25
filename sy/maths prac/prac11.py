def nr(f,g,x0,e):
    step=1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        x1=x0-f(x0)/g(x0)
        print('Iteration =',step,'x1 =',x1,'and f(x1) =',f(x1))
        x0=x1
        step=step+1
        condition = abs(f(x1))>e
    print('required root is:',x1)

from math import *
def f(x):
    return x**3+3*x-2
def g(x):
    return 3*x**2+3

print(nr(f,g,10,0.00001))
print(nr(f,g,0.7,0.00000001))
print(nr(f,g,1,0.0000000000000001))


def fp(f,x0,x1,e):
    if f(x0) == f(x1) > 0.0:
        print('given guess valoue do not bracket the root.')
        print('try again with difffernt guess value.')
    else:
        step=1
        condition = True
        while condition:
            x2=x0-(x1-x0)*f(x0)/(f(x1)-f(x0))
            print('Iteration =',step,'x2 =',x2,'and f(x2) =',f(x2))
            if f(x0)==f(x2)<0:
                x1=x2
            else:
                x0=x2
            step=step+1
            condition = abs(f(x2))>e
    print('required root is:',x2)

from math import *
def f(x):
    return x**3-5*x-9
     
fp(f,2,4,0.0000001)
fp(f,2,4,0.00000000001)















        
