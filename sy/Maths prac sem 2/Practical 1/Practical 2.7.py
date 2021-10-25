import matplotlib.pyplot as plt
x1=[1,2,3]
y1=[3,6,2]
plt.plot(x1,y1,label='line 1')
x2=[1,2,3]
y2=[7,2,5]
plt.plot(x2,y2,label='line 2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two lines on the same graph')
plt.legend()
plt.show()
