# open(filename,mode)

# f=open("abc.txt")
# print(f.read())
# print(f.readline()) #read first line 
# print(f.readlines()) #readline and each line will in list items
# f.close()

# f=open("abc.txt","r")
# print(f.read())           
# f.close()

# f=open("abcd.txt","r")  #already aavatha file read chythaal error varum
# print(f.read())
# f.close()

# f=open("abc.txt","w")  #already ulla value chnge aayit new value add aavum
# f.write("hello")
# f.close()

f=open("abcde.txt","w")  #already illaatha file write chythaal new file create aayit athilk write chyum
f.write("hello")        
f.close()

#already ulla value athinte koode new oru value koodi append chyth vekkum
# f=open("abc.txt","a")
# f.write(("hai"))
# f.close()


#create file
# f=open("abd.txt","x")
# f.close()

#find maximum value

# f=open("abd.txt",'w')
# f.write("10\n5\n6")
# f.close()
# f1=open("abd.txt","r")
# p=f1.readlines()
# g=[int(i) for i in p]
# print(g)
# u=max(g)
# print(u)

#create a file with some text count and print the no fo words in the  file

# f=open("abe.txt","w")
# f.write("hai hello welcome")
# f.close()

# f1=open("abe.txt",'r')
# p=f1.read()
# print(p.split())
# print(len(p.split()))

'''seek'''

f=open("abc.txt","r")
a=f.seek(5)
print(a)
x=f.read(5)
print(x)
f.close()

'''tell'''

# f=open("abc.txt","r")
# a=f.tell()
# print(a)
# x=f.read(5)
# print(x)
# a=f.tell()
# print(a)
# f.close()

# f=open(r"C:\Users\shazz\OneDrive\Documents\hello.txt","r")
# x=f.read()
# print(x)
# f=open(r"C:\Users\shazz\OneDrive\Documents\hello.txt","a")
# x=f.write("10")
# f.close()


# import os
# # # os.remove("hai.txt") #empty file remove aakan
# os.rmdir(("hello")) #empty folder remove aakan

#non empty file & folder  remove aavan

# import os
# import shutil

# # os.remove("hai.txt") # file remove aakan
# os.rmdir(("hello")) # folder remove aakan

#open file using with function

# with open("abc.txt","w") as file:
#     x=file.write("worked")
#     print(x)
# file.close()

# input=[2,7,11,15]
# target=9
# output=[0,1]
# i=0
# j=len(input)-1
# while i<j:
    

