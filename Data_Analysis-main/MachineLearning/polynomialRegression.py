import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("positions.csv")
# print(data.columns)
# print(data.describe())

"""
    Index(['Position', 'Level', 'Salary'], dtype='object')
            Level         Salary
    count  10.00000      10.000000
    mean    5.50000  125900.000000
    std     3.02765  146067.298036
    min     1.00000   22000.000000
    25%     3.25000   32000.000000
    50%     5.50000   62500.000000
    75%     7.75000  155000.000000
    max    10.00000  480000.000000
"""
levels = data.iloc[:,1].values.reshape(-1,1) # x
salaries = data.iloc[:,2].values.reshape(-1,1) # y

regression = LinearRegression()
regression.fit(levels,salaries)

plt.xlabel("Seviye")
plt.ylabel("Maaş")
plt.title("SLR")

plt.scatter(levels,salaries, color= "red")
plt.plot(levels,regression.predict(levels),color = "blue")

print('--------------------------------------------------------')

regressionPoly = PolynomialFeatures(degree = 4)
levelsPoly = regressionPoly.fit_transform(levels)
regression2 = LinearRegression()
regression2.fit(levelsPoly,salaries)


plt.plot(levels,regression2.predict(levelsPoly))



plt.show()