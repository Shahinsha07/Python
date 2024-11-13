# #print('hello')
# """print('hello')
# print('hello')"""

# # ctrl+/ for multiline command
# # print("welcome")

# # a=10
# # print(a)
# # type() function return type of variable
# # print(type(a))
# # b="hello"
# # print(b)
# # print(type(b))

# # s=input("enter your name") 
# # print(s)
# # print(type(s))
# # y=input("enter name")
# # print(s+y)
# # #to use int to taking value type is integer
# # x=int(input("enter a number"))
# # print(x)
# # print(type(x))
# # z=int(input("enter a second number"))
# # print(z)
# # print("the sum is", x+z)

# #use , or +" "+ to use space in between strings using concatenate

# # print(s,y)
# # print(y+""+s)

# #identifiers doesnot start with numbers only start with  lettersand using didgits underscore, do not use special characters, do not use keywords

# # a="hello"
# # A="hi"

# # print(a,A)

# # s="welcome"
# # s="all"
# # print(s,s)

# #data types

# #immutable data types doesnot chnage once created : int,float,boolean,string,tuple
# #mutable data type changable list, set, dictionary

# # a=10
# # b="shh"
# # c=True
# # d=10.25
# # t=(10,20,30)
# # print(t)
# # l=[10,20,30]
# # print(l)
# # s={10,20,30} 
# # print(s)
# # dic={"name":"shazz"}
# # print(dic)
# # print(type(a))
# # print(type(b))
# # print(type(c))
# # print(type(d))
# # print(type(t))
# # print(type(l))
# # print(type(s))
# # print(type(dic))

# # a=20
# # b=30
# # print(a+b)
# # print(a/b) #division
# # print(a-b)
# # print(a*b)
# # #floor division quotient will be the answer
# # c=23
# # d=5
# # print("answer",c//d)

# # print(c%d) #reminder is the answer

# # e=5
# # f=2
# # print(e**f)

# # a=235 #only print last letter 5
# # print(a%10)

# # x=a//10 #only print 3
# # print(x)
# # print(x%10)

# # a=453
# # print(a%10)

# # b=a//10
# # print(b%10)

# # a=10
# # b=10
# # print(a==b)
# # a=100
# # b=10
# # print(a!=b)
# # print(a<=b)
# # print(a>=b)
# # print(a>b)
# # print(a<b)
# #assignment
# # a=20
# # a+=5
# # print(a)
# # a-=5
# # print(a)
# # a*=5
# # print(a)
# # a=25
# # a/=20
# # print(a)
# # a=25
# # a%=20
# # print(a)
# # a=25
# # a//=20
# # print(a)
# # a=5
# # a**=2
# # print(a)

# #logical

# # a=10
# # b=10
# # print(a>=b and a<=b)
# # print(a>b or a>=b)
# # print(not(a==b))

# #membership

# # a="python"
# # print("y" in a)
# # print("e" in a)
# # print("e" not in a)

# #identify

# # a="hello"
# # b="hello"
# # print(a is b)
# # print(a  is  not b)
# # print(id(a))
# # print(id(b))

# #conditional operator

# #if-else

# # a=10
# # if a==10:
# #     print("a equal to 10")
# # else:
# #     print(" a is not equal to 10")

# # b=int(input("enter a number"))
# # if b==0:
# #     print("b is equal to zero")
# # elif b>0:
# #     print("b is positive")
# # elif b<0:
# #     print("b is negative")
# # else:
# #     print("invalid")
# #find largest number
# # a=10
# # b=40
# # c=30
# # if(a>b and a>c):
# #     print("a is greater")
# # elif (b>c and b>a):
# #     print("b is greater")
# # elif (c>a and c>b):
# #     print("c is greater")
# # else:
# #     print("invalid")
# # #take a input from user and find the number is even or odd
# # a=int(input("enter a number"))
# # if (a%2==0):
# #     print("the number is even")
# # else:
# #     print("the number is odd")

# #write a program to display "hello" if a number entered by user is divisible by 7 or not print bye

# # a=int(input("enter a number"))
# # if a%7==0:
# #     print("hello")
# # else:
# #     print("bye")

