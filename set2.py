# y={True,10,20,"java",0,"php",False}
# print(y)
#methods

# print(dir(y))

# k=[10,20,30]
# p={"python","java",10,20}
# p.add("orange")
# print(p)
# p.update(y)
# print(p)
# p.update(k)
# print(p)
# p={"python","java",10,20}
# p.remove("java")
# print(p)
# p={"python","java",10,20}
# p.discard("python")
# print(p)
# p={"python","java",10,20}
# p.remove("abc")
# print(p)
# p={"python","java",10,20}
# p.discard("abc")
# print(p)
# p={"python","java",10,20}
# p.clear()
# print(p)


# p={"python","java","hai","hello"}
# q={"php","dotnet","hai","hello"}
# x=p.union(q)
# print(x)
# print(p|q)

# p={"python","java","hai","hello"}
# q={"php","dotnet","hai","hello"}
# x=p.intersection(q)
# print(x)
# print(p&q)
# p.intersection_update(q)
# print(p)
# p&=q
# print(p)

# p={"python","java","hai","hello"}
# q={"php","dotnet","hai","hello"}
# x=p.difference(q)
# print(x)
# print(p-q)
# p.difference_update(q)
# print(p)
# p-=q
# print(p)

# p={"python","java","hai","hello"}
# q={"php","dotnet","hai","hello"}
# x=q.difference(p)
# print(x)
# print(q-p)


# p={"python","java","hai","hello"}
# q={"php","dotnet","hai","hello"}
# x=p.symmetric_difference(q)
# print(x)
# print(p^q)
# p.symmetric_difference_update(q)
# print(p)
# p^=q
# print(p)


# p={"python","java","hai","hello"}
# for i in p:
#     print(i)

# p={"python","java","hai","hello"}
# y=p.pop()
# print(p)
# print(y)

# numbers={1,2,3,4,5,6,7,8,9,10}
# odd={1,3,5,7,9}
# even={2,4,6,8}
# print(numbers.issuperset(odd))
# print(numbers.issuperset(even))
# print(odd.issuperset(even))
# print(odd.issubset(even))
# print(odd.issubset(numbers))
# print(odd.isdisjoint(even))

# odd={1,3,5,7,9}
# p=odd.copy()
# print(p)



#pgm to add all elements in list1 into given set
# set1={"yellow","orange","black"}
# list1=["blue","green","red"]
# set1.update(list1)
# print(set1)

#return a new set of identical items from 2 sets

# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# set=set1.intersection(set2)
# print(set)


#get only unique items from 2 sets
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# set3=set1.union(set2)
# print(set3)

# update the 1st set with items that dont exist in the 2nd set
# set1={10,20,30}
# set2={20,40,50}
# set1.difference_update(set2)
# print(set1)

#return a set of elements present in set1 or set2 but not both
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# y=set1.symmetric_difference(set2)
# print(y)