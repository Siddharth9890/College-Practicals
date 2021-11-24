import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()


data = pd.read_csv('Set_A_Data.csv')
print(data)
print('describe \n', data.describe())
print('shape\n', data.shape)
print('first 3 rows\n', data.head(3))

meanAge = data['Age'].mean()
meanSalary = data['Salary'].mean()
data['Age'].fillna(meanAge, inplace=True)
data['Salary'].fillna(meanSalary, inplace=True)

print('new data\n', data)

data['Purchased'] = labelencoder.fit_transform(data['Purchased'])
print('label encoding on purchased column \n', data)

enc = OneHotEncoder(handle_unknown='ignore')
enc_df = pd.DataFrame(enc.fit_transform(data[['Country']]).toarray())
data=data.join(enc_df)
print('one hot encoding \n',data)
