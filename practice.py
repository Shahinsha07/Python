# 1.Question: How do you append an element(example 4) to a list?

# list=[1, 2, 3]
# list.append(4)
# print(list)

# 2.Question: How can you remove an element from a list by value(remove 3)?

# list=[1,2,3,4]
# list.remove(3)
# print(list)

# 3.Question: How do you sort a list in ascending order?

# list=[3, 1, 4, 2]
# list.sort()
# print(list)

# 4.Question: How can you find the length of a list?

# my_list = [1, 2, 3, 4]
# print(len(my_list))

# 5.Question: How do you access an element in a list by index?

# my_list = [10, 20, 30, 40]

# print(my_list[1])

# 6.Question: How can you reverse a list?

# my_list = [1, 2, 3, 4]

# print(my_list[::-1])

# 7.Question: How do you extend a list with another list?

# my_list = [1, 2]
# another_list = [3, 4]
# my_list.extend(another_list)
# print(my_list)


# 8.Question: How can you count the occurrences of an element in a list(count of 2)?

# my_list = [1, 2, 2, 3]

# count = 0
# for i in my_list:
#     if i == 2:
#         count+= 1

# print(count)  


# 9.Question: How can you insert an element at a specific index in a list(Insert 2 at index 1)?

# my_list = [1, 3, 4]

# my_list.insert(1, 2)
# print(my_list) 


# 10.Question: How do you pop an element from a list by index(Remove element at index 2)?

# my_list = [1, 2, 3, 4]

# my_list.pop(2)
# print(my_list)


# 11.Question: How can you clear all elements from a list?


# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)

# 12.Question: How do you find the maximum element in a list(using max function also you can find maximum value from a list)?
# my_list = [5, 3, 9, 1]
# max_value = max(my_list)
# print(max_value)  

# 13.Question: How can you find the minimum element in a list(using min function also you can find minimum value from a list?
# my_list = [5, 3, 9, 1]
# min_value = min(my_list)
# print(min_value)

# 14.Question: How can you slice a list to get a subset(Get elements from index 2 to 4)?

# my_list = [0, 1, 2, 3, 4, 5]
# sub_list=my_list
# print(sub_list[2:5])

# 15.Question: How do you concatenate two lists?

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# concatenated_list = list1 + list2
# print(concatenated_list)  

# 16.Question: How can you check if an element exists in a list?

# my_list = [1, 2, 3, 4]

# if 2 in my_list:
#     print("already exist in my list")
# else:
#     print("not exist")

# 17.Question: How do you find the index of the first occurrence of an element in a list?

# my_list = [1, 2, 3, 2]

# first_index_of_2 = my_list.index(2)
# print(first_index_of_2)  

# 18.Question: How can you replace an element at a specific index in a list(Replace element at index 1 by 5)?

# my_list = [1, 2, 3]

# my_list[1] = 5
# print(my_list)  

# print(dir(my_list))

# 19.Question: How do you extend a list by adding another list's elements?
# my_list = [1, 2]
# another_list = [3, 4]
# # Output: [1, 2, 3, 4]

# my_list.extend(another_list)
# print(my_list)

# 20.Question: How can you remove all occurrences of an element from a list?
# my_list = [1, 2, 2, 3, 2]
# Output: [1, 3]


# my_list = [1, 2, 2, 3, 2]

# while 2 in my_list:
#     my_list.remove(2)

# print(my_list)  

# 21.Question: How do you get a list of unique elements from a list?

# my_list = [1, 2, 2, 3, 4, 4]
# # Output: [1, 2, 3, 4]
# a=[]
# for i in my_list:
#     if i not in a:
#         a.append(i)

# print(a)

# 22.Question: How can you convert a string into a list of characters?
# my_string = "hello"
# char_list = list(my_string)
# print(char_list)  
# Output: ['h', 'e', 'l', 'l', 'o']

# 23.Question: How do you create a list from a string using a specified delimiter?
# my_string = "apple,banana,cherry"
# # Output: ['apple', 'banana', 'cherry']

# a=my_string.split(",")

# print(list(a))

# 24.Question: How can you find the sum of all elements in a list?

