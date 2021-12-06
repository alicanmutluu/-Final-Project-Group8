import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from preprocessor import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
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
'''
plt.scatter(out_data['GDP per capita (in USD)'],out_data['Outdoor particulate matter (deaths per 100,000)'])
plt.title('Outdoor fatality rate and GDP')
plt.show()

plt.scatter(out_data[['Energy from oil per capita']],out_data['Outdoor particulate matter (deaths per 100,000)'])
plt.show()
plt.scatter(out_data[['Energy from coal per capita']],out_data['Outdoor particulate matter (deaths per 100,000)'])
plt.show()
'''
print(len({i for i in out_data[out_data['Energy from oil per capita']>40000]['Location']}))
print(len({i for i in out_data[out_data['Energy from oil per capita']==0]['Location']}))
print(len({i for i in out_data[out_data['Energy from coal per capita']==0]['Location']}))
#
#model 2 with generated feature
out_data=out_data[out_data['Energy from coal per capita']!=0]
out_data['GDP/fuel']=out_data['GDP per capita (in USD)']/(out_data['Energy from coal per capita']+out_data['Energy from oil per capita'])
plt.scatter(out_data['GDP/fuel'],out_data['Outdoor particulate matter (deaths per 100,000)'])
plt.title('Outdoor fatality rate and GDP/fuel')
plt.ylabel('Fatality per 100,000')
plt.xlabel('GDP/fuel')
plt.savefig('Outdoor fatality rate and GDP fuel.png')
plt.show()
out_data1=out_data.copy()
out_data1['Outdoor particulate matter (deaths per 100,000)']=out_data1['Outdoor particulate matter (deaths per 100,000)'].map(lambda x: np.log(x))


model2=LinearRegression()
model2.fit(out_data1[['GDP/fuel','GDP per capita (in USD)']],out_data1['Outdoor particulate matter (deaths per 100,000)'])
print(model2.score(out_data1[['GDP/fuel','GDP per capita (in USD)']],out_data1['Outdoor particulate matter (deaths per 100,000)']))
resid=model2.predict(out_data1[['GDP/fuel','GDP per capita (in USD)']])-out_data1['Outdoor particulate matter (deaths per 100,000)']
plt.scatter(out_data1['GDP/fuel'],resid)
plt.ylabel('residual')
plt.xlabel('GDP/fuel')
plt.title('outdoor model trasnformed residual')
plt.savefig('residual for outdoor transformed model.png')
plt.show()
#model3 with squared feature
out_data1['GDP/fuel squared']=out_data1['GDP/fuel'].map(lambda x:x*x)
model2=LinearRegression()
model2.fit(out_data1[['GDP/fuel','GDP/fuel squared','GDP per capita (in USD)']],out_data1['Outdoor particulate matter (deaths per 100,000)'])
print(model2.score(out_data1[['GDP/fuel','GDP/fuel squared','GDP per capita (in USD)']],out_data1['Outdoor particulate matter (deaths per 100,000)']))
resid=model2.predict(out_data1[['GDP/fuel','GDP/fuel squared','GDP per capita (in USD)']])-out_data1['Outdoor particulate matter (deaths per 100,000)']

print(model2.coef_,model2.intercept_)
pred=model2.predict(out_data1[['GDP/fuel','GDP/fuel squared','GDP per capita (in USD)']])
mse=mean_squared_error(out_data1['Outdoor particulate matter (deaths per 100,000)'], pred)

print('mse',mse)
X=np.array(out_data1[['GDP/fuel','GDP/fuel squared','GDP per capita (in USD)']])
s_error=mse*np.linalg.inv(X.T.dot(X))
print(s_error)