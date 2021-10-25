t=tuple('demo')
print(t)
t1=tuple([1,2,3,'python','pandas'])
print(t1)

tuple1=(1,2,3,4,5,6)
type(tuple1)
tuple2=tuple1[3:5]
print(tuple2)

tup1=()
print(tup1)

tup1=('physics','maths','chem',1998)
tup2=(1,2,3,4,5,6,7,8,9,10)
print('tup1[0]',tup1[0])
print("tup2[1:5]",tup2[1:5])

tup3=tup1+tup2
print(tup3)

n_tuple=("mouse",[1,2,3],[4,5,6])
print(n_tuple[0][1])
print(n_tuple[1][2])
print(n_tuple[2][-1])

my_tuple=('p','y','t','h','o','n')
print(my_tuple[:])

t1=(10,20,40)
t2=(90,80,70)
t1,t2=t2,t1
print(t1)
print(t2)

def circleinfo(r):
    c=2*3.142*r
    a=3.142*r*r
    return (c,a)
print(circleinfo(10))
