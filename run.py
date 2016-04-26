import numpy as np
import pandas as pd
import seaborn as sb

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv');
print (data.head())
print (data.shape)
sb_plot = sb.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales')
sb_plot.savefig("output.png")
