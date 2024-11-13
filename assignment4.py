from tkinter import *
from tkinter import messagebox
import re

x = Tk()

x.geometry("300x200")
l1 = Label(x, text="Name")
l1.grid(row=1, column=1)
l2 = Label(x, text="Phone Number")
l2.grid(row=2, column=1)
l3 = Label(x, text="Email")
l3.grid(row=3, column=1)
l4 = Label(x, text="Password")
l4.grid(row=4, column=1)
l5 = Label(x, text="Confirm Password")
l5.grid(row=5, column=1)

e1 = Entry(x)
e1.grid(row=1, column=2)
e2 = Entry(x)
e2.grid(row=2, column=2)
e3 = Entry(x)
e3.grid(row=3, column=2)
e4 = Entry(x, show='*')  # Password hidden
e4.grid(row=4, column=2)
e5 = Entry(x, show='*')  # Password hidden
e5.grid(row=5, column=2)

l6 = Label(x)
l6.grid(row=6, column=2)

def display():
    flag = True
    a = e1.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    e = e5.get()

    # Name validation
    if a == "":
        messagebox.showerror("Error", "Invalid Name")
        flag = False
    elif re.findall(r"[^A-Za-z\s]", a):
        messagebox.showerror("Error", "Invalid Name (only letters and spaces allowed)")
        flag = False

    # Phone number validation
    if not re.findall(r"\b\d{10}\b",b):
        messagebox.showerror("Error", "Invalid Phone Number (must be 10 digits)")
        flag = False

    # Email validation
    if " " in c or not re.findall(r"\b\w+@\w+\.\w+\b",c):
        messagebox.showerror("Error", "Invalid Email (must contain this format example@gmail.com, no spaces)")
        flag = False

    # Password validation
    if d == "":
        messagebox.showerror("Error", "Invalid Password (cannot be empty)")
        flag = False
    elif " " in d:
        messagebox.showerror("Error", "Invalid Password (cannot contain spaces)")
        flag = False

    # Confirm password validation
    if e != d:
        messagebox.showerror("Error", "Passwords do not match")
        flag = False

    # If all validations pass
    if flag:
        l6.configure(text="Successful")
    else:
        l6.configure(text="")

b = Button(x, text="Submit", command=display)
b.grid(row=7, column=2)

x.mainloop()
