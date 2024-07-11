import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([0.0052, 0.0124, 0.0289, 0.067, 0.1076])
y = np.array([2.679 * 10**-6, 6.389 * 10**-6, 14.9 * 10**-6, 34.52 * 10**-6,55.44 * 10**-6])

plt.plot(x, y, 'o')

#obtain m (slope) and b(intercept) of linear regression line
m, b = np.polyfit(x, y, 1)

#add linear regression line to scatterplot
plt.plot(x, m * x + b)
plt.show()
