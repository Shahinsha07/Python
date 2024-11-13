# from tkinter import *
# x=Tk()
# x.title("tkinter")



# f1=Frame(x,highlightbackground='blue',highlightthickness=5)
# f1.grid(row=0,column=0,ipadx=100,ipady=100,padx=40,pady=40)

# f3=Frame(x,highlightbackground='red',highlightthickness=5)
# f3.grid(row=0,column=3,ipadx=100,ipady=100)


# l=Label(f1,text='name')
# l.grid(row=1,column=1)

# x.mainloop()

##############image in tkinter 


# from tkinter import *
# x=Tk()
# x.title("tkinter")
# x.geometry("400x400")
# f1=Frame(x,highlightbackground='blue',highlightthickness=5)
# f1.grid(row=0,column=0,ipadx=5,ipady=5,padx=5,pady=5)

# img=PhotoImage(file="./11151743.png")

# l=Label(f1,image=img)
# l.grid(row=1,column=1)

# x.mainloop()

### jpg format into png

# from PIL import Image
# img=Image.open("download.jpg")
# img.save("image.png","PNG")
# from tkinter import *
# x=Tk()
# x.title("tkinter")


# f1=Frame(x,highlightbackground='blue',highlightthickness=5)
# f1.grid(row=0,column=0,ipadx=100,ipady=100,padx=40,pady=40)

# img=PhotoImage(file="./image.png")
# l=Label(f1,image=img)
# l.grid(row=1,column=1)

# x.mainloop()


###canvas
# from tkinter import *
# x=Tk()
# x.title("tkinter")


# img=PhotoImage(file='./image.png')

# Canvas=Canvas(x,width=img.width(),height=img.height())
# Canvas.pack()
# Canvas.create_image(0,0,anchor=NW,image=img)
# Canvas.create_text(50,40,text="survey",font=("Helvetica",20),fill="red")
# x.mainloop()



####tkinter pack methods
###side
# from tkinter import *
# x=Tk()
# x.title("tkinter")
# l=Label(x,text='name',bg='red')
# l.pack(side=LEFT)
# l=Label(x,text='name',bg='red')
# l.pack(side=RIGHT)
# l=Label(x,text='name',bg='red')
# l.pack(side=TOP)
# l=Label(x,text='name',bg='red')
# l.pack(side=BOTTOM)
# x.mainloop()

####fill
# from tkinter import *
# x=Tk()
# x.title("tkinter")
# l=Label(x,text='name',bg='red')
# l.pack(fil=X,expand=True)
# l=Label(x,text='name',bg='green')
# l.pack(fil=Y,expand=True)
# l=Label(x,text='name',bg='yellow')
# l.pack(fil=BOTH,expand=True)
# x.mainloop()

#####padxpady
# from tkinter import *
# x=Tk()
# x.title("tkinter")
# l=Label(x,text='name',bg='red')
# l.pack(padx=20,pady=20)
# l=Label(x,text='name',bg='green')
# l.pack(ipadx=40,ipady=20)
# l=Label(x,text='name',bg='blue')
# l.pack(ipadx=20,ipady=20)
# l=Label(x,text='name',bg='yellow')
# l.pack(padx=40,pady=40)
# x.mainloop()
######all inside label
# from tkinter import *
# x=Tk()
# x.title("tkinter")
# l=Label(x,text="name",bg="red")
# l.pack(side=LEFT,expand=True,fill=BOTH)
# l=Label(x,text="name",bg="green")
# l.pack(side=RIGHT,expand=True,fill=BOTH)
# x.mainloop()




####menu
# from tkinter import *
# x=Tk()
# x.title("tkinter")

# menu=Menu(x)
# menu.add_cascade(label='file')
# x.configure(menu=menu)


# x.mainloop()

##dropdown for a option
# from tkinter import *
# x=Tk()
# x.title("tkinter")

# menu=Menu(x)
# new=Menu(menu)
# menu.add_cascade(label='file',menu=new)
# new.add_command(label='new file')
# new.add_command(label='new window')
# new.add_command(label='open file')
# new.add_command(label='open folder')
# x.configure(menu=menu)

# x.mainloop()

##seperator in a dropdown
# from tkinter import *
# x=Tk()
# x.title("tkinter")

# menu=Menu(x)
# new=Menu(menu, tearoff=0)
# menu.add_cascade(label='file',menu=new)
# new.add_command(label='new file')
# new.add_command(label='new window')
# new.add_separator()
# new.add_command(label='open file')
# new.add_command(label='open folder')
# x.configure(menu=menu)
# x.mainloop()