import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from preprocessor import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from model_maker import model_maker
from model_maker import auto_plot, auto_plott
#implement f_test  by scipy to deal with model selection
'''
def f_test(ma,mb,paradif,n):
    
'''   
pre=preprocessing()


indoor=pre.indoor()

in_data=indoor[['Location','Year','First Tooltip','Indoor air pollution (deaths per 100,000)','GDP per capita (in USD)']]
in_data=in_data.dropna()
model_in1,report_in1=model_maker(in_data[['First Tooltip']],in_data['Indoor air pollution (deaths per 100,000)'],False)
print('indoor basic model:',report_in1)
auto_plot(in_data[['First Tooltip']],in_data['Indoor air pollution (deaths per 100,000)'],model_in1,'First Tooltip','basic model','Indoor air pollution (deaths per 100,000)')
in_data_t=in_data.copy()
in_data_t['Indoor air pollution (deaths per 100,000)']=in_data_t['Indoor air pollution (deaths per 100,000)'].map(lambda x: np.log(x))
model_in2,report_in2=model_maker(in_data[['First Tooltip']],in_data['Indoor air pollution (deaths per 100,000)'],True)
print('indoor transformed model:',report_in2)
auto_plott(in_data[['First Tooltip']],in_data['Indoor air pollution (deaths per 100,000)'],model_in2,'First Tooltip','log transfromed model','Indoor air pollution (deaths per 100,000)')

model_in3,report_in3=model_maker(in_data[['First Tooltip','GDP per capita (in USD)']],in_data['Indoor air pollution (deaths per 100,000)'],True)
print('indoor transformed model with 2 variable:',report_in3)


#model 4
in_data1=in_data[in_data['First Tooltip']<94].copy()
model_in4,report_in4=model_maker(in_data1[['First Tooltip','GDP per capita (in USD)']],in_data1['Indoor air pollution (deaths per 100,000)'],True)
auto_plott(in_data1[['First Tooltip','GDP per capita (in USD)']],in_data1['Indoor air pollution (deaths per 100,000)'],model_in4,'First Tooltip','log transfromed model 2 var','Indoor air pollution (deaths per 100,000)')
print('indoor transformed model with 2 variable:',report_in4)
auto_plott(in_data1[['First Tooltip','GDP per capita (in USD)']],in_data1['Indoor air pollution (deaths per 100,000)'],model_in4,'GDP per capita (in USD)','log model 2 var with GDP','Indoor air pollution (deaths per 100,000)')
#case 2016
indoor2016=pre.indoor2016()
in16_model_data=indoor2016.dropna()
model16,report16=model_maker(in16_model_data[['GDP per capita (in USD)']],in16_model_data['Health_exp_per_capita_USD_2016'],False)
print(report16)
auto_plot(in16_model_data[['GDP per capita (in USD)']],in16_model_data['Health_exp_per_capita_USD_2016'],model16,'GDP per capita (in USD)','relation GDP and Med expenditure','Health_exp_per_capita_USD_2016')

#out

out=pre.Merge_energy()
out_data=out[['Location', 'Year', 'Coal Consumption - EJ',
       'Oil Consumption - EJ','GDP per capita (in USD)','Population','Outdoor particulate matter (deaths per 100,000)']].copy()
out_data=out_data.dropna()
out_data['Oil Consumption - kwh']=out_data['Oil Consumption - EJ'].map(lambda x: x*277777777777.78)
out_data['Energy from oil per capita']=out_data['Oil Consumption - kwh']/out_data['Population']
out_data['Coal Consumption - kwh']=out_data['Coal Consumption - EJ'].map(lambda x: x*277777777777.78)
out_data['Energy from coal per capita']=out_data['Coal Consumption - kwh']/out_data['Population']
out_data['GDP/fuel']=out_data['GDP per capita (in USD)']/(out_data['Energy from coal per capita']+out_data['Energy from oil per capita'])
out_data['GDP/fuel squared']=out_data['GDP/fuel'].map(lambda x:x*x)
model_o,report_o=model_maker(out_data[['GDP/fuel','GDP per capita (in USD)','GDP/fuel squared']],out_data['Outdoor particulate matter (deaths per 100,000)'], True)
model_o1,report_o1=model_maker(out_data[['Energy from coal per capita','Energy from oil per capita']],out_data['Outdoor particulate matter (deaths per 100,000)'], False)
print(report_o1)
auto_plott(out_data[['GDP/fuel','GDP per capita (in USD)','GDP/fuel squared']],out_data['Outdoor particulate matter (deaths per 100,000)'], model_o, 'GDP/fuel', 'transformed outdoor model 2 variable', 'Outdoor particulate matter (deaths per 100,000)')
auto_plott(out_data[['GDP/fuel','GDP per capita (in USD)','GDP/fuel squared']],out_data['Outdoor particulate matter (deaths per 100,000)'], model_o, 'GDP per capita (in USD)', 'transformed outdoor model 2 variable with GDP', 'Outdoor particulate matter (deaths per 100,000)')
print('outdoor transformed model with 2 variable:',report_o)