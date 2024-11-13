# x=[10,20,30,40,50]
# print(x)
# print(len(x))
# print(type(x))
# x=["python0","java","php"]
# print(x)
# x=[True,False]
# print(x)
# x=[10,20,'string','python',True,False]
# print(x)
# for i in x:
#     print(i)

# for i in range(len(x)):
#     print(x[i])

# print(x[0])
# print(x[-1])
# print(x[2:5])
# print(x[-6:-1])
# print(x[::-1])
# print(x[1:-3])

# a="hai"
# x=list(a)
# print(x)

# #append
# x=["python","java","php"]
# x.append("dotnet")
# print(x)

# #insert
# x.insert(2,"js")
# print(x)

# #extend
# y=[10,20,34]
# x.extend(y)
# print(x)

# a=int(input("enter a number between 1 to 10"))

# x=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

# y=[" "," ","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]

# if a<20:
#     print(x[a])
# elif a>=20 and a<=99:
#     z=a//10
#     c=a%10
#     if c==0:
#         print(y[z])
#     else:
#         print(y[z]+x[c])
# else:
#     print("invalid")

#take 10 numbers from user and add the numbers into a list

# x=[]
# for i in range(10):
#     a=int(input("enter number"))
#     x.append(a)
# print(x)

# x=["m","na","i","ke"]
# y=["y","me","s","lly"]
# z=[]
# for i in range(len(x)):
#     b=x[i]+y[i]
#     z.append(b)
# print(z)
    

# x=["hello","hai"]
# y=["dear","madam"]
# z=[] #["hellodear","hellomadam","haidear","haimadam"]
# for i in range(len(x)):
#     for j in range(len(y)):
#         b=x[i]+y[j]
#         z.append(b)
# print(z)

#index method

# z=["my","name","is","kelly"]
# print(z.index("name"))

#count method to count the values in list how much times

# z=["my","name","is","kelly","name"]

# print(z.count("name"))


#clear method

# z.clear()
# print(z)

# #reverse method to reverse the list
# z=["my","name","is","kelly"]
# z.reverse()
# print(z)

# #sort method list ordering alphabetic order priority  capital letter then sort small letter
# #sort chythit athine reverse chythal descending order kittum
# z=["My","name","is","kelly","adam"]
# z.sort()
# print(z)

# #pop method delete last value in the list
# z.pop()
# print(z)
# z.pop(1) #to delete specified index position
# print(z)
# x=z.pop(2) #to get deleted value
# print(z)
# print(x)


# #remove remove the specified item

# # z=["my","name","is","kelly"]
# # z.remove("my")
# # print(z)


# #copy method copy the list to another variable

# # z=["my","name","is","kelly"]
# # x=z.copy()
# # print(x)


# z=["my","name","is","kelly"]

# for i in z:
#     print(i)

# z=["my","name","is","kelly"]

# for i in range(len(z)):
#     print(z[i])

# z=["my","name","is","kelly"]

# i=0

# while i<len(z):
#     print(z[i])
#     i=i+1

#add 7000 after 6000

# list2=[10,20,[300,400,[5000,6000],500],30,40]


# list2[2][2].append(7000)
# print(list2)


# x=["h","i","j"]
# y=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
# #output=['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
# print(y[2][1][2])
# y[2][1][2].extend(x)
# print(y)

#remove all 20 in the list
# x=[5,20,15,20,25,50,20] 

# for i in x:
#     if i==20:
#         x.remove(i)
# print(x)

#to find the value 20 in the list and if it is present,replace it with 200.only update the first occurance of an item
# x=[5,10,15,20,25,50,20]

# c=x.index(20)       

# for i in x:
#     for j in range(i==20):
#         x[c]=200
# print(x)


# x=[5,10,15,20,25,50,20]

# y=x.index(20)
# x[y]=200
# print(x)


# a="have a nice day"
# # output=day nice a have
# x=a.split()
# print(x)
# x.reverse()
# y=" ".join(x)
# print(y)

# l=[1,2,3,5,4,2,1,3,5,4]
# y=[]
# l.sort()
# print(l)
# for i in range(len(l)):
#     if i%2==0:
#         b=l[i]
#         y.append(b)
#         i+=1
# print(y)

# l=[1,2,3,5,4,2,1,3,5,4]
# y=[] #output=[1,2,3,4,5]

# for i in l:
#     if i not in y:
#         y.append(i)
#         y.sort()
# print(y)


# l=[1,2,3,5,4,2,1,3,5,4]
# sum=0

# for i in range(len(l)):
#     sum+=l[i]
# print(sum)
#z=sum(l)
# print(z)


# l=[11,84,56,19,73,56]

# l.sort()

# print("minimum of",l[0])

# print("maximum of",l[-1])



# l=[11,84,56,19,73,56]

# z=min(l)
# y=max(l)
# print("minimum value",z,"maximum value",y)



# list comprehension

# syntax x=[expression for i in iterable if condition]
#string to list
# a="python"
# x=[i for i in a]
# print(x)

# x=[i*i for i in range(1,11)]
# print(x)

#only print even numbers
# s=[1,2,3,4,5,6,7,8,9,10]
# x=[i for i in s if i%2==0]
# print(x)

# s=[1,2,3,4,5,6,7,8,9,10]
# x=[i for i in s if i%2==0 if i%5==0]
# x=[i for i in s if i%2==0 and  i%5==0]
# print(x)


# s=[1,2,3,4,5,6,7,8,9,10]
# x=[i+1 if i>2 else i for i in s]
# print(x)

#check pallindrome and print this value
# l=["madam","level","random","python","mom"]
# x=[i for i in l if i==i[::-1]]
# print(x)

# p=["hai","hello","welcome"] #convert this string items to uppercase
# x=[i.upper() for i in p]
# print(x)
 

#print common numbers
# x=[1,2,3,4,5]
# y=[2,3,5,6,8]
# x=[i for i in y if i in x]
# print(x)

#convert positive number to true and -ve number to false
# f=[-1,-2,5,1,2]
# x=[i>0 for i in f]
# print(x)

#remove all vowels
# s="list comprehensive is simple"
# s.lower()
# x=[i for i in s if i not in 'aeiou']
# print(x)

# #print half of all elements
# x=[20,30,40,50]
# y=[i/2 for i in x ]
# print(y)


a=[[1,2],[3,4]]
for i in a:
    for j in i:
        print(j,end=" ")
    print()





