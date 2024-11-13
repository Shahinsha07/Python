#pgm to add all elements in list1 into given set

set1={"yellow","orange","black"}
list1=["blue","green","red"]
set1.update(list1)
print(set1)

#return a new set of identical items from 2 sets #given elements are common in 2 sets

# set1={10,20,30,40,50}
# set2={50,40,30,45,12}
# set=set1.intersection(set2)
# print(set)

# return a new set of unique item from 2 sets

# set1={10,20,30,40,50}
# set2={10,30,50,55,66}
# set=set1.union(set2)
# print(set)

# update the 1st set with items that dont exist in the 2nd set

# set1={10,20,30,40,50,55}
# set2={40,50,10,20}
# set1.difference_update(set2)
# print(set1)

#return a set of elements present in set1 or set2 but not both

# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# y=set1.symmetric_difference(set2)
# print(y)