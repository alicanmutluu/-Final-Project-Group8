
#use this to estimate, in the GUI.py, import this class to do estimate
# when import this estimator , first return the info on the GUI, click 'estimate on GUI' will call pred method to generate this string and show the string on the GUI
class estimator:
    def __init__(self,para_list):
        self.f_in=lambda x: para_list[0]+float(x[0])*para_list[1] 
        self.f_out=lambda x: para_list[2]+float(x[1])*para_list[3]
        
    def pred(self,x):
        if type(x) != str:
            return 'flase input, cannot interpret'
        xlist=x.split(',')
        if len(xlist) != 2:
            return 'flase input number of parameters'
        predin=self.f_in(xlist)
        predout=self.f_out(xlist)
        
        return 'estimated fatality caused by indoor pollution is '+str(predin)+'estimated fatality caused by indoor pollution is '+str(predout)
        
    def info(self):
        return 'enter the quantity of GDP and rate to estimate fataility per 100,000 people'
    
    

#example
est=estimator([1,2,1,2])
print(est.pred('5,2'))