# #write a program to check whether the last digit of a number is divisible by 3 or not

# # a=124
# # b=a%10
# # print(b)
# # if b%3==0:
# #     print("divisible by 3")
# # else:
# #     print("not divisible by 3")
# # check the person is eligible or not for voting
# # a=int(input("enter your age"))
# # if a>=18:
# #     print("you are eligible")
# # else:
# #     print("you are not eligible")

# # a=int(input("enter a number"))

# # if a%3==0 and a%2==0:
# #     print(a,"the number is divisible by 3 and 2")

# # else:
# #     print("the number is not divisible by 2 and 3")

# # a=int(input("enter a number : "))
# # if a==1:
# #     print("sunday")
# # elif a==2:
# #     print("monday")
# # elif a==3:
# #     print("tuesday")
# # elif a==4:
# #     print("wednesday")
# # elif a==5:
# #     print("thursday")
# # elif a==6:
# #     print("friday")
# # elif a==7:
# #     print("saturday")
# # else:
# #     print("invalid")

# # a=input("enter a character")
# # b="aeiou"
# # if a in b:
# #     print("vowel")
# # else:
# #     print("not vowel")

# #check if a number is within a range of 1 to 10

# #a=int(input("enter a number"))
# #if a>=1 and a<=10:
# #    print("the number whithin range of 1 to 10")
# #else:
# #    print("the number is not whithin range of 1 to 10")



# #
# # a=5
# # if a==5:
# #     print("a equal to 5")
# # elif a<5:
# #     print("a is less than 5")
# # elif a>5:
# #     print("a greater than 5")
# # else:
# #     print("a is not 5, not lessthan 5 and positive number")

# # a=5
# # if a==5:
# #     print("a equal to 5")
# # if a<5:
# #     print("a is less than 5")
# # if a>5:
# #     print("a greater than 5")
# # else:
# #     print("a is not 5, not lessthan 5 and negative number")

# #nested if
# # a=10
# # if a>0:
# #     print("a is greater than zero")
# #     if a==10:
# #         print("a is equal  to 10")
# #     else:
# #         print("a greater than 10")
# # else:
# #     print("a less than zero")

# #check the given number is divisible by 2 and 5(using nested-if)

# # a=int(input("enter a number"))
# # if a%2==0:
    
# #     if a%5==0:
# #         print("the number is divisible by 5 and 2")
# #     else:
# #         print("divisible by 2 and not 5")
# # else:
# #     if a%5==0:
# #         print("the number is divisible by 5 but not 2")
# #     else:
# #         print("the number is not divisible by 2 and 5")

# # a=10
# # b=20
# # temp=a
# # a=b
# # b=temp
# # print("a=",a)
# # print("b=",b)

# # a=10
# # b=20
# # a=a+b
# # b=a-b
# # a=a-b
# # print(a,b)

# #a=1# i=0
# # while i<5:
# #     print(i)
# #     i=i+1

# # i=0
# # while i<5:
# #     i=i+1
# #     print(i)

# #write a program to print 1 to 10

# # i=1
# # while i<11:
# #     print(i)
# #     i=i+1

# #frist 10 even number
# # i=1
# # while i<=20:
# #     if i%2==0:
# #         print(i)
# #     i=i+1

# #first 10 odd number
# # i=1
# # while i<20:
# #     print(i)
# #     i=i+2

# #first 10 integer and their square

# # i=1
# # while i<=10:
# #     print(i,i*i)
# #     i=i+1

# #print the following series:10 20 30 40 50

# # i=10
# # while i<=50:
# #     print(i)
# #     i=i+10

# #print the following series:20 18 16 14 12 10 8 6 4 2 

# # i=20
# # while i>=2:
# #     print(i)
# #     i-=2

# #write a program to print sum of first 10 numbers

# # i=0
# # sum=0
# # while i<=10:
# #     sum+=i
# #     i+=1
# # print("the sum of first 10 number is",sum)

# #write a program to print sum of first 10 even numbers

# # i=2
# # sum=0
# # while i<=20:
# #     if i%2==0:
# #         sum+=i
# #     i+=1
# # print("the sum first 10 even number is",sum)

# #write a program to print multiplication table of a number entered from the user

