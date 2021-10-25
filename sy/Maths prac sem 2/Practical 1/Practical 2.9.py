import matplotlib.pyplot as plt
ages=[2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,40,45,32,38]
range=(0,100)
bins=5
plt.hist(ages,bins,range,color='blue',histtype='bar',rwidth=0.8)
plt.xlabel('age')
plt.ylabel('No.of people')
plt.title('histogram plot')
plt.show()
