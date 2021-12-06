import pandas as pd
import numpy as np



class preprocessing():
    def __init__(self):
        self.data_health =pd.read_csv('https://raw.githubusercontent.com/alicanmutluu/Pollution-Solvers/main/2.12_Health_systems.csv',  sep = ',')
        self.data_clean = pd.read_csv('https://raw.githubusercontent.com/alicanmutluu/Pollution-Solvers/main/cleanFuelAndTech.csv',  sep = ',')
        self.data_pollution = pd.read_csv('https://raw.githubusercontent.com/alicanmutluu/Pollution-Solvers/main/death-rates-from-air-pollution.csv',  sep = ',')
        self.data_GDP=pd.read_csv('Country wise GDP from 1994 to 2017.csv')
        self.data_share = pd.read_csv('https://raw.githubusercontent.com/alicanmutluu/Pollution-Solvers/main/share-energy-consum-by-source.csv',  sep = ',')
        self.set1 = {i for i in self.data_health['World_Bank_Name']}
        self.set2 = {i for i in self.data_clean['Location']}
        self.set3 = {i for i in self.data_pollution['Entity']}
        self.set4 = {i for i in self.data_GDP['Country']}
        self.set5 = {i for i in self.data_share['Entity']}
        self.setf = self.set1.intersection(self.set2)
        self.setf = self.setf.intersection(self.set3)
        self.setf = self.setf.intersection(self.set4)
        self.setf = self.setf.intersection(self.set5)     
        self.setf2= self.set1.intersection(self.set2)
        self.setf2= self.setf2.intersection(self.set3)
        self.setf2= self.setf2.intersection(self.set4)

    def dfselection(self,s, df, v):
        ans = df.copy()
        for n, i in df.iterrows():
            if i[v] not in s:
                ans = ans.drop(n, axis=0)

        return ans
    def indoor2016(self):
        df1=self.dfselection(self.setf2,self.data_health,'World_Bank_Name')
        df2=self.dfselection(self.setf2,self.data_clean,'Location')
        df3=self.dfselection(self.setf2,self.data_pollution,'Entity')
        df4=self.dfselection(self.setf2,self.data_GDP,'Country')
        df2=df2[df2['Period']==2016]
        df3=df3[df3['Year']==2016]
        df4=df4[df4['Year']==2016]
        df1=df1.rename(columns={"World_Bank_Name": "Location"})
        df3=df3.rename(columns={'Entity':'Location'})
        df4=df4.rename(columns={'Country':'Location'})
        out=pd.merge(df1,df2,how='outer',on='Location')
        out=pd.merge(out,df3,how='outer',on="Location")
        out=pd.merge(out,df4,how='outer',on='Location')
        out=out.drop(columns='Province_State')
        
        return out
    
    def outdoor2016(self):
        df1=self.dfselection(self.setf,self.data_health,'World_Bank_Name')
        df3=self.dfselection(self.setf,self.data_pollution,'Entity')
        df5=self.dfselection(self.setf,self.data_share,'Entity')
        
        return
    def indoor(self):
        # merge df2 df3 df4 on location and year, on=outer do not drop na
        df2=self.dfselection(self.setf2,self.data_clean,'Location')
        df3=self.dfselection(self.setf2,self.data_pollution,'Entity')
        df4=self.dfselection(self.setf2,self.data_GDP,'Country')
        df2 = df2.rename(columns={"Period": "Year"})
        df3 = df3.rename(columns={'Entity': 'Location'})
        df4 = df4.rename(columns={'Country': 'Location'})
        out = pd.merge(df2, df3, how='outer', on=['Location','Year'])
        out = pd.merge(out, df4, how='outer', on=['Location','Year'])
        
        return

    def outdoor(self):
        # merge df3 df4 df5, on location and year, on=outer do not drop na
        df3=self.dfselection(self.setf,self.data_pollution,'Entity')
        df4=self.dfselection(self.setf,self.data_GDP,'Country')
        df5=self.dfselection(self.setf,self.data_share,'Entity')
        df3 = df3.rename(columns={'Entity': 'Location'})
        df4 = df4.rename(columns={'Country': 'Location'})
        df5 = df5.rename(columns={'Entity': 'Location'})
        out = pd.merge(df3, df4, how='outer', on=['Location', 'Year'])
        out = pd.merge(out, df5, how='outer', on=['Location', 'Year'])
        return
#prepare data for indoor2016 
pre=preprocessing()
indoor2016=pre.indoor2016()
print(indoor2016.columns)
print(indoor2016.shape)        
#prepare data for indoor
pre=preprocessing()
indoor=pre.indoor()
print(indoor.columns)
print(indoor.shape) 
#prepare data for outdoor2016
pre=preprocessing()
outdoor2016=pre.outdoor2016()
print(outdoor2016.columns)
print(outdoor2016.shape) 
#prepare data for outdoor
pre=preprocessing()
outdoor=pre.outdoor()
print(outdoor.columns)
print(outdoor.shape) 