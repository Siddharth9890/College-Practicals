marks=[]
for i in range(5):
    value=int(input())
    marks.append(value)


sum=0
for i in range(5):
    sum+=marks[i]

total=500
print("Percentage is ",(sum/total)*100)