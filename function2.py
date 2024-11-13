# def hello(name,age):
#     print(name,age)
# hello("ammu",10)
# hello("anu",20)

# def hello(name,age=30):
#     print(name,age)
# hello("ammu")
# hello("anu",20)

#local variable and global variable

#local

def hello():
    a=100
    print(a)
    print("success")
hello()
# print(a)

#global

# b=200
# def hello():
#     # global b
#     b=100+b
#     # print(a)
#     # print("success")
#     print(b)
# hello()

'''Arbitriy arguements(*args) if you dont know how many arguments that will be passed into your fn add * before the parameter name in the fn defintio
that the fn be recieve a tuble of arguements'''

'''Arbitriy keyword arguments (**kwargs) if you dont know how many key word arguments that will be passed into your fn add two **before the parameter name in the the fn defintion that the fn be recieve a dictionary of arguments'''

#*args
# def display(*a):
#     print(a)
# display(10,20,30)

def display(a,b,c):
    print(a,b,c)
display(a=10,b=20,c=30)

# **args
def display(**a):
    print(a)

display(a=10,b=10,c=20)

# def display(n):
#     if n==0:
#         return n
#     else:
#         return n+display(n-1)
#         #5+display(4)
#         #5+4+display(3)
#         #5+4+3+display(2)
#         #5+4+3+2+display(1)
#         #5+4+3+2+1=15

# print(display(5))

'''factorial of number'''
# def factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# sum of digit

def sum(n):
    if n==0:
        return n
    else:
        return n%10+sum(n//10)
print(sum(123))

#write a recursive funtion to reverse a given string

# def reverse(a):
#     if len(a)==0:
#         return a
#     else:
#         return a[-1]+reverse(a[:-1])
# a=input("enter a string")

# print(reverse(a))

#wrie a recursive function to calculate x raised to the power of n

# def display(n,x):
#     if x==1:
#         return n
#     else:
#         return n*display(n,x-1)
# print(display(2,3))

'''write a recursive function to to find a number fibonacci or not'''

# def fibonacci(num):
#     if num<=0:
#         return "fibonacci series"
#     elif num==1:
#         return 0
#     elif num==2:
#         return 1
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)
    
# for i in range(0,11):
#     print(fibonacci(i))
    
def is_fibonacci(num, a=0, b=1):
  
    if num == a or num == b:
        return True
   
    elif b > num:
        return False
   
    else:
        return is_fibonacci(num, b, a + b)


number = int(input("Enter a number: "))
if is_fibonacci(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is not a Fibonacci number.")    


