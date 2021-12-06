
from tkinter import *
from estimator import estimator

from PIL import Image
import os
from pathlib import Path

est=estimator( )
cwd=os.getcwd()

pngs=Path(cwd).glob('*.png')
png_dict={os.path.basename(i):i for i in pngs}


print(png_dict)
def est_button():
    t.delete('1.0',END)
    para=entry.get()
    ans=est.pred(para)
    t.insert('1.0',ans)
    return

def show_list():
    t.delete('1.0',END)
    list1=[i for i in png_dict.keys()]
    for x in range(len(list1)):
        a=x+1
        n=str(float(1+x))
        content = list1[x]
        t.insert(n,str(a)+': '+content+'\n')

    return   

def show_png(): 
    list1=[i for i in png_dict.keys()]
    ind = entry.get()

    name=list1[int(int(ind)-1)]    
    
    png = PhotoImage(file=name)  
    canvas.create_image(0,0, anchor=NW, image=png) 
    canvas.png=png
    return
    
root = Tk()

root.geometry('1200x700')
root.title('Pollution Estimator')
content1= Label(root, text = 'Input value:', font=(50), width = 10)
entry= Entry(root)
entry.grid(row=1,column=1)
content1.grid(row=1,column=0)



estimate_button = Button(root, text='estimate',comman=est_button)
estimate_button.grid(row=1,column=2)
pre_button=Button(root,text='Show Images List',command=show_list)
next_button=Button(root,text='Show Image',command=show_png)
pre_button.grid(row=1,column=3)
next_button.grid(row=1,column=4)




t = Text(root,height=30,width=50)
t.config(font=30)
t.grid(row=0,column=0,columnspan=3)
canvas=Canvas(root,width=640,height=500)
canvas.grid(row=0,column=3,columnspan=2)
t.insert(str(1.0),est.info())
root.mainloop()