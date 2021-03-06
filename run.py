import numpy as np
import pandas as pd
import seaborn as sb
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn import metrics

data = pd.read_csv('Cars93.csv')
features = ['Cylinders', 'EngineSize', 'Fuel.TankCapacity', 'Passengers', 'Length', 'Wheelbase', 'Width', 'Weight']
target = ['Price']
X=data[features].values
y=data[target].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25)
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

print('Coefficients: \n', regr.coef_)
print('Intercept: \n', regr.intercept_)
print('Variance score: %.2f' % regr.score(X_test, y_test))

y_pred = regr.predict(X_test)

print metrics.mean_absolute_error(y_test, y_pred)
print metrics.mean_squared_error(y_test, y_pred)
print np.sqrt(metrics.mean_squared_error(y_test, y_pred))

sb_plot = sb.pairplot(data, x_vars=['Cylinders', 'Length', 'Width', 'Weight'], y_vars='Price', size=10, aspect=0.7, kind='reg')
sb_plot.savefig("chart.png")


