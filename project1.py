import pandas as pd
import numpy as np


def dfselection(s,df,v):
   
    ans=df.copy()
    for n,i in df.iterrows():
        if i[v]  not in s:
            ans=ans.drop(n,axis=0)
            
            
    return ans


  
data_health=pd.read_csv('2.12_Health_systems.csv')
data_clean=pd.read_csv('cleanFuelAndTech.csv')
data_pollution=pd.read_csv('death-rates-from-air-pollution.csv')
data_ele=pd.read_csv('Electricity_Production_By_Source.csv')

set1={i for i in data_health['World_Bank_Name']}
set2={i for i in data_clean['Location'] }
set3={i for i in data_pollution['Entity'] }
set4={i for i in data_ele['Entity'] }

setf=set1.intersection(set2)
setf=setf.intersection(set3)
setf=setf.intersection(set4)
print(setf)
print(len(setf))

data_health_selectbylocation=dfselection(setf,data_health,'World_Bank_Name')
data_clean_selectbylocation=dfselection(setf,data_clean,'Location')
data_pollution_selectbylocation=dfselection(setf,data_pollution,'Entity')
data_ele_selectbylocation=dfselection(setf,data_ele,'Entity')

# Drop 'Province_State', which column is empty. Drop the NA value
data_health_selectbylocation = data_health_selectbylocation.drop(columns=['Province_State'])
data_health_selectbylocation = data_health_selectbylocation.dropna()
# [56 rows x 13 columns]

# Drop NA
data_clean_selectbylocation = data_clean_selectbylocation.dropna()
# [2801 rows x 4 columns]

# Drop NA
data_pollution_selectbylocation = data_pollution_selectbylocation.dropna()
# [4144 rows x 7 columns]

# Drop NA
data_ele_selectbylocation = data_ele_selectbylocation.dropna()
# [3347 rows x 11 columns]

# Select data recent years
data_clean_selectbylocation = data_clean_selectbylocation[data_clean_selectbylocation['Period']>=2010]
# [1331 rows x 4 columns]

# Select data recent years
data_pollution_selectbylocation = data_pollution_selectbylocation[data_pollution_selectbylocation['Year']>=2010]
# [1184 rows x 7 columns]

# Select data recent years
data_ele_selectbylocation = data_ele_selectbylocation[data_ele_selectbylocation['Year']>=2010]
# [1537 rows x 11 columns]