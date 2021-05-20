import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,14,45,32,15]
city=['pune','mumbai','nagpur','nashik','satara']
fig=plt.figure(figsize=(10,7))
plt.pie(y,labels=city)
plt.show()
