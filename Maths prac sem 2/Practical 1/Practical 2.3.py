import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,2,100)
y=x**2
fig=plt.figure(figsize=(10,5))
plt.plot(x,y)
plt.show()
