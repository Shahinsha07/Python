# '''method overloding'''
# class student:
#     def display(self,a,b):
#         print(a+b)

#     def display(self,a,b,c):
#         print(a+b+c)

# s=student()
# s.display(10,20,30)

# s=student()
# s.display(10,20)


'''constructor overloding'''

# class student:
#     def _init_(self,a,b):
#         print(a+b)

#     def __init__(self,a,b,c):
#         print(a+b+c)

# s=student(10,20,30)

# s=student(10,20)


'''operator overloding'''

## magic method
'''add'''
# class student:
#     def __init__(self,a):
#         self.a=a

#     def __add__(self,other):
#         print(self.a)
#         print(other.a)
#         print(self.a+other.a)

# s=student(10)
# ss=student(2)
# s+ss

'''subtraction'''

# class student:
#     def _init_(self,a):
#         self.a=a

#     def _sub_(self,other):
#         print(self.a)
#         print(other.a)
#         print(self.a-other.a)

# s=student(10)
# ss=student(20)
# s-ss

'''multiplication'''

# class student:
#     def _init_(self,a):
#         self.a=a

#     def _mul_(self,other):
#         print(self.a)
#         print(other.a)
#         print(self.a*other.a)

# s=student(10)
# ss=student(20)
# s*ss

'''power'''

# class student:
#     def _init_(self,a):
#         self.a=a

#     def _pow_(self,other):
#         print(self.a)
#         print(other.a)
#         print(self.a**other.a)

# s=student(10)
# ss=student(20)
# s**ss

'''division'''

# class student:
#     def _init_(self,a):
#         self.a=a

#     def _truediv_(self,other):
#         print(self.a)
#         print(other.a)
#         print(self.a/other.a)

# s=student(100)
# ss=student(20)
# s/ss

'''floor division'''


# class student:
#     def _init_(self,a):
#         self.a=a

#     def _floordiv_(self,other):
#         print(self.a)
#         print(other.a)
#         print(self.a//other.a)

# s=student(100)
# ss=student(20)
# s//ss

'''reminder(modulo)'''


# class student:
#     def _init_(self,a):
#         self.a=a

#     def _mod_(self,other):
#         print(self.a)
#         print(other.a)
#         print(self.a%other.a)

# s=student(100)
# ss=student(20)
# s%ss
 

'''comparison operator'''                         

# less than=_lt_ (<)
# lass than or equal to=_le_ (<=)
# greater than=_gt_ (>)
# greater than or equal to=_ge_ (>=)
# equal to=_eq_ (==)
# not equal to=_ne_ (!=)

'''less than=_lt_ (<)'''
# class student:
#     def __init__(self,a):
#         self.a=a

#     def __lt__(self,other):
#         print(self.a)
#         print(other.a)
#         print(self.a<other.a)

# s=student(100)
# ss=student(20)
# s<ss

'''lass than or equal to=_le_ (<=)'''
# class student:
#     def _init_(self,a):
#         self.a=a

#     def _le_(self,other):
#         print(self.a)
#         print(other.a)
#         print(self.a<=other.a)

# s=student(100)
# ss=student(20)
# s<=ss


'''constructor overiding'''

# class Father:
#     def __init__(self):
#         print("father")

# class Son(Father):
#     def __init__(self):
#         print("son")
#         super().__init__()

# s=Son()

'''method overiding'''

# class Father:
#     def phone(self):
#         print("father can only call")

# class Son(Father):
#     def phone(self):
#         print("son can call,video call,msg,take img")
#         super().phone()

# s=Son()
# s.phone()  



'''private method'''

# class Father:
#     __name="abc"
#     def __init__(self):
#         print("working")
#         print(self.__name)
#         self.__phone()
#     def __phone(self):
#         print("father can only call")
# s=Father()    
        

# class Father:
#     _name = "abc"  # Protected member
#     def __init__(self):
#         print("working")
#     def _phone(self):  # Protected method
#         print("father can only call")

# class Son(Father):
#     def __init__(self):
#         print("son")
#         print(self._name)  # Accessing protected member
#         self._phone()  # Calling protected method

# s = Son()



'''some method fn'''

# class A:
#     def show(self):
#         print("a")
# class B(A):
#     def show1(self):
#         print("b")
# class C:
#     def show2(self):
#         print("c")
# class D(C):
#     def show3(self):
#         print("d")

# b1=B()
# d1=D()
# print(issubclass(B,A))
# print(issubclass(D,C))
# print(issubclass(D,A))
# print(isinstance(b1,B))
# print(isinstance(d1,B))
# print(isinstance(d1,C))



'''attribute method'''

# class Student:
#     name="ammu"
#     age=20
#     course="python"

# s=Student()
# print(s.name)
# print(hasattr(s,"name"))   ## checking attributes in class
# print(hasattr(s,"mark"))
# print(getattr(s,"name"))   ## get the value in that attribute
# setattr(s,"name","anu")        ## set the value in that attribute
# print(s.name)
# setattr(s,"mark",90)        ## set a new attribute and value
# print(s.mark)
# delattr(Student,"age")     ## delete the attribute and value
# print(s.age)



# docstring
# class A:
#     """this is a class of A"""
#     def show1(self):
#         print("a")
# class B(A):
#     """this is a class of B"""
#     def show2(self):
#         print("b")
# class C:
#     """this is a class of c"""
#     def show3(self):
#         print("c")
# class D(C):
   
