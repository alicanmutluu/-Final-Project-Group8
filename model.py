import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from preprocessor import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#implement f_test  by scipy to deal with model selection
'''
def f_test(ma,mb,paradif,n):
    
'''   
pre=preprocessing()


indoor=pre.indoor()
print(indoor.columns)
in_data=indoor[['Location','Year','First Tooltip','Indoor air pollution (deaths per 100,000)','GDP per capita (in USD)']]
in_data=in_data.dropna()
print(in_data)
fig1=plt.scatter(in_data['First Tooltip'],in_data['Indoor air pollution (deaths per 100,000)'])
plt.title('clean fuel usage rate and fatality per 100,000')
plt.xlabel('clean fuel usage rate')
plt.ylabel('fatality per 100,000')
plt.savefig('plot_of_clean_fuel_usage_rate_and_fatality_rate.png')
plt.show()


#indoor basic modes without transformation

in_model=LinearRegression()

in_model.fit(in_data[['First Tooltip']],in_data['Indoor air pollution (deaths per 100,000)'])
print('Basic model R squared',in_model.score(in_data[['First Tooltip']],in_data['Indoor air pollution (deaths per 100,000)']))
fig2=plt.scatter(in_data['First Tooltip'],in_model.predict(in_data[['First Tooltip']])-in_data['Indoor air pollution (deaths per 100,000)'])
plt.title('residual of basic model')
plt.xlabel('clean fuel usage rate')
plt.ylabel('residual')
plt.savefig('residual of basic model.png')
plt.show()
#the residual is change with clean fuel level, which means the model is not well
#basic model after transformation
in_data_t=in_data.copy()
in_data_t['Indoor air pollution (deaths per 100,000)']=in_data['Indoor air pollution (deaths per 100,000)'].map(lambda x: np.log(x))
in_model.fit(in_data_t[['First Tooltip']],in_data_t['Indoor air pollution (deaths per 100,000)'])
print('transformed model R squared',in_model.score(in_data_t[['First Tooltip']],in_data_t['Indoor air pollution (deaths per 100,000)']))
resid=in_model.predict(in_data_t[['First Tooltip']])-in_data_t['Indoor air pollution (deaths per 100,000)']
plt.scatter(in_data_t['First Tooltip'],resid)
plt.title('residual for log transformed model')
plt.xlabel('clean fuel usage rate')
plt.ylabel('residual')
plt.savefig('residual for log transformed model')
plt.show()


# the r-squared is 0.66, should have more explantory variable
# from case in 2016,medical exp could be in term of GDP, add GDP into the model

in_model.fit(in_data_t[['First Tooltip','GDP per capita (in USD)']],in_data_t['Indoor air pollution (deaths per 100,000)'])
print('transformed model with clean fuel and GDP R squared',
      in_model.score(in_data_t[['First Tooltip','GDP per capita (in USD)']],in_data_t['Indoor air pollution (deaths per 100,000)']))
resid=in_model.predict(in_data_t[['First Tooltip','GDP per capita (in USD)']])-in_data_t['Indoor air pollution (deaths per 100,000)']
plt.scatter(in_data_t['First Tooltip'],resid)
plt.title('residual for log transformed model with clean fuel usage rate and GDP')
plt.xlabel('clean fuel usage rate')
plt.ylabel('residual')
plt.savefig('residual for log transformed model with with clean fuel usage rate and GDP')
plt.show()


#indoor model2
in_model1=LinearRegression()
'''
print(in_data[in_data['GDP per capita (in USD)']>20000]['Indoor air pollution (deaths per 100,000)'].mean())
'''
# the percentage over 94 could have large residual 
in_data1=in_data[in_data['First Tooltip']<94].copy()




in_data1['Indoor air pollution (deaths per 100,000)']=in_data1['Indoor air pollution (deaths per 100,000)'].map(lambda x: np.log(x))




in_model1.fit(in_data1[['First Tooltip','GDP per capita (in USD)']],in_data1['Indoor air pollution (deaths per 100,000)'])
print(in_model1.score(in_data1[['First Tooltip','GDP per capita (in USD)']],in_data1['Indoor air pollution (deaths per 100,000)']))
print(in_model1.coef_,in_model1.intercept_)
pred=in_model1.predict(in_data1[['First Tooltip','GDP per capita (in USD)']])
resid=in_data1['Indoor air pollution (deaths per 100,000)']-pred
resid2=in_data1['Indoor air pollution (deaths per 100,000)'].map(lambda x: np.exp(x))-np.exp(pred)
x=[i for i in range(0,len(resid))]



plt.scatter(in_data1['First Tooltip'],resid)
plt.title('residual of log transformed model after dropping extreme instance')
plt.xlabel('clean fuel usage rate')
plt.ylabel('residual')
plt.savefig('residual of log transformed model after dropping extreme instance.png')
plt.show()

plt.scatter(in_data1['GDP per capita (in USD)'],resid)
plt.xlabel('GDP per capita (in USD)')
plt.ylabel('residual')
plt.title('residual-GDP of log transformed model after dropping extreme instance')
plt.savefig('residual-GDP of log transformed model after dropping extreme instance.png')
plt.show()
mse=mean_squared_error(in_data1['Indoor air pollution (deaths per 100,000)'], pred)

print('mes',mse)
X=np.array(in_data1[['First Tooltip','GDP per capita (in USD)']])
s_error=mse*np.linalg.inv(X.T.dot(X))
print(s_error)
         
# the residual do not change with the level, and R squared is 0.8137
#this model preforms better
#indoor model3
in_model2=LinearRegression()
in_data2=in_data1
in_data2['intereact']=in_data2['First Tooltip']*in_data2['GDP per capita (in USD)']
in_model2.fit(in_data2[['First Tooltip','GDP per capita (in USD)','intereact']],in_data2['Indoor air pollution (deaths per 100,000)'])
print(in_model2.score(in_data2[['First Tooltip','GDP per capita (in USD)','intereact']],in_data2['Indoor air pollution (deaths per 100,000)']))
print(in_model2.coef_,in_model1.intercept_)
#weak intereact for the two term

#check the extreme condition
in_data3=in_data[in_data['First Tooltip']>=94].copy()
print(in_data3['Indoor air pollution (deaths per 100,000)'].mean())
in_data3['Indoor air pollution (deaths per 100,000)']=in_data['Indoor air pollution (deaths per 100,000)'].map(lambda x:np.log(x))
in_data3['GDP per capita (in USD)']=in_data3['GDP per capita (in USD)'].map(lambda x: np.log(x))
print(in_data3.shape)


in_model3=LinearRegression()
in_model3.fit(in_data3[['GDP per capita (in USD)']],in_data3['Indoor air pollution (deaths per 100,000)'])
print(in_model3.score(in_data3[['GDP per capita (in USD)']],in_data3['Indoor air pollution (deaths per 100,000)']))
resid=in_model3.predict(in_data3[['GDP per capita (in USD)']])-in_data3['Indoor air pollution (deaths per 100,000)']
plt.scatter(in_data3['GDP per capita (in USD)'],resid)
plt.xlabel('log GDP per capita (in USD)')
plt.ylabel('residual')
plt.title('residual-log GDP of log transformed model for extreme instance')
plt.savefig('residual-log GDP of log transformed model for extreme instance.png')
plt.show()
