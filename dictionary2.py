'''write a python to check if value 200 exit inthe following dictionnary'''
# d={"a":100,"b":200,"c":300}

# if 200 in d.values():
#     print("yes")
# else:
#     print("no")


# x={"name":"ammu","age":10,"place":"kochi"}
# print(x["name"])
# z=x.get("name")
# print(z)
# x.update({"name":"anu"})    ## change value
# print(x)
# x.update({"course":"python"})     ## add a item in dict
# print(x)

# z=x.pop("name")
# print(x)         ### delete the keyvalue


# z=x.popitem()
# print(x)         ### delete the last item in dict

# x.clear()
# print(x)     ### delete the full dict


''' print the value of key history form the below dict'''

# d={"class":{"student":{"name":"mike","marks":{"physics":70,"histroy":80}}}}
# print(d["class"]["student"])
# print(d["class"]["student"]["marks"]["histroy"])  


'''wap to rename a key city to location in the dictionary'''

# d={"name":"kelly","age":25,"salary":8000,"city":"newyork"}
# d.pop("city")
# print(d)
# d.update({"location":"newyork"})
# print(d)

'''OR'''

# d={"name":"kelly","age":25,"salary":8000,"city":"newyork"}
# d["loction"]=d.pop("city")
# print(d)


'''wap to change athira's salary to 8500'''

# d={"emp1":{"name":"jhon","salary":5000,},
#     "emp2":{"name":"anu","salary":7000},
#     "emp3":{"name":"athira","salary":8000,}}
# d["emp3"]["salary"]=8500
# print(d)     

    # print(d["emp3"]["salary"])


#from keys

