import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-white")
def f(x,y):
    return np.sin(x)**10+np.cos(5+y*x)*np.sin(x)
x=np.linspace(0,5,50)
y=np.linspace(0,5,50)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
plt.contourf(X,Y,Z,20,cmap='RdBu')
plt.colorbar()
plt.show()
