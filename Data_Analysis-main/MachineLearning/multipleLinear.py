import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("insurance.csv")
# print(data.columns)
# print(data.describe())

expenses = data.expenses.values.reshape(-1,1) # y
ageBmis = data.iloc[:,[0,2]].values # x

regression = LinearRegression()
regression.fit(ageBmis,expenses)

print(regression.predict(np.array([[30,20],[30,21],[20,22],[20,23],[20,24]])))