import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from project2 import preprocessing
from sklearn.linear_model import LinearRegression
pre=preprocessing()
'''
indoor2016=pre.indoor2016()
print(indoor2016)

in16_model_data=indoor2016[['Location','GDP per capita (in USD)','Indoor air pollution (deaths per 100,000)','First Tooltip']]
in16_model_data=in16_model_data.dropna()
print(in16_model_data)


fig1=plt.scatter(in16_model_data['First Tooltip'],in16_model_data['Indoor air pollution (deaths per 100,000)'])
plt.show()

'''

indoor=pre.indoor()
print(indoor.columns)
in_data=indoor[['Location','Year','First Tooltip','Indoor air pollution (deaths per 100,000)','GDP per capita (in USD)']]
in_data=in_data.dropna()
print(in_data)
fig1=plt.scatter(in_data['GDP per capita (in USD)'],in_data['Indoor air pollution (deaths per 100,000)'])
plt.show()

'''
out=pre.outdoor()
print(out.columns)
out_data=out[['Location','Year','Outdoor particulate matter (deaths per 100,000)','GDP per capita (in USD)','Oil (% sub energy)','Coal (% sub energy)']]
out_data=out_data.dropna()
out_data['clean']=100
out_data['clean']=out_data['clean']-out_data['Oil (% sub energy)']-out_data['Coal (% sub energy)']
fig1=plt.scatter(out_data['clean'],out_data['Outdoor particulate matter (deaths per 100,000)'])
plt.show()
print(np.corrcoef(out_data['clean'],out_data['Outdoor particulate matter (deaths per 100,000)']))
'''
#indoor basic mode
in_model=LinearRegression()
in_model.fit(in_data[['First Tooltip','GDP per capita (in USD)']],in_data['Indoor air pollution (deaths per 100,000)'])
print(in_model.score(in_data[['First Tooltip','GDP per capita (in USD)']],in_data['Indoor air pollution (deaths per 100,000)']))


#indoor model2
in_model1=LinearRegression()
print(in_data[in_data['GDP per capita (in USD)']>20000]['Indoor air pollution (deaths per 100,000)'].mean())
in_data1=in_data[in_data['GDP per capita (in USD)']>20000]
in_model1.fit(in_data1[['First Tooltip','GDP per capita (in USD)']],in_data1['Indoor air pollution (deaths per 100,000)'])
print(in_model1.score(in_data1[['First Tooltip','GDP per capita (in USD)']],in_data1['Indoor air pollution (deaths per 100,000)']))
print(in_model1.coef_,in_model1.intercept_)

#indoor model3
in_model2=LinearRegression()
in_data2=in_data1
in_data2['intereact']=in_data2['GDP per capita (in USD)']*in_data2['First Tooltip']
in_model2.fit(in_data2[['First Tooltip','GDP per capita (in USD)','intereact']],in_data2['Indoor air pollution (deaths per 100,000)'])
print(in_model2.score(in_data2[['First Tooltip','GDP per capita (in USD)','intereact']],in_data2['Indoor air pollution (deaths per 100,000)']))
print(in_model2.coef_,in_model1.intercept_)
#no intereact for the two term