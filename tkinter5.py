from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox,Progressbar
from tkinter.scrolledtext import ScrolledText
x=Tk()
x.geometry("400x400")
cc=Combobox(x)
cc["values"]=["python","java",".net","data science"]
cc.current(2)
cc.grid(row=1,column=1)

s=Spinbox(x,from_=1,to=10).grid(row=2,column=1)
s1=ScrolledText(x,width=20,height=10).grid(row=3,column=1)

p=Progressbar(x,length=800)
p['value']=50
p.grid(row=4,column=1)

def fileclick():
    u=filedialog.askopenfilename()
bb=Button(x,text="click",bg="red",fg="yellow",bd=5,command=fileclick)
bb.grid(row=5,column=1)



x.mainloop()