# class Person: classname first letter capital 

# class Classname:
#     pass
    
#objectname=Classname()

# class Bird:
#     eyes=2
#     beak=1
#     def fly(self,a):
#         self.a=a
#         print(a)
#     def walk(self):
#         print(self.a)
# parrot=Bird()
# print(parrot.eyes)
# print(parrot.beak)
# parrot.fly()
# parrot.eyes=1
# parrot.fly("parrot")
# print(parrot.eyes,"eyes")
# peacock=Bird()
# print(peacock.eyes)
# peacock.fly("peacock")
# peacock.walk()

# class Sum():
#     def num(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.c= self.a+self.b
#     def view(self):
#         print(self.c)
# obj=Sum()
# obj.num(10,20)
# obj.sum()
# obj.view()

# class Rectangle():
#     def size(self,length,breadth):
#         self.l=length
#         self.breadth=breadth
#     def area(self):
#         self.c=self.l*self.breadth
#     def perimeter(self):
#         self.d=2*(self.l+self.breadth)
#     def view(self):
#         print("the area is ",self.c)
#         print("the perimeter is ",self.d)
# obj=Rectangle()
# obj.size(10,20)
# obj.area()
# obj.perimeter()
# obj.view()

# class Book():
#     def title(self,a):
#         self.a=a
#     def author(self,b):
#         self.b=b
#     def view(self):
#         print("book name is: ",self.a,"\nauthor name:",self.b)
# obj=Book()
# obj.title("balyakalasaghi")
# obj.author("vaikom muhammed basheer")
# obj.view()

# class Bank():
#     def initial(self, initial_amount):
#         self.balance = initial_amount
#         print("Current balance:", self.balance)

#     def deposit(self, deposit):
#         self.balance += deposit
#         print("Deposited", deposit, "Current balance:", self.balance)

#     def withdrawal(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print("Withdraw", amount, "Current balance:", self.balance)
#         else:
#             print("Insufficient balance")

#     def current_balance(self):
#         print("Current balance:", self.balance)

# # Menu function

# bank = Bank()

# while True:
#     print("\nMENU")
#     print("1. Set initial amount")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Check current balance")
#     print("5. Exit")
    
#     choice = int(input("Choose an option: "))
    
#     if choice == 1:
#         amount = float(input("Enter initial amount: "))
#         bank.initial(amount)
#     elif choice == 2:
#         deposit_amount = float(input("Enter deposit amount: "))
#         bank.deposit(deposit_amount)
#     elif choice == 3:
#         withdrawal_amount = float(input("Enter withdrawal amount: "))
#         bank.withdrawal(withdrawal_amount)
#     elif choice == 4:
#         bank.current_balance()
#     elif choice == 5:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid option. Please choose a valid option.")




# class Student():
#     collage="abc"
#     def __init__(self,a):
#         print("welcome",a)
#     def study(self):
#         print("studying")
# ammu=Student("all")
# ammu.study()

#create a class person that initialize with a name and age include a method  display info that print name and age of the person

# class Person():
    
#     def __init__(self,name,age):
#         self.a=name
#         self.b=age
#     def info(self):
#         print("name:",self.a,"age:",self.b)
# person=Person("shazz",22)
# person.info()

# class Rectangle():

#     def __init__(self,len,breadth):
#         self.a=len
#         self.b=breadth
#     def area(self):
#         c=self.a*self.b
#         print("area is:",c)
# rec=Rectangle(10,20)
# rec.area()

# create a class student that initialize with a name and list of grades write methods to calculate the average grade and display the student details
# 85,90,70,75

# class Student:
#     def __init__(self,name,grades):
#         self.a=name
#         self.b=grades
#     def average(self):
#         self.avg=sum(self.b)/len(self.b)
#     def display(self):
#         print("name: ",self.a)
#         print("grades: ",self.b)
#         print("avg: ",self.avg)
# std=Student("shazz",[90,92,80,86])
# std.average()
# std.display()



#inheritance single

# class Father():
#     def phone(self):
#         print("phone is using")
#     def walk(self):
#         print("walking")
# class Son(Father):
#     def study(self):
#         print("studying")
# f=Son()
# f.phone()
# f.walk()
# f.study()

# #parent and child constructor use aakiyal child nte constructor work aavum parent mathrm annell parent work aavum
# class Father():
#     def __init__(self):
#         print("my name is aaaa")
# class Son(Father):
#     def __init__(self):
#         print("my name is aasdf")
# f=Son()

#super

# class Father():
#     def __init__(self,a):
#         print("father name",a)
#     def phone(self):
#         print("calling")
# class Son(Father):
#     def __init__(self,s,f):
#         print("son page",s)
#         super().__init__(f)
#         # Father.__init__(self)
#     def study(self):
#         print("studying")
    
# obj=Son("son","Anandhan")

#multilevel inheritance

class Grandfather():
    def phone(self):
        print("phone is using")
class Father(Grandfather):
    def walk(self):
        print("walking")
class Son(Father):
    def study(self):
        print("studying")

f=Son()
f.study()
f.phone()
f.walk()


# #multiple inheritence - multiple parents and only one child

# class Father():
#     def phone(self):
#         print("phone is using")
# class Mother():
#     def walk(self):
#         print("walking")
# class Son(Mother,Father):
#     def study(self):
#         print("studying")

# f=Son()
# f.phone()
# f.study()
# f.walk()

# 2 parrents contains same method only have working first inheritant method
class Father():
    def walk(self):
        print("phone is using")
class Mother():
    def walk(self):
        print("walking")
class Son(Mother,Father):
    def study(self):
        print("studying")

# f=Son()
# f.study()
# f.walk()

# #hierarchical inheritance opposite of multiple inheritance

# class Vehicle():
#     def accelerator(self):
#         print("vehicle")
# class Car(Vehicle):
#     def four():
#         print("four wheeler")
# class Bike(Vehicle):
#     def two():
#         print("two wheeler")

# f=Bike()
# f.two()
# f.accelerator
# ff=Car()
# ff.four()
# ff.accelerator()

#hybrid inheritance


# class Grandfather():
#     def walk(self):
#         print("walking")
# class Father(Grandfather):
#     def phone(self):
#         print("calling")
# class Mother(Grandfather):
#     def cook(self):
#         print("cooking")
# class Son(Father,Mother):
#     def study(self):
#         print("studying")
# class Daughter(Son):
#     def playing(self):
#         print("playing")

# d=Daughter()
# d.playing()
# d.cook()
# d.phone()
# d.walk()


# class School():
#     def fun1(self):
#         print("school")
# class Teacher1(School):
#     def fun2(self):
#         print("teacher1")
# class Teacher2(School):
#     def func3(self):
#         print("teacher2")
# class Student(Teacher1,Teacher2):
#     def func4(self):
#         print("student")

# obj=Student()
# obj.func4()
# obj.func3()
# obj.fun2()
# obj.fun1()
# print(Student.__mro__) #path


# class Grandfather():
#     def __init__(self,e):
#         print("hello",e)
# class Father(Grandfather):
#     def __init__(self,d,g):
#         print("hello",d)
#         super().__init__(g)
# class Son(Father,Grandfather):
#     def __init__(self,a,b,c):
#         print("hello",a)
#         super().__init__(b,c)
# obj=Son("son","father","grandfather")






