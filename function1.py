# def function_name(n):
#     print("success",n)
# function_name(10)

# def sum(a,b):
#     print(a+b)
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# sum(x,y)

# def sum(a,b):
#     return a+b
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# print(sum(x,y))

# def list(n):
#     print(n)
#     for i in n:
#         print(i)
# a=[10,20,30,40]
# list(a)


# def list(n):
#     print(n)
#     b=0
#     for i in n:
#         b+=i
#     print(b)
# a=[10,20,30]
# list(a)

'''palindrome checking'''
# def palindrome(n):
#     # print(n)
#     b=""
#     for i in n:
#         b=i+b
#     if a==b:
#         print("it is palindrome")
#     else:
#         print("not a palindrome")
# a=input("enter a string: ")
# palindrome(a)

'''calculator'''

# def addition(a,b):
    
#     print(a+b)
    
# def subtraction(a,b):
#     print(a-b)
# def multiplication(a,b):
    
#     print(a*b)
# def division(a,b):
    
#     print(a/b)    
# w=True
# while w:
#     ch=int(input("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.exit\n choose a number:"))
#     if ch<5:
#         x=int(input("enter a number"))
#         y=int(input("enter a number"))
#         if ch==1:
#             addition(x,y)
#         elif ch==2:
#             subtraction(x,y)
#         elif ch==3:
#             multiplication(x,y)
#         elif ch==4:
#             division(x,y)
#     else:
#         print("exit")
#         w=False
        

# PASS BY VALUE

def display(a):
    print(a,"inside")
    a=10
    print(a,"inside 1")
a=40
display(a)
print(a,"outside")

#pass by reference it will reflect outside

def display(a):
    print(a,"inside")
    a[0]=15
    print(a,"inside 1")
a=[10,20,30]
display(a)
print(a,"outside")