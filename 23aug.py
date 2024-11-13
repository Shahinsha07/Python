#lambda 
 
# lambda arguments:expression
# x=lambda a,b:a+b
# print(x(10,20))

# x=lambda a,b,c:a+b+c
# print(x(10,20,30))

# # #filter
# p=[1,2,3,4,5,6,7,8,9,10]
# x=list(filter(lambda a:a%2==0,p))
# print(x)
# #map

# p=[1,2,3,4,5,6,7,8,9,10]
# x=list(map(lambda a:a**2,p))
# print(x)
# #reduce

# from functools import reduce

# p=[1,2,3,4,5,6,7,8,9,10]
# x=reduce(lambda a,b:a+b,p)  #a=1 b=2 ith add chythit athinte value variable a store chyum enit b increase chyth veendum add chyum 1+2=3 3+3=6 6+4=10...
# print(x)


# #find the positive numbers
# p=[1,-1,2,-2,3,-3]
# x=list(filter(lambda a:a>0,p))
# print(x)

# # #find the strings which are palindrome
# k=['mom','level','bat','cat']
# x=list(filter(lambda a:a[::-1]==a,k))
# print(x)

# # #convert each string to capital letters
# t=['hello','python','hai','java']
# x=list(map(lambda a:a.upper(),t))
# print(x)

# #calculate length of each string
# y=['apple','banana','pineapple','mango']
# x=list(map(lambda a:len(a),y))
# print(x)

# # #find the maximum value
# from functools import reduce
# e=[3,5,6,8,1]
# x=reduce(lambda a,b:a if a>b else b,e)
# x=reduce(lambda a,b:max(a,b),e)
# print(x)

# # #concatenate them into a single string
# from functools import reduce
# h=['hello','python','programming','language']
# x=reduce(lambda a,b:a+b,h)
# print(x)

# #write a lambda fun to add 10 to a given number
# x=lambda a:a+10
# print(x(20))

# #using def with filter
# def display (n):
#     return n>0
# p=[1,-1,2,-2,3,-3]
# x=list(filter(display,p))
# print(x)

# #using def with map

# def display(n):
#     return n.upper()
# t=['hello','python','hai','java']
# x=list(map(display,t))
# print(x)

#methods common
#sorted 
# l=[10,12,81,54,60]
# print(sorted(l))

# l=[10,12,81,54,60]
# print(sorted(l,reverse=True))

# l=['abc','python','apple','bat','java']
# print(sorted(l,key=len))

# #reversed
# l=[10,12,81,54,60]
# print(list(reversed(l)))

# for i in reversed(range(5)):
#     print(i)

# #reverse a string using reversed
# l="hello"
# x=''.join(reversed(l))
# print(x)


# #enumerate method
# l=[1,2,3,4,5,6]
# for i,j in enumerate(l):
#     print(i,j)

# for i,j in enumerate (l,start=1):
#     print(i,j)

