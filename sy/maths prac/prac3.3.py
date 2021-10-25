import math
print(list(range(10)))
print(list(range(2,10)))
print(list(range(20,8)))
print(list(range(2,20,3)))
print(list(range(20,1,-3)))

n=range(7,1000,7)
print(len(n))

for i in range(4):
    print("hello")

for i in [0,2,7,9]:
    print(i*i)

print('\n')
for i in ['M','H','12','NM','1234']:
    print(i,end=' ')

print('\n')
for i in 'PUNE':
    print(i*2)

print('\n')
x=range(3,8)
for n in x:
    print(n)

print('\n')
def divisor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=' ')

divisor(60)
