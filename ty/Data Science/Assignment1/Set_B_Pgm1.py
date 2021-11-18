import pandas as pd
data = pd.read_csv("data.csv")
print("head data");
print(data.head(10));
print("tail data");
print(data.tail(10));
sample=data.sample(20);
print("random 20 sample")
print(sample)
