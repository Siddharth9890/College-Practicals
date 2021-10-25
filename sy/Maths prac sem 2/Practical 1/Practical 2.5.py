import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,2*(np.pi),0.1)
y=np.sin(x)-np.exp(x)+3*x**2+np.log10(x)
plt.plot(x,y)
plt.show()
