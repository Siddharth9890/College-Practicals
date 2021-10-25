import math

n=1
while n<=5:
    print(n)
    n+=1
sum=0
n=1
while n<=10:
    sum+=n
    n+=1
print(sum)

def multitable(n):
    i=1
    while i<=10:
        print(i*n,end=',')
        i+=1
multitable(5)
print("\n")
multitable(6)
