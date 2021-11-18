import pandas as pd
import matplotlib.pyplot as plot
data = pd.read_csv("data.csv")

print(data)
data["BMI"]=data["Weight"]/(data["Height"]*data["Height"])
print(data)

print(data["BMI"].max())
print(data["BMI"].min())

data.plot.scatter(x='Height', y='Weight')
plot.show()