# # a=int(input ("enter a number"))
# # i=1
# # while i<=10:
# #     print(a," x ",i,"=",a*i)
# #     i+=1

# #write a program to print all even numbers between two intervals

# # a=int(input("enter the starting interval"))
# # b=int(input("enter the end interval"))
# # print("starting interval is ",a,"ending", b )
# # while a<=b:
# #     if a%2==0:
# #         print(a)
# #     a+=1

# #write a program to check whether a number is prime or not (do not use while loop)

# # a=int(input("enter a number"))
# # i=2
# # prime=True
# # while i<a:
# #     if a%i==0:
# #         print("not a prime")
# #         prime=False
# #         break
# #     i+=1
# # if prime:
# #     print("prime number")

a=int(input("enter a number"))
prime=True
if a==2:
    print("prime")
else:
    for i in range(2,a):
        if a%i==0:
            prime=False
            break
    if prime>0:
        print("not prime")
    else:
        print("prime")

# a=int(input("enter a number"))

# prime=True

# if a<2:
#     prime=False

# else:
#     for i in range(2,a):



# #sum of the digit
# # a=int(input("enter a number"))
# # sum=0

# # while a!=0:
# #     sum=sum+a%10
# #     a=a//10
# # print("sum of the digit",sum)

# #count of a digit

# # a=int(input("enter a digit"))

# # count=0

# # while a!=0: #while a>0
# #     a//=10
# #     count+=1
# # print(count)

# #amstrong number

# a = int(input("Enter a number: "))
# b = a  # Keep the original number for comparison
# c = 0  # Initialize sum of powered digits
# count = 0  # Initialize the count of digits
# amstrong = 0  # Initialize Armstrong number check variable

# # Count the number of digits
# temp = a  # Use a temporary variable to keep original 'a' intact
# while temp != 0:
#     temp //= 10
#     count += 1

# # Calculate the sum of the digits raised to the power of the count of digits
# temp = a  # Reset temp to the original number
# while temp != 0:
#     d = temp % 10
#     c = d ** count
#     amstrong += c
#     temp //= 10

# # Check if the calculated Armstrong number matches the original number
# if amstrong == b:
#     print("It is an Armstrong number")
# else:
#     print("Not an Armstrong number")


# # reverse a number

# a=int(input("enter a number"))
# reverse=0

# while a>0:
#     x=a%10
#     reverse=reverse*10+x
#     a//=10
# print(reverse)


# #palindrome

# a=int(input("enter a number"))
# b=a
# reverse=0

# while a>0:
#     x=a%10
#     reverse=reverse*10+x
#     a//=10
# if reverse==b:
#     print("palindrome")
# else:
#     print("not palindrome")
    

# #spy number

# # a=int(input("enter a number:"))

# # sum=0 #for sum 
# # product=1 #for product

# # temp=a
# # while temp>0:
# #     b=temp%10
# #     sum+=b
# #     temp//=10
# # print("sum=",sum)

# # temp=a

# # while temp>0:
# #     c=temp%10
# #     product*=c
# #     temp//=10
# # print("product=",product)

# # if sum==product:
# #     print("it is a spy number")
# # else:
# #     print("it is not a prime number")

# #spy  number

# # a=int(input("enter a number"))
# # b=a
# # sum=0
# # product=1
# # d=0
# # temp=a
# # while temp>0:
# #     c=temp%10
# #     sum+=c
# #     temp//=10
# # print("sum ",sum)

# # temp=a
# # while temp>0:
# #     c=temp%10
# #     product*=c
# #     temp//=10
# # print("product ",product)

# # d=product+sum

# # if d==b:
# #     print("it is a spy number")
# # else:
# #     print("not a spy number")


# # i=0
# # while i<=5:
# #     if i==3:
# #         break
# #     i+=1
# #     print(i)
# # else:
# #     print("finished")#ith wrok avilla

# # print("welcome")

# # i=0
# # while i<5:
# #     i+=1
# #     if i==3:
# #         continue #ee condition true aavunth mathrm work aavilla baaki okke work avum
# #     print(i)
# # else:
# #     print("finished")


# #pass statement block onnum define cheyaan illaatha time pass statement use aakum

