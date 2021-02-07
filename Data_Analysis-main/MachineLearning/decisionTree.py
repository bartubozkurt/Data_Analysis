import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("positions.csv")
# print(data.columns)
levels  = data.iloc[:,1].values.reshape(-1,1)
salaries  = data.iloc[:,2].values.reshape(-1,1)

regression = DecisionTreeRegressor()
regression.fit(levels,salaries)

plt.scatter(levels,salaries, color = "red")
x = np.arange(min(data.Level),max(data.Salary),0.01).reshape(-1,1)
plt.plot(x,regression.predict(x), color = "orange")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Decision Tree Model")
plt.show()