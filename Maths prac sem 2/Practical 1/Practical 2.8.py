import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,14,45,32,15]
city=['pune','mumbai','nagpur','nashik','satara']
plt.bar(x,y,tick_label=city,width=0.8,color=['red','green'])
plt.xlabel('cities')
plt.ylabel('No. of covid patient(in thousands)')
plt.title('Covid-19 data')
plt.show()
