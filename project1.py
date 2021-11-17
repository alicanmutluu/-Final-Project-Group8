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



