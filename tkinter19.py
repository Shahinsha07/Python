# '''icon set'''

# from tkinter import *
# root=Tk()
# root.title("Icon Set")
# img=PhotoImage(file=r"11151743.png")
# root.iconphoto(True,img)


# root.mainloop()


# from tkinter import *

# root=Tk()
# root.geometry("400x400")
# # s=StringVar()
# l=Label(root,text="selcet gender")
# l.grid(row=0,column=0)
# s=IntVar()
# r1=Radiobutton(root,text="female",variable=s,value=0,width=20,anchor="w")
# r1.grid(row=1,column=0)
# r2=Radiobutton(root,text="male",variable=s,value=2,width=20,anchor="w")
# r2.grid(row=2,column=0)
# r3=Radiobutton(root,text="others",variable=s,value=3,width=20,anchor="w")
# r3.grid(row=3,column=0)


# root.mainloop()


from tkinter import *
from tkinter.scrolledtext import ScrolledText
root=Tk()

def show():
    # s.insert(1.0,"hai\n")
    # s.insert(2.0,"hello\n")
    # s.delete('1.0',END)
    # s.delete('1.0','1.end')
    # s.delete('2.0','2.end')

s=ScrolledText(root,width=10,height=10)
s.grid(row=6,column=2)


b1=Button(text="click",command=show)
b1.grid(row=3,column=3)


root.mainloop()