from tkinter import *
x=Tk()
x.title("welcome to tkinter window")

x.geometry("500x500")


# l1=Label(x,text="name")
# l1.grid(row=1,column=1)
# a=StringVar()
# e1=Entry(x,justify="left",textvariable=a)
# e1.grid(row=1,column=2)


# def click():
#     a.set("shazz")

# b2=Button(x,text="submit",command=click)
# b2.grid(row=4,column=2,columnspan=2)


#pack


# l1=Label(x,text="name")
# l1.pack()
# l1=Label(x,text="name")
# l1.pack()
# l1=Label(x,text="name")
# l1.pack()
# l1=Label(x,text="name")
# l1.pack()
# l1=Label(x,text="name")
# l1.pack()
# l1=Label(x,text="name")
# l1.pack()
# l1=Label(x,text="name")
# l1.pack()
# l1=Label(x,text="name")
# l1.pack()

l1=Label(x,text="First Number")
l1.pack()
e1=Entry(x)
e1.pack()
l2=Label(x,text="Second Number")
l2.pack()
e2=Entry(x)
e2.pack()
l3=Label(x,text="Result")
l3.pack()
a=StringVar()
e3=Entry(x,textvariable=a)
e3.pack()

def click():
    
    a.set(int(e1.get())+int(e2.get()))

b2=Button(x,text="Find Sum",command=click)
b2.pack()
x.mainloop()