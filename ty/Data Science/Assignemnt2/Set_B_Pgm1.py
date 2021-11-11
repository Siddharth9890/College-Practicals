import pandas as pd
data = pd.read_csv("iris.csv")
sample1 = data.sample(5)
print(sample1)

print("max sepal.length", data["sepal.length"].max())
print("min sepal.length", data["sepal.length"].min())

print("max sepal.width", data["sepal.width"].max())
print("min sepal.width", data["sepal.width"].min())

print("max petal.length", data["petal.length"].max())
print("min petal.length", data["petal.length"].min())

print("max petal.width", data["petal.width"].max())
print("min petal.width", data["petal.width"].min())

# Pgm2

data2=data.groupby("variety").nunique()
print(data2)

# Pgm 3
print("mean sepal.length", data["sepal.length"].mean())
print("median sepal.length", data["sepal.length"].median())

print("mean sepal.width", data["sepal.width"].mean())
print("median sepal.width", data["sepal.width"].median())

print("mean petal.length", data["petal.length"].mean())
print("median petal.length", data["petal.length"].median())

print("mean petal.width", data["petal.width"].mean())
print("median petal.width", data["petal.width"].median())
