# '''from a list of numbers remove zero to the end of the list'''

# list1=[1,0,2,0,4,6]

# for i in list1:
#     if i==0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)




# '''write a python function that takes a list and return a new list with distinct elements from the list'''
# list1=[1,2,3,3,3,3,4,5]
# list2=[]
# for i in list1:
#     if i not in list2:
        
#         list2.append(i)
# print(list2)



'''find the missing number'''
list1=[1,2,4,5,6]
list2=[]
for i in range(1,7):
    # print(i)
    if i not in list1:
        list2.append(i)
        print(i)
print(list2)


# '''OR'''

# # def display(l):
# #     n=len(l)+1
# #     total=n*(n+1)//2
# #     total_l=sum(l)
# #     missing_num=total-total_l
# #     return missing_num
# # list1=[1,2,4,5,6]
# # print(display(list1))


# '''what is the python program to find paris of numbers a given list such that the sum of 
# their squares equals a perfect square a^2+b^2=c^2'''

import math

numbers = [1,2,3,4,5,6,7,8,9,10]

def is_perfect_square(n):
    return int(math.sqrt(n))**2 == n


print("Pairs of numbers (a, b) such that a^2 + b^2 = c^2:")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        a = numbers[i]
        b = numbers[j]
        sum_of_squares = a**2 + b**2
        if is_perfect_square(sum_of_squares):
            c = int(math.sqrt(sum_of_squares))
            print(f"({a}, {b}) where {a}^2 + {b}^2 = {c}^2")
     


    

# '''sorted method'''
# ## syntax : sorted(iterable,key=none,reverse=True)    

# l=[10,12,81,54,60]
# print(sorted(l))
# l=[10,12,81,54,60]
# print(sorted(l,reverse=True))

# x=["abc","python","apple","bat","java"]
# print(sorted(x,key=len))



# #reversed
# l=[10,12,81,54,60]
# print(list(reversed(l)))

# for i in reversed(range(5)):
#     print(i)


# a="hello"
# x="".join(reversed(a))
# print(x)