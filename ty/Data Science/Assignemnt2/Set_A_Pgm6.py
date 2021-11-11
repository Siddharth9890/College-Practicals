import pandas 
df=pandas.DataFrame(columns=["name","age","marks"]) 
df.loc[0] = ['sagar', 19, 7] 
df.loc[1] = ['ashish', 25, 21] 
df.loc[2] = ['aman', 56, 19] 
df.loc[3] = ['sayali', 100, 15] 
df.loc[4] = ['sa', 10, 35] 
df.loc[5] = ['yal', 20, 65] 
df.loc[6] = ['i', 100, 15] 
df.loc[7] = ['ali', 100, 15] 
df.loc[8] = ['si', 100, 15] 
df.loc[9] = ['s', 100, 15] 
df.loc[10] = ['l', 40, 15] 
print(df)
print(df["age"].mean())
print(df["marks"].mean())
print(df.describe())
