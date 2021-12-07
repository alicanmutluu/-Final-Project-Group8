import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from preprocessor import preprocessing
from sklearn.linear_model import LinearRegression
from numpy.lib.function_base import corrcoef
pre=preprocessing()
#case study,use instance for 2016, since it has more details
indoor2016=pre.indoor2016()
print(indoor2016)

in16_model_data=indoor2016[['Location','GDP per capita (in USD)','Health_exp_per_capita_USD_2016','Indoor air pollution (deaths per 100,000)','First Tooltip']]
in16_model_data=in16_model_data.dropna()
print(in16_model_data)


fig1=plt.scatter(in16_model_data['First Tooltip'],in16_model_data['Indoor air pollution (deaths per 100,000)'])
plt.show()

fig2=plt.scatter(in16_model_data['Health_exp_per_capita_USD_2016'],in16_model_data['Indoor air pollution (deaths per 100,000)'])
plt.show()

fig3=plt.scatter(in16_model_data['GDP per capita (in USD)'],in16_model_data['Indoor air pollution (deaths per 100,000)'])
plt.show()
fig4=plt.scatter(in16_model_data['GDP per capita (in USD)'],in16_model_data['Health_exp_per_capita_USD_2016'])
plt.show()
print('GDP and health exp relation',np,corrcoef(in16_model_data['GDP per capita (in USD)'],in16_model_data['Health_exp_per_capita_USD_2016']))
model=LinearRegression(fit_intercept=False)
model.fit(in16_model_data[['GDP per capita (in USD)']],in16_model_data['Health_exp_per_capita_USD_2016'])
print(model.score(in16_model_data[['GDP per capita (in USD)']],in16_model_data['Health_exp_per_capita_USD_2016']))
resid=model.predict(in16_model_data[['GDP per capita (in USD)']])-in16_model_data['Health_exp_per_capita_USD_2016']
plt.scatter(in16_model_data['GDP per capita (in USD)'],resid)
plt.show()

# the result suppose that medical exp and GDP generally linear related, that is Med exp = b*GDP, it concluded that, for the full model we can use GDP instead of Med exp
#since there is a linear model