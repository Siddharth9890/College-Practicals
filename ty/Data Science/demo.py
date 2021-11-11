import numpy as np 
import matplotlib.pyplot as plt 
import pandas 
df=pandas.DataFrame(columns=["name","age","percentage"]) 
df.loc[0] = ['sagar', '19', 7] 
df.loc[1] = ['aaves', '25', 21] 
df.loc[2] = ['amaan', '56', 19] 
df.loc[3] = ['sai', '100', 15] 
df.loc[4] = ['sargam', '10', 35] 
df.loc[5] = ['sid', '20', 65] 
df.loc[6] = ['ro', '100', 15] 
df.loc[7] = ['ali', '100', 15] 
df.loc[8] = ['si', '100', 15] 
df.loc[9] = ['s', '100', 15] 
df.loc[10] = ['l', '40', 15] 
 
df.plot(x="name", y="percentage") 
plt.show() 
