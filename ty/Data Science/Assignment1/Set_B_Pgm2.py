import pandas as pd
data = pd.read_csv("data.csv")

print(data.size)
print(data.describe)
print("Height mean,median,mode")
print(data["Height"].mean())
print(data["Height"].median())
print(data["Height"].mode())
print("weight mean,median,mode")
print(data["Weight"].mean())
print(data["Weight"].median())
print(data["Weight"].mode())