#     def show4(self):
#         print("d")

# b1=B()
# d1=D()
# print(A.__doc__)
# print(B.__doc__)
# print(C.__doc__)


#create a class student with class variables school.
#a.create a paramatrized constructor with id,name,and age
#b.create instance of the class with id=1,name=sara,age=10 and id=2,nam='jose',age=20
#c.access value of attributes of an instances using built in function
#d.change the name attributes from jose to kris of defined instances
# e.check if class student has place attribute.if class student has no place place attribute
#  then create it using the built in method


# class Student:
#     school='abc'
#     def __init__(self,id,name,age):
#         self.id=id
#         self.name=name
#         self.age=age
        
# s=Student(1,'sara',10)
# s1=Student(2,'jose',20)
# print(getattr(s,'id'))
# print(getattr(s,"name"))
# print(getattr(s,"age"))
# print(getattr(s1,'id'))
# print(getattr(s1,"name"))
# print(getattr(s1,"age"))
# setattr(s1,'name','kris')
# print(s1.name)
# if hasattr(s1,'place'):
#     print(getattr(s1,'place'))
# else:
#     setattr(s,'place','kollam')
#     setattr(s1,'place','kochi')
#     print(s.place)
#     print(s1.place)


##abstraction
# from abc import ABC ,abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Polygon):
#     def area(self):
#         print("area")
# r=Rectangle()
# r.area()



# print("""hello  hai   
#       hello
#       helllo""")


##decorators
##instance method
# class Student:
#     class_variable=0
#     def __init__(self,name):
#         self.name=name
#     def modify(self,newname):
#         self.name=newname
#         self.__class__.class_variable+=1
#         #_class_ is a special attribute that allows an instance of a class to access its class
# s=Student("ammu")
# print(s.name)
# print(Student.class_variable)
# s.modify("anu")
# print(s.name)
# print(Student.class_variable,"pppppp")

##class method
# class Student:
#     class_variable=0
#     def __init__(self,name):
#         self.name=name
#     @classmethod 
#     def modify(cls):
#         cls.class_variable+=1
          
# s=Student("ammu")
# print(s.name)
# print(Student.class_variable)
# # s.modify("anu")
# # print(s.name)
# s=Student.modify("anu")
# print(s.name)
# print(Student.class_variable,"pppppp")


##static method
# class Student:
#     class_variable=0
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def modify(a,b):
#         print(a+b)
# s=Student("ammu")
# print(s.name)
# print(Student.class_variable)
# Student.modify(10,20)
# print(s.name)
# print(Student.class_variable,"pppppp")


##destructor
# class Student:
#     def __init__(self):
#         print("constructor")
#     def __del__(self):
#         print("destructor","first")
#     def hello(self):
#         print("working")
# s=Student()
# del s

# #without del s
# class Student:
#     def __init__(self):
#         print("constructor")
#     def __del__(self):
#         print("destructor","first")
#     def hello(self):
#         print("working")
# s=Student()

try:
    a=int(input("enter a first number:"))
    b=int(input("enter a second number:"))
    print(a/b)
except:
    print("zero division error")
else:
    print("no error")
finally:
    print("always executes ")
print("stop")

#check exceptions
#index error
# try:
#     a=[1,2,3]
#     print(a[3])
# except IndexError:
#     print("index error")
# except NameError:
#     print("name error")
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("zero division error")

# except:
#     print("index error")
# else:
#     print("no error")
# finally:
#     print("always executes ")
# print("stop")

#name error
# try:
 
#     print(a)
# except IndexError:
#     print("index error")
# except NameError:
#     print("name error")
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("zero division error")

# except:
#     print("name error")
# else:
#     print("no error")
# finally:
#     print("always executes ")
# print("stop")

# #value error
# try:
    
#     a=int(input("enter the input:"))
# except IndexError:
#     print("index error")
# except NameError:
#     print("name error")
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("zero division error")

# except:
#     print("value error")
# else:
#     print("no error")
# finally:
#     print("always executes ")
# print("stop")

#key error
# try:
#     dic={'name':'ammu','age':10}
#     print(dic['place'])
# except KeyError:
#     print("key error first")
# except:
#     print("key error")

# #import error
# try:
#   from math import cube
# except ImportError:
#     print("import error first")
# except:
#     print("import error")

# #type error
# try:
#     print("10"+10)
# except TypeError:
#     print("type error first")
# except:
#     print("type error")


#keyword raise

# try:
#     age=int(input("enter your age"))
#     if age<18:
#         raise
#     else:
#         print("eligible for voting")
# except:
#     print("not eligible for voting")

# # ##
# try:
#     age=int(input("enter your age"))
#     if age<18:
#         raise TypeError
#     else:
#         print("eligible for voting")
# except TypeError:
#     print("not eligible for voting")
# except:
    # print("not eligible for voting")

# #we can create a exception name
# class AgeError(Exception):
#     pass
# try:
#     age=int(input("enter your age"))
#     if age<18:
#         raise AgeError
#     else:
#         print("eligible for voting")
# except AgeError:
#     print("not eligible for voting")
# except:
#     print("not eligible for voting")

#keyword assert
try:
    a=10
    b=50
    assert a>b,"a is lessthan b"
    print("a is greater than b")
except AssertionError as msg:
    print(msg)