# # i=0
# # while i<5:
# #     pass


# #for loop

# # for i in "python":
# #     print(i)

# #for i in range(start,stop,step):

# # for i in range(5): #stop
# #     print(i)

# # for i in range(2,5): #start,stop
# #     print(i)

# # for i in range(1,10,2): #start stop step, step value start value increment chyum print chyumboll
# #     print(i)

# # 1 to 10 using for loop
# # for i in range(1,11):
# #     print(i)


# #odd number betwwen 1 and 10
# # for i in range(1,10,2):
# #     print(i)

# #10,20,...,100

# # for i in range(10,101,10):
# #     print(i)

# # 3,6,9,12,15,18,21,24,27,30

# # for i in range(3,31,3):
# #     print(i)


# # 105,98,97,91,....,7

# for i in range(105,6,-7):
#     print(i)

# #factorial
# a=int(input("enter a number"))
# factorial=1
# for i in range(1,a+1):
#     factorial*=i
# print(factorial)

#PATTERNS

# for i in range(5):
#     print("*")     #print avunth line by line aavum

# for i in range(5):
#     print("*",end=" ") #end use chythaal same line aavum athinullil space kodkumboll athin anusarich gap varum

# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print() #ee print use akunth next line povaan aanu

# # n=5
# # for i in range(n):
# #     for j in range(i+1):
# #         print("*",end="  ")
# #     print()

# # n=5
# # for i in range(n):
# #     for j in range(n-i):
# #         print("*",end="  ")
# #     print()


# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(n,end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(i+2,end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if i%2==0:
#             print(1,end=" ")
#         else:
#             print(2,end=" ")
        
#     print()

# n=5
# number=1

# for i in range(n):
#     for j in range(i+1):
#         print(number, end="  ")
#         number += 1
#     print()

# n=5

# for i in range(n):
#     p=5
#     for j in range(i+1):
#         print(p,end=" ")
#         p-=1
#     print()


# n=5

# for i in range(n):
#     p=5
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(p,end=" ")
#         p-=1
#     print()

# n=5
# for i in range(n):
#     p=1
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(p,end=" ")
#         p+=1
#     print()


#         * 
#       * *
#     * * *
#   * * * *
# * * * * *    
# n=5

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     # for k in range(i):
#     #     print("*",end=" ")
#     for j in range(i+1): #allell i+1 use aakam melle ulla loop koodi execute chytha mathi
#         print("*",end=" ")
#     print()


#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


      
#       +
#       +
# +  +  + + + +
#       +
#       +

# n=7
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2:
#             print("+",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# *         *
#    *   *
#      *
#    *   *
# *         *

n=5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end="  ")
        else:
            print(" ",end="  ")
    print()

# a="hello world"
# print(a)

# a=10
# b=20
# print("sum=",a+b)

# 0
# 22
# 444
# 6666
# 88888
# n=5
# p=0
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=2
#     print()


#  1 2 3 4 5 
#    1 2 3 4
#      1 2 3
#        1 2
#          1
# n=5

# for i in range(n):
#     p=1
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(p,end=" ")
#         p+=1
#     print()

#find the differnece of two numbers

# a=20
# b=10
# print("a-b=",a-b)

#cube of a number

# a=int(input("enter a number"))
# c=a**3
# print(c)

#swap to numbers

# a=10
# b=20
# print("a is",a,"b is",b)
# temp=a
# a=b
# b=temp
# print("a is",a,"b is",b)

#factorial

# a=int(input("enter a number"))
# factorial=1
# for i in range(1,a+1):
    
#     factorial*=i
# print(factorial)

#reverse of string

# s="hello"
# p=""
# for i in s:
#     p=i+p
# print(p)

# palindrome of string 

# a="malayalam"
# p=""
# for i in a:
#     p=i+p
# if p==a:
#     print("it is a pallindrome")
# else:
#     print("not a pallindrome")

#2 print kodthaalum same line varaan end=" " use aakiya mmathi
# print("hello",end=" ")
# print("hi")

# a=123
# reverse=0
# while a>0:
#     x=a%10
#     reverse=reverse*10+x
#     a//=10
# print(reverse)





