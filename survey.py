from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox,Progressbar
x=Tk()
x.title("survey form")
x.geometry("400x400")

l=Label(x,text="Let us know how we can improve",font="san-serif 15 bold")
l.grid(row=1,columnspan=2)

#place row x column y
l2=Label(x,text="Name",font="san-serif 10 bold")
l2.grid(row=2,column=1)
e=Entry(x,justify="left")
e.grid(row=2,column=2)
l3=Label(x,text="E Mail",font="san-serif 10 bold")
l3.grid(row=3,column=1)
e1=Entry(x,justify="left")
e1.grid(row=3,column=2)
l4=Label(x,text="AGE",font="san-serif 10 bold")
l4.grid(row=4,column=1)
e2=Entry(x,justify="left")
e2.grid(row=4,column=2)
def fileclick():
    u=filedialog.askopenfilename()
bb=Button(x,text="Choose file",bg="skyblue",fg="black",bd=5,command=fileclick)
bb.grid(row=5,columnspan=2)
l5=Label(x,text="which option best describe your current role",font="san-serif 10 bold")
l5.grid(row=6,column=1)
cc=Combobox(x)
cc["values"]=["Student","Employee","UNEMPLOYEE"]
cc.current(0)
cc.grid(row=6,column=2)

# x.configure(bg="red")
x.mainloop()