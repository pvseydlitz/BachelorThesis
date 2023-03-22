#Tutorial: https://www.youtube.com/watch?v=NUXdtN1W1FE
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

companies = pd.read_csv('./Data/Test/1000_companies.csv')
X = companies.iloc[:, :-1].values
Y = companies.iloc[:, :-4].values

print(companies.head())

sns.heatmap(companies.corr(numeric_only=True))
plt.show()

#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])

from sklearn.compose import ColumnTransformer 
onehotencoder = ColumnTransformer([("Profit", OneHotEncoder(),[3])], remainder="passthrough")
X = onehotencoder.fit_transform(X)

#Avoiding dummy variable trap
X = X[:, 1:]

#Splitting the data into Train and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#Fitting multiple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)
print(Y_pred)

#Calculating the coefficients
print(regressor.coef_)

#Calculating the intercept
print(regressor.intercept_)

#Calculating the r squared value
from sklearn.metrics import r2_score
r2_score(Y_test, Y_pred)
print(r2_score)