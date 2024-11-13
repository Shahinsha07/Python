# generate 100 tickets 6 digit number and choose 2 winner
import random
tickets = [random.randint(100000, 100100) for i in range(100)]
print(tickets)
print(random.sample(tickets,2))

#100 to 999 numbers print only 3 numbers divisible by 5
import random
numbers = [random.randrange(100,999,5) for i in range(3)]
print(random.sample(numbers,3))

# import random
# x=[]
# numbers=[random.randint(100,999) for i in range(1000)]
# # print(numbers)
# x=list(numbers)
# # print(x)
# #get 3 numbers in the list divisible by 5
# divisible_by_5 = [i for i in x if i % 5 == 0]
# print(random.sample(divisible_by_5,3))

# import random
# for i in range(3):
#     print(random.randrange(100,999,5),end=" ")

import random
x=random.randint(1,10)

for i in range(3):
    num=int(input("enter a number: "))
    if x==num:
        print("you won")
    else:
        print("you are looser")
print("i guess number is ",x)

# import random
# x=random.randint(1,6)
# y=random.randint(1,6)
# print("player 1 dice ",x,"player 2 dice ",y)
# if x==y:
#     print("draw")
# elif x>y:
#     print("player 1 wins")
# else:
#     print("player 2 wins")

#input: a=["eat","tea","ate","ten","net","bat"]
#output: b=[["eat","tea","ate"],["net","ten"],["bat"]]

a=["eat","tea","ate","ten","net","bat"]
b=[]








