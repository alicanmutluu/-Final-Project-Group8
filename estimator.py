import numpy as np
#use this to estimate, in the GUI.py, import this class to do estimate
# when import this estimator , first return the info on the GUI, click 'estimate on GUI' will call pred method to generate this string and show the string on the GUI
class estimator:
    def __init__(self):
        self.para_list=[5.065091369509082,-2.32373457*10**-2 ,-6.12877848*10**-5] 
        self.f_in=lambda x: self.para_list[0]+float(x[0])*self.para_list[1] + float(x[1])*self.para_list[2]
        self.mse=0.16816010123449202
        self.x_inv=np.array([[ 1.56116664*10**-7 ,-1.54922318*10**-9],[-1.54922318*10**-9 , 2.11861538*10**-11]],dtype=float)
    def pred(self,x):
        if type(x) != str:
            return 'false input, cannot interpret'
        xlist=x.split(',')
        if len(xlist) != 2:
            return 'false input number of parameters'
        pred=self.f_in(xlist)
        x0=np.array(xlist,dtype=float)
        error=self.mse*np.dot(np.dot(x0,self.x_inv),x0.T)
        bound=np.sqrt(error)*1.96
        bound_h=pred+bound
        bound_l=pred-bound
        predin=np.exp(pred)
        pred_h=np.exp(bound_h)
        pred_l=np.exp(bound_l)
        
        return 'estimated fatality caused by indoor pollution is '+str(predin)+'For 95% confidence interval, the estimated value is in the range of:'+str(pred_l)+', '+str(pred_h)
        
    def info(self):
        return 'enter the quantity of GDP per capita  and rate of clean fuel usage in population divide with \',\' to estimate fatality per 100,000 people, click show Image list to select image by index'
    
    

#example
