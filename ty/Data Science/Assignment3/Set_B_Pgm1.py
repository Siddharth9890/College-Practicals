import pandas as pd
from sklearn import preprocessing 
data = pd.read_csv('Set_B_Data.csv')


print(type(data))
print("\n\n Data Scaled Between 0 to 1") 
data_scaler = preprocessing.MinMaxScaler(feature_range = (0, 1))
print(data_scaler)
data_scaled = data_scaler.fit_transform(data) 
print("\n Min Max Scaled Data ") 
print("-----------------------") 
print(data_scaled.round(2))
