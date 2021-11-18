import pandas as pd
data = pd.read_csv("data.csv")

# print(data["Height"].value_counts())
print(data["Height"].isnull().sum())