# my_list = [1, 2, 3, 4]
# sum=0

# for i in my_list:
#     sum+=i

# print(sum)

# 25.Question: How do you create a list of squares of numbers from 1 to 5?
# Output: [1, 4, 9, 16, 25]



# list=[1,2,3,4,5]
# square=[]
# for i in list:
#     square.append(i**2)
# print(square)

# 26.Question: How can you find the intersection of two lists?

# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# # Output: [2, 3]
# list=[]
# for i in list1:

#         if i in list2:
#             list.append(i)
# print(list)

# 27.Question: How do you remove duplicates from a list while maintaining order?
# my_list = [1, 2, 2, 3, 4, 4]
# # Output: [1, 2, 3, 4]

# s=set(my_list)
# print(list(s))

# 28.Question: How can you convert a list of integers to a list of strings?

# int_list = [1, 2, 3]
# str_list = []
# for num in int_list:
#     str_list.append(str(num))
# print(str_list)  
# Output: ['1', '2', '3']

# 29.Question: How do you find the common elements in three lists?
# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# list3 = [3, 4, 5]
# # Output: [3]
# list=[]
# for i in list1:
#     if i in list2 and i in list3:
#         list.append(i)
# print(list)

# 30.Question: How do you remove all elements from a list using a while loop?
# my_list = [1, 2, 3, 4]

# while len(my_list)>0:
#     my_list.pop()
# print(my_list)

# 31.Question: How can you multiply all the elements in a list?
# my_list = [1, 2, 3, 4]
# # Output: 24
# a=1
# for i in my_list:
#     a*=i
# print(a)

# 32.Question: How can you find the difference between two lists (elements in the first list but not in the second)?
# list1 = [1, 2, 3, 4]
# list2 = [2, 4]
# # Output: [1, 3]
# list=[]
# for i in list1:
#     if i not in list2:
#         list.append(i)
# print(list)

# 33.Question: How can you check if a list is a palindrome (reads the same forward and backward)?

# my_list = [1, 2, 3, 2, 1]


# palindrome = my_list[::-1]


# if palindrome == my_list:
#     print("palindrome")
# else:
#     print("not a palindrome")


# 34.Question: How do you find the second largest element in a list?

# my_list = [10, 20, 4, 45, 99]
# a=0

# for i in my_list:
#     if i>a:
#         a=i
# print(a)


# 35.Question: How can you check if all elements in a list are the same?

# my_list = [2, 2, 2, 2]

# a=set(my_list)

# if len(a)==1:
#     print("all same")

# else:
#     print("not same")

# 36.Question: How can you find the length of each element in a list of strings?


# Output: [5, 6, 6]

# string_list = ["apple", "banana", "cherry"]

# length= []
# for i in string_list:
#     length.append(len(i))

# print(length)  

# 37.Question: How can you split a list into two lists: one with even numbers and one with odd numbers?
# my_list = [1, 2, 3, 4, 5, 6]
# # Output: [2, 4, 6]
# # Output: [1, 3, 5]
# even=[]
# odd=[]

# for i in my_list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even=",even)
# print("odd=",odd)

# 38.Question: How do you remove elements at even indices from a list?
# my_list = [1, 2, 3, 4, 5, 6]
# # Output: [2, 4, 6]
# new=[]
# for i in range(len(my_list)):
#     if i%2!=0:
#         new.append(my_list[i])
# print(new)


# 39.Question: How can you remove all negative numbers from a list?
# my_list = [1, -2, 3, -4, 5]
# Output: [1, 3, 5]

# my_list = [1, -2, 3, -4, 5]
# new=[]
# for i in my_list:
#     if i>0:
#         new.append(i)
# print(new)

# 40.Question: How do you find the minimum and maximum elements in a list?
# my_list = [10, 20, 30, 40, 50]
# min_value = min(my_list)
# max_value = max(my_list)
# print("Min:", min_value)  
# print("Max:", max_value)



# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

 

# Example 1:

# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:

# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

s = "PPAALP"

absent_count=s.count("A")

# print(absent_count)

consecutive_late= "LLL" in s

eligible= absent_count<2 and not consecutive_late

print(eligible)

