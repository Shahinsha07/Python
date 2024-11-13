# x={"name":"ammu","age":10,"place":"kochi"}
# print(x)
# print(len(x))
# print(type(x))
# x={"name":"ammu","age":10,"place":"kochi","name":"anu"}
# print(x)
# x={"name":"ammu","age":10,"place":"kochi","name":"anu","place":"kollam"}
# print(x)

x={"name":"ammu","age":10,"place":"kochi"}
# print(x["name"])
# print(x["age"])

# for i in x:
#     print(i)

# for i in x:
#     print(x[i])

# print(x.keys())
# print(x.values())
# print(x.items())

# for i in x.keys():
#     print(i)
# for i in x.values():
#     print(i)    
# for i in x.items():
#     print(i)
# for i,j in x.items():
#     print(i,j)

x["age"]=20
print(x)
del x["age"]
print(x)