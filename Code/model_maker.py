import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from preprocessor import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def model_maker(x,y,lg):
    if lg==True:
        
        yl=y.map(lambda x: np.log(x))
    else:
        yl=y.copy()
    
    ans=LinearRegression()
    x1,xt,y1,yt=train_test_split(x,yl,test_size=0.1)
    ans.fit(x1,y1)
    sc1=ans.score(x1,y1)
    sc2=ans.score(xt,yt)
    mse=mean_squared_error(y1,ans.predict(x1))
    result='R squared for train'+str(sc1)+'R squared for test'+str(sc2)+' mse: '+str(mse)
    
    
    return ans, result
   
def auto_plot(x,y,m,col,name,label): 
    pred=m.predict(x)
    plt.scatter(x[[col]],y-pred)
    plt.xlabel(col)
    plt.ylabel('residual')
    plt.title(name+' residual plot')
    plt.savefig(name+' residual plot')
    plt.show()
    
    fig = plt.figure(1)
    plt.scatter(x[[col]],pred)
    plt.scatter(x[[col]],y,c= 'g',marker='.')
    plt.title(name+' plot true and predict')
    plt.xlabel(col)
    plt.ylabel(label)    
    plt.savefig(name+' plot true and predict')
    plt.show()
    return

def auto_plott(x,y,m,col,name,label): 
    pred=m.predict(x)
    
    plt.scatter(x[[col]],y.map(lambda x: np.log(x))-pred)
    plt.xlabel(col)
    plt.ylabel('residual')
    plt.title(name+' residual plot')
    plt.savefig(name+' residual plot')
    plt.show()
    pred=np.exp(pred)
    fig = plt.figure(1)
    plt.scatter(x[[col]],pred)
    plt.scatter(x[[col]],y,c= 'g',marker='.')
    plt.title(name+' plot true and predict')
    plt.xlabel(col)
    plt.ylabel(label)    
    plt.savefig(name+' plot true and predict')
    plt.show()
    return   