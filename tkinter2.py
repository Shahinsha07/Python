from tkinter import *
x=Tk()
x.title("welcome to tkinter window")

x.geometry("500x500")
# l=Label(x,text="name",bg="red",fg="yellow",width=10,height=3,anchor="nw",font="arial 10 italic",cursor="plus") #bg or background use cheyaam
# l.grid(row=1,column=1)
# def click():
#     print("hello")
#     l.configure(text="changed text")


# b2=Button(x,text="submit",relief=RAISED,bd=10,command=click)
# b2.grid(row=2,column=1)
l=Label(x,text="name",font="arial 10 italic",cursor="plus") #bg or background use cheyaam
l.grid(row=1,column=1)
l1=Label(x,text="age",font="arial 10 italic",cursor="plus") 
l1.grid(row=2,column=1)
l2=Label(x,text="email",font="arial 10 italic",cursor="plus") 
l2.grid(row=3,column=1)

e1=Entry(x,justify="left")
e1.grid(row=1,column=2)
e2=Entry(x,justify="left")
e2.grid(row=2,column=2)
e3=Entry(x,justify="left")
e3.grid(row=3,column=2)
def click():
    # print("hello")
    # l.configure(text="changed text")
    # print(e1.get())
    # print(e2.get())
    # print(e3.get())
    # l.destroy()
    # l7=Label(x,text="My details",font="arial 10 bold")
    # l7.grid(row=5,column=2)
    # l4=Label(x,text=e1.get())
    # l4.grid(row=6,column=2)
    # l5=Label(x,text=e2.get())
    # l5.grid(row=7,column=2)
    # l6=Label(x,text=e3.get())
    # l6.grid(row=8,column=2)
    l7.configure(text="My Details",font="arial 20 bold")
    l4.configure(text=e1.get())
    l5.configure(text=e2.get())
    l6.configure(text=e3.get())



l7=Label(x)
l7.grid(row=5,column=2)
l4=Label(x)
l4.grid(row=6,column=2)
l5=Label()
l5.grid(row=7,column=2)
l6=Label(x)
l6.grid(row=8,column=2)

def delete():
    l7.destroy()
    l4.destroy()
    l5.destroy()
    l6.destroy()
b2=Button(x,text="submit",command=click)
b2.grid(row=4,column=2,columnspan=2)
b3=Button(x,text="Delete",command=delete)
b3.grid(row=4,column=3)

print("start")
x.mainloop()
print("stop")

