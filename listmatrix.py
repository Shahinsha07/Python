# #2x2 matrix
# a=[[1,2],[3,4]]
# for i in a:
#     for j in i:
#         print(j,end=" ")
#     print()


# #3x3 matrix
# a=[[1,2,3],[1,4,5],[5,6,7]]
# for i in a:
#     for j in i:
#         print(j,end=" ")
#     print()

#adding 2x2 matrix

# a=[[1,2],[3,4]]
# b=[[1,2],[3,4]]
# c=[[0,0],[0,0]]
# for i in range(len(a)):
#     for j in range(len(b)):
#         c[i][j]=a[i][j]+b[i][j]
# print(c)

# for i in c:
#     for j in i:
#         print(j,end=" ")
#     print()


# a=int(input("enter no of rows: "))
# b=int(input("enter no of colums: "))
# c=[]
# for i in range(a):
#     d=[]
#     for j in range(b):
#         x=int(input("enter the values"))
#         d.append(x)
#     c.append(d)
# print(c)

#matrix multiplication

# x=[[1,2,3],[4,5,6],[7,8,9]]
# y=[[1,2,3],[4,5,6],[7,8,9]]
# z=[[0,0,0],[0,0,0],[0,0,0]]

# for i in range(len(x)):
#     for j in range(len(y)):
#         for k in range(len(z)):
#             z[i][j]+=x[i][k]*y[k][j]
# print(z)

#transpose of a matrix

# x=[[1,2,3],[4,5,6],[7,8,9]]

# z=[[0,0,0],[0,0,0],[0,0,0]]


# for i in range(len(x)):        
#     for j in range(len(x[0])): 
#         z[j][i]=x[i][j]   

# print("original matrix")
# for i in x:
#     for j in i:
#         print(j,end=" ")
#     print()

# print("transpose matrix")
# for i in z:
#     for j in i:
#         print(j,end=" ")
#     print()