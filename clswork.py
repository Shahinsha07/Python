#1.write a python program which accepts two strings as input and create a new string by combining specific characters from each input strings based on certain criteria

#example

# s="hello"
# s1="world"
# out="hwlrod"

String1="hello"
String2="world"
result=""
for i in range(0,5,2):
    result+=String1[i]+String2[i]
print(result)

#2.write a program to calculate the product of elements of a list excluding duplicate

list=[1,2,3,3,3,4,5,6,7]

result=1

for i in set(list):
    result*=i
print(result)



#3.write a program that counts the number of strings that have a length greater than 2 and start and end with the same character

list=["hi","hello","mam","malayalam","amma"]
count=0
for i in list:
    if len(i)>2 and i[0]==i[-1]:
        count+=1
print(count)

#4.write a program to remove the characters which have odd index values of a string

str="helloworld"
result=""
for i in range(len(str)):
    if i%2==0:
        result+=str[i]
print(result)

#5.write a python program to change the position of every nth value to the (n+1)th in a list
# input:[0,1,2,3,4,5]
# expected output:[1,0,3,2,5,4]

list1=[0,1,2,3,4,5]
list2=[]

for i in range(len(list1)):
    if i%2==0:
        list2.append(list1[i+1])
    else:
        list2.append(list1[i-1])
print(list2)


#6.write a program to print the length of unique characters in a string

str="shahinsha"
output=""
count=0

for i in str:
    if str.count(i)==1:
        output+=i
        count+=1
print(count)
print(output)

#7.write a program to convert a tuple to a string


t=("python","java","asp.net")
output=" ".join(t)
print(output)

#8. write a python program to separate positive and negative number a list

l=[1,-1,2,-3,4,5]
positive=[]
negative=[]

for i in l:
    if i>0:
        positive.append(i)

    else:
        negative.append(i)

print(positive)
print(negative)

#9.given a list of words,write a python program to count how many anagrams exist for each unique grouping of letters(anagrams).two words are considered anagrams if they contain the same characters in a different order


# • create a dictionary where the keys are the sorted versions of the words (as a string of characters) and the values are the counts of words that match the sorted version.
# • Finally, print out each unique grouping (sorted letters) and the corresponding count of how many words in the list are anagrams of that group.
# Words: ['eat', 'tea', 'ten', 'bat', 'ate", 'net', 'dub', "bud"]

# Expected Output:
# aet: 3
# ent: 2
# abt: 1
# bdu: 2

Words=['eat', 'tea', 'ten', 'bat', 'ate', 'net','dub','bud']
        
anagrams={}
for i in Words:
    sorted_words="".join(sorted(i))
    print(sorted_words)
    if sorted_words in anagrams:
        anagrams[sorted_words]+=1 
    else:
        anagrams[sorted_words]=1
print(anagrams)

# 1.Given a list of integers, move all negative numbers to the left and positive numbers to the right,
#   without changing the order of negative and positive numbers.
#  Example:
#  Input: [1, -2, 3, -4, 5, -6]
#  Output: [-2, -4, -6, 1, 3, 5]

input=[1,-2,3,-4,5,-6]

negative=[x for x in input if x<0]
positive=[x for x in input if x>0]

result=negative+positive
print(result)

# 2.Given a list of words, find all the words that are palindromes (a word that reads the same backward as forward).
#  Example:
#  Input: ['level', 'world', 'madam', 'python', 'noon']
#  Output: ['level', 'madam', 'noon']
input_list = ['level', 'world', 'madam', 'python', 'noon']

palindromes = []

for word in input_list:
    if word == ''.join(reversed(word)):
        palindromes.append(word)

print(palindromes)

# 3.Given a string, replace all vowels in the string with a specific character.
#  Example:
#  Input: "programming", replacement char = '*'
#  Output: "pr*gr*mm*ng"

Input="programming"
v="aeiou"

for i in v:
    Input=Input.replace(i,"*")

print(Input)
    

# 4.Given a sentence, find the longest word in it.
#  Example:
#  Input: "she is reading a book"
#  Output: "reading"

Input= "she is reading a book"
b=Input.split()
print(b)

lw=""
for i in b:
    if len(i)>len(lw):
        lw=i
print(lw)

# 6.Given two lists, find the common elements between them.
#  Example:
#  Input:
#  List1: [1, 2, 3, 4]
#  List2: [3, 4, 5, 6]
#  Output: [3, 4]

List1= [1, 2, 3, 4]
List2= [3, 4, 5, 6]
l=[]
for i in List1:
    for j in List2:
        if i==j:
            l.append(j)
print(l)

# 7. Given a string and a character, find the index of the first occurrence of the character.
#  Example:
#  Input: "hello world", char = 'o'
#  Output: 4


