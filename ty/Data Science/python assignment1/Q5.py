maxEven=0
for i in range(1,11):
    if i%2==0:
        if i>maxEven:
            maxEven=i

print(maxEven)