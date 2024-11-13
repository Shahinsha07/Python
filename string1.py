# a="hello"
# print(a)
# n='hello'
# print(n)

# a=input("enter your name ")
# print(a)
# print(type(a))
# print(len(a))

# p="hello world"
# print(p[1])
# print(p[4],end=" ")
# print(p[-1])
# print(p[-2])
# print(p[5])
# print(p[3])

# a='hello "my" world'
# print(a)


#SLICING
# a="helloworld"
# print(a[2:6]) #index 2 thott 5 vare
# print(a[4:8])
# print(a[1:])  #index thott baaki full
# print(a[:8])  #adhym thott index-1 (7) vare
# print(a[-5:-1])
# print(a[::-1]) #reverse a string
# print(a[::-2])
# print(a[:-6:-1])
# print(a[-1:-5:-1])
# print(a[5:1:-1]) 
# print(a[-1:-5:-1])

# a="hello"
# b="world"
# print(a+b)
# print(a,b)
# print(a+" "+b)
# print(a,"world")

# c="hello"
# print(c*4) #repeat times printed

# a="Hello World"
# print(a.upper())
# print(a.lower())
# print(a.swapcase()) #captial lower aavum and vice versa
# print(a.count("l")) #count of the given letter
# print(a.index("l")) #first l index
# print(a.find("l"))  #first l nte index find chyum
# print(a.rfind("l")) #right ill ninnn first
# print(a.rindex("l"))
# print(a.title()) #each word first letter will be capitalize
# a="hello"
# print(a.capitalize())  #only first word will be capitalize

# a="helloworld"
# print(a.islower()) #ouput true or false aavum
a="HELLO"
print(a.isupper())
# a="Hello World"
# print(a.istitle())
# a="helloworld"
# print(a.isalpha()) #alphabet mathram
# a="helloworld12"
# print(a.isalnum()) #alphabet and number include,not include special character and space
# x=a.replace("o","@")
# print(x)

# a="Python"
# print(a.casefold()) #same as lower, but lower only convert english letters

# a="123"
# a="½"
# a=""
# print(a.isdigit())  #number and squares,all powers
# print(a.isnumeric)  #numbers and fractions,square,all powers
# print(a.isdecimal()) #only 0-9 numbers

#write a program to count the number of lowercase and uppercase character in a string accepted from the user

# a=input("enter a name: ")
# upper=0
# lower=0
# for i in a:
#     if i.isupper():
#         upper+=1
        
#     else:
#         lower+=1
# print("count of lower letter ",lower,"count of capital letter",upper)

#count vowels
# a=input("enter a string: ")
# count=0
# a=a.lower()
# for i in a:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         count+=1
# print(count)

#count of alphabets
# a=input("enter a name: ")
# count=0
# for i in a:
#     if i.isalpha():
#         count+=1
# print(count)

# count of alphabets without using inbuilt function

# a=input("enter a number")
# len=0
# for i in a:
#     len+=1
# print(len)

# count of lower and upper without using inbuilt functions

# a=input("enter a name")
# up=0
# low=0
# for i in a:
#     if i>="A" and i<="Z":
#         up+=1
#     else:
#         low+=1
# print(up)
# print(low)

# count and sum of number

# a=input("enter a string")
# count=0
# sum=0
# for i in a:
#     if i.isdigit():
#         count+=1
#     if i.isdigit():
#         sum=sum+int(i)
# print(count)
# print(sum)


# a=input("enter a string")

# if len(a)<=2:
#     print(a)
    
# elif len(a)>=2 and a.endswith("ing"):
#     x=a[:-3]
    
#     print(x+"ly")
# elif len(a)>2:
#     print(a+"ing")

# restart replace resta$t

a="restart"
x=a[1:]
y=x.replace("r","$")
print("r"+y)
x=a.replace("r","$",)
print(x)

# a="hello world"
# print(a.startswith("h"))
# print(a.startswith("hello"))
# print(a.endswith("world"))
# print(a.endswith("d"))

# a="elloh world"
# print(a.startswith("h",4)) #4th index position start chyunth nokaan
# print(a.endswith("d",4)) #4thh index thott check chyum

# print(a.endswith("h",0,5)) #0 to 5-1 position vare

# a="hello world hai hello"
# x=a.split(",")
# print(x)
# y=" ".join(x)
# print(y)
# a="hello"
# x=a.zfill(20)
# print(x)
# a="hello"
# x=a.zfill(6)
# print(x)
# y=a.center(20)
# print(y)
# z=a.center(20,"$")
# print(z)
# w=a.rjust(15)
# print(w)
# w=a.rjust(12,"@")
# print(w)
# c=a.ljust(13,"@")
# print(c)

# a=" "
# print(a.isspace())

# a="hello world"
# x=a.removeprefix("hello")
# print(x)
# x=a.removesuffix("world")
# print(x)

# a="abc"
# print(a.isidentifier())
# a="1abc"
# print(a.isidentifier()) #false
# a="ABC"
# print(a.isidentifier()) #true
# a="$abc"
# print(a.isidentifier()) #false
# a="_abc"
# print(a.isidentifier()) #true
# print("/\\/\\/\\/\\")

# a="hello,hai,hello,hai,hello,hai"
# x=a.split(",",2) #hello oru item hai oru item baaki ellaam vere oru item
# print(x)
# x=a.rsplit(",",2) #rightill ninn
# print(x)

# # a="abc#$_\" igne \ kodthal error varum so \\ use cheyenm
# a="abc#$_12\\"
# print(a.isprintable()) #ture
# a="abc\tc"
# print(a.isprintable()) #false

# a="@@@@welcome@@@@"
# print(a.lstrip("@")) #leftlle remove aavum
# print(a.rstrip("@")) #rightlle remove aavum
# print(a.strip("@")) #2 side remove aavum

# a="welcome"
# print("\t",a)

# #string formats

# print("my name is {} my age is {} my hobby is {}".format("shazz",18,"playing"))
# print("my name is {0} my age is {1} my hobby is {2}".format("shazz",18,"playing"))

