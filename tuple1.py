# x=(1,2,34,5)
# print(x)
# print(type(x))
# print(len(x))

# x=(10,) #it is a single variable in tuple 
# print(type(x))

# y=("python","java",4,5,True,False,4,5)
# print(y)
# print(y[0])
# print(y[-1])
# print(y[-2])
# print(y[-1:-4])
# print(y[::-1]) #reverse

# print(y.index(4))
# print(y.count(4))

# x=(1,2,3,4,5)
# for i in range(len(x)):
#     print(x[i])

# i=0
# while i<len(x):
#     print(x[i])
#     i+=1

# x=("python","php","java","dotnet")
# b=list(x)
# print(b)
# b[0]="apple"
# print(b)
# b.remove("java")
# print(b)
# del b[1]
# print(b)
# x=tuple(b)
# print(x)

# # reverse the tuple 10 20 30 40 50
# x=(10,20,30,40,50)
# print(x[::-1])

# #access the value 20 from the tuple
# x=("orange",[10,20,30],(5,15,25))

# print(x[1][1])


# #create a tuple with single item 15

# x=(5,)
# print(x)



# #modify the tuple 22 is changed to 222
# x=[11,[22,33],45,55]
# b=list(x)

# b[1][0]=222
# print(tuple(b))


# #check if all items in the tuple are the same
# t=(45,45,45,45)
# print(t.count(t[0])==len(t))

# #count the no of occurances of item of 50 in tuple
# x=(50,10,50,70,50)

# print(x.count(50))


# tuple operators

# t1=(10,20,30,40)
# t2=(1,2,3,4,55)
# print(t1+t2)
# x=t1+t2
# print(x)
# t1+=t2
# print(t1)


# t1=(10,20,30,40)
# t2=(1,2,3,4,55)

# print(t1*3)

# print(10 in t1)
# print(100 not in t1)

#PACKING AND UNPACKING

# courses=("python","java","php","dotnet")
# (a,b,c,d)=courses
# print(a)
# print(b)
# print(c)
# print(d)

# courses=("python","java","php","dotnet")
# (*a,b,c)=courses
# print(a)
# print(b)
# print(c)


