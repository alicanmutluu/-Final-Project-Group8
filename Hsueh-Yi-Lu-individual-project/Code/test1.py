import pandas as pd
import numpy as np

# read file from Github
data_health = pd.read_csv('https://raw.githubusercontent.com/alicanmutluu/Pollution-Solvers/main/2.12_Health_systems.csv',  sep = ',')
data_clean = pd.read_csv('https://raw.githubusercontent.com/alicanmutluu/Pollution-Solvers/main/cleanFuelAndTech.csv',  sep = ',')
data_pollution = pd.read_csv('https://raw.githubusercontent.com/alicanmutluu/Pollution-Solvers/main/death-rates-from-air-pollution.csv',  sep = ',')
data_ele = pd.read_csv('https://raw.githubusercontent.com/alicanmutluu/Pollution-Solvers/main/Electricity_Production_By_Source.csv',  sep = ',')
data_share = pd.read_csv('https://raw.githubusercontent.com/alicanmutluu/Pollution-Solvers/main/share-energy-consum-by-source.csv',  sep = ',')



def dfselection(s, df, v):
    ans = df.copy()
    for n, i in df.iterrows():
        if i[v] not in s:
            ans = ans.drop(n, axis=0)

    return ans


set1 = {i for i in data_health['World_Bank_Name']}
set2 = {i for i in data_clean['Location']}
set3 = {i for i in data_pollution['Entity']}
set4 = {i for i in data_ele['Entity']}
set5 = {i for i in data_share['Entity']}

setf = set1.intersection(set2)
setf = setf.intersection(set3)
setf = setf.intersection(set4)
setf = setf.intersection(set5)
print(setf)
print(len(setf))

data_health_selectbylocation = dfselection(setf, data_health, 'World_Bank_Name')
data_clean_selectbylocation = dfselection(setf, data_clean, 'Location')
data_pollution_selectbylocation = dfselection(setf, data_pollution, 'Entity')
data_ele_selectbylocation = dfselection(setf, data_ele, 'Entity')
data_share_selectbylocation = dfselection(setf, data_share, 'Entity')

  
data_health=pd.read_csv('2.12_Health_systems.csv')
data_clean=pd.read_csv('cleanFuelAndTech.csv')
data_pollution=pd.read_csv('death-rates-from-air-pollution.csv')
data_ele=pd.read_csv('Electricity_Production_By_Source.csv')
data_share=pd.read_csv('share-energy-consum-by-source.csv')

set1={i for i in data_health['World_Bank_Name']}
set2={i for i in data_clean['Location'] }
set3={i for i in data_pollution['Entity'] }
set4={i for i in data_ele['Entity'] }
set5={i for i in data_share['Entity'] }

setf=set1.intersection(set2)
setf=setf.intersection(set3)
setf=setf.intersection(set4)
setf=setf.intersection(set5)
print(setf)
print(len(setf))

data_health_selectbylocation=dfselection(setf,data_health,'World_Bank_Name')
data_clean_selectbylocation=dfselection(setf,data_clean,'Location')
data_pollution_selectbylocation=dfselection(setf,data_pollution,'Entity')
data_ele_selectbylocation=dfselection(setf,data_ele,'Entity')
data_share_selectbylocation=dfselection(setf,data_share,'Entity')


data_health_selectbylocation = data_health_selectbylocation.rename(columns={"World_Bank_Name": "Country"})
data_clean_selectbylocation = data_clean_selectbylocation.rename(columns={"Location": "Country"})
data_pollution_selectbylocation = data_pollution_selectbylocation.rename(columns={"Entity": "Country"})
data_ele_selectbylocation = data_ele_selectbylocation.rename(columns={"Entity": "Country"})
data_share_selectbylocation = data_share_selectbylocation.rename(columns={"Entity": "Country"})

data_clean_selectbylocation = data_clean_selectbylocation.rename(columns={"Period": "Year"})

# Drop 'Province_State', which column is empty. Drop the NA value
data_health_selectbylocation = data_health_selectbylocation.drop(columns=['Province_State'])
data_health_selectbylocation = data_health_selectbylocation.dropna()
# [56 rows x 13 columns] --- health

# Drop NA
data_clean_selectbylocation = data_clean_selectbylocation.dropna()
# [2801 rows x 4 columns] --- clean

# Drop NA
data_pollution_selectbylocation = data_pollution_selectbylocation.dropna()
# [4144 rows x 7 columns] --- pollution

# Drop NA
data_ele_selectbylocation = data_ele_selectbylocation.dropna()
# [3347 rows x 11 columns] --- ele

