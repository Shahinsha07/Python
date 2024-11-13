# from tkinter import messagebox
# from tkinter import *

# root=Tk()
# root.geometry("400x300")

# def display():
    # messagebox.showinfo("information","loginsuccess")
    # messagebox.showwarning("warning","it only consists of alphabets and space")
    # messagebox.showerror("error","login error")
    # messagebox.askokcancel("ask quaestion","are you sure")
    # messagebox.askyesno("ask quaestion","are you sure")
    # messagebox.askretrycancel("ask quaestion","are you sure")
    # x=messagebox.askquestion("ask question","are you sure")
    # if x=="yes":
    #     print("yes clicked")
    # else:
    #     print("....")
    # x=messagebox.askyesno("ask question","are you sure")
    # if x:
    #     messagebox.showinfo("information","success")
    # else:
    #     messagebox.showinfo("information","cancel")


# b1=Button(root,text="click",command=display)
# b1.pack()

# root.mainloop()


# from tkinter import *

# root=Tk()
# root.geometry("400x300")
# clicked=0

# l=Label(root,text="click "+str(clicked)+" times")
# l.pack()
# def click():
#     global clicked
#     clicked+=1
#     l.configure(text="clicked "+str(clicked)+" times")
#     l.pack

# b1=Button(root,text="click",command=click)
# b1.pack()

# root.mainloop()

# from tkinter import *
# root=Tk()
# root.geometry("400x300")


# s=IntVar()

# r1=Radiobutton(root,text="female",variable=s,value=1)
# r1.grid(row=1,column=1)
# r1=Radiobutton(root,text="male",variable=s,value=2)
# r1.grid(row=1,column=2)
# r1=Radiobutton(root,text="others",variable=s,value=3)
# r1.grid(row=1,column=3)

# ss=IntVar()

# r1=Radiobutton(root,text="Python",variable=ss,value=1)
# r1.grid(row=2,column=1)
# r1=Radiobutton(root,text="java",variable=ss,value=2)
# r1.grid(row=2,column=2)
# r1=Radiobutton(root,text=".net",variable=ss,value=3)
# r1.grid(row=2,column=3)

# root.mainloop()


from tkinter import *
root=Tk()
root.geometry("400x300")

r1=Checkbutton(root,text="female")
r1.grid(row=1,column=1)
r1=Checkbutton(root,text="male")
r1.grid(row=1,column=2)
r1=Checkbutton(root,text="others")
r1.grid(row=1,column=3)

ss=IntVar()

r1=Checkbutton(root,text="Python")
r1.grid(row=2,column=1)
r1=Checkbutton(root,text="java")
r1.grid(row=2,column=2)
r1=Checkbutton(root,text=".net")
r1.grid(row=2,column=3)

root.mainloop()