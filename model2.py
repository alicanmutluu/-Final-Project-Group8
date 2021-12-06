import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from project2 import preprocessing
from sklearn.linear_model import LinearRegression

pre=preprocessing()





out=pre.Merge_energy()
out_data=out[['Location', 'Year', 'Coal Consumption - EJ',
       'Oil Consumption - EJ','GDP per capita (in USD)','Population','Outdoor particulate matter (deaths per 100,000)']].copy()
out_data=out.dropna()
print(len({i for i in out_data['Location']}))
print(out_data.shape)
print(out.columns)
out_data['Oil Consumption - kwh']=out_data['Oil Consumption - EJ'].map(lambda x: x*277777777777.78)
out_data['Energy from oil per capita']=out_data['Oil Consumption - kwh']/out_data['Population']
out_data['Coal Consumption - kwh']=out_data['Coal Consumption - EJ'].map(lambda x: x*277777777777.78)
out_data['Energy from coal per capita']=out_data['Coal Consumption - kwh']/out_data['Population']
print(np.corrcoef(out_data['GDP per capita (in USD)'],out_data['Outdoor particulate matter (deaths per 100,000)']))

model=LinearRegression()
model.fit(out_data[['GDP per capita (in USD)']],out_data['Outdoor particulate matter (deaths per 100,000)'])
print(model.score(out_data[['GDP per capita (in USD)']],out_data['Outdoor particulate matter (deaths per 100,000)']))
plt.scatter(out_data['GDP per capita (in USD)'],out_data['Outdoor particulate matter (deaths per 100,000)'])
plt.show()

plt.scatter(out_data[['Energy from oil per capita']],out_data['Outdoor particulate matter (deaths per 100,000)'])
plt.show()

#