# Drop NA and 'Code'
data_share_selectbylocation = data_share_selectbylocation.drop(columns=['Code'])
data_share_selectbylocation = data_share_selectbylocation.dropna()
# [3339 rows x 10 columns] --- share




# Select data recent years
data_share_selectbylocation = data_share_selectbylocation[data_share_selectbylocation['Year'] >= 2010]


# Select data recent years
data_clean_selectbylocation = data_clean_selectbylocation[data_clean_selectbylocation['Year']>=2010]
# [1331 rows x 4 columns] --- clean 2010-2021

# Select data recent years
data_pollution_selectbylocation = data_pollution_selectbylocation[data_pollution_selectbylocation['Year']>=2010]
# [1184 rows x 7 columns] --- pollution 2010-2021

# Select data recent years
data_ele_selectbylocation = data_ele_selectbylocation[data_ele_selectbylocation['Year']>=2010]
# [1537 rows x 11 columns] --- ele 2010-2021

# Select data recent years
data_share_selectbylocation = data_share_selectbylocation[data_share_selectbylocation['Year']>=2010]
# [650 rows x 10 columns] --- share 2010-2021

# Select the 2016 data
Data1 = pd.merge(data_share_selectbylocation, data_ele_selectbylocation, on=["Country", "Year"])
Data2 = pd.merge(data_pollution_selectbylocation, data_clean_selectbylocation, on=["Country", "Year"])

Data3 = pd.merge(Data1, Data2, on=["Country", "Year"])

Data_2016 = Data3[Data3['Year'] == 2016]

Data3 = pd.merge(Data1, Data2, on = ["Country", "Year"])

Data_2016 = Data3[Data3['Year']==2016]
# [65 rows x 26 columns]

# Data1_2016 = Data1[Data1['Year']==2016]  --- [65 rows x 19 columns]
# data_share_selectbylocation['Country'].nunique() ----  only 65 countries inside  :(
# data_ele_selectbylocation['Country'].nunique() --- only 65 countries inside too


Data_2016_final = pd.merge(Data_2016, data_health_selectbylocation, on=["Country"])

Data_2016_final = pd.merge(Data_2016, data_health_selectbylocation, on = ["Country"])

# [35 rows x 38 columns] ---- 35 rows left  :(

###########  Not using new dataset  ############
# Data1_1 = pd.merge(data_pollution_selectbylocation, data_ele_selectbylocation, on=["Country", "Year"])
# Data2_1 = pd.merge(Data1_1, data_clean_selectbylocation, on=["Country", "Year"])
# Data_2016_1 = Data2_1[Data2_1['Year']==2016]
#
# Data_2016_final_1 = pd.merge(Data_2016_1, data_health_selectbylocation, on = ["Country"])
# [35 rows x 30 columns]
#  ------------------------- same results ---------------------------------

# data_clean['Location'].nunique()     ----------------   191
# data_health['World_Bank_Name'].nunique()  ------------ 210
# data_pollution['Entity'].nunique()   ---------------- 231
# data_ele['Entity'].nunique()  -----------------------  235
# data_share['Entity'].nunique() ---------------------- 83


# ------------------------------ Retry 1 ----------------------------------------

def drop(D):
    a = D.dropna()
    return a

data_health= data_health.drop(columns=['Province_State'])   # 'Province_State' is empty

data_clean = drop(data_clean)
data_health = drop(data_health)
data_pollution = drop(data_pollution)
data_ele = drop(data_ele)
data_share = drop(data_share)

data_health = data_health.rename(columns={"World_Bank_Name": "Country"})
data_clean = data_clean.rename(columns={"Location": "Country"})
data_pollution = data_pollution.rename(columns={"Entity": "Country"})
data_ele = data_ele.rename(columns={"Entity": "Country"})
data_share = data_share.rename(columns={"Entity": "Country"})

data_clean = data_clean.rename(columns={"Period": "Year"})

def year2016(X):
    a = X[X['Year']==2016]
    return a

data_clean = year2016(data_clean)
data_pollution = year2016(data_pollution)
data_ele = year2016(data_ele)
data_share = year2016(data_share)

# data_clean ---- [190 rows x 4 columns]
# data_pollution ---- [196 rows x 7 columns]
# data_ele ---- [210 rows x 11 columns]
# data_share ---- [80 rows x 11 columns]

# Don't merge data_share this time
data1 = pd.merge(data_pollution, data_ele, on=["Country", "Year"])
data2 = pd.merge(data_clean, data1, on=["Country", "Year"])
data_final = pd.merge(data2, data_health, on=["Country"])

#