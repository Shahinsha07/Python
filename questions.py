#1.write a program to declare integer,character,flaot,double,boolean and display

# a=10
# b="shazz"
# c=10.3
# d=10.0000002
# e=True
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(type(d))

#2.write a program to print "helloworld"

# print("Hello World")

#3.write a program to print sum of two numbers and display it

# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# print("the sum of 2 number is ",a+b)

#4.write a program to find difference of two numbers

# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# print("the sum of 2 number is ",a-b)

#5.write a program to find cube of a number

# a=int(input("enter a number: "))
# print("the cube of a number is",a**3)

#6.write a program to swap two numbers

# a=10
# b=20

# print("the a is",a,"the b is",b)
# temp=a
# a=b
# b=temp

# print("the a is",a,"the b is",b)

#7.write a program to find the factorial of a number
# a=int(input("enter a number"))
# factorial=1
# for i in range(1,a+1):
    
#     factorial*=i
# print(factorial)

#8.find the largest of two numbers

# a=int(input("enter a number"))
# b=int(input("enter a number"))
# if a>b:
#     print(a,"is greater than",b)
# elif a<b:
#     print(b,"is greater than",a)
# else:
#     print(a,"and",b,"are equal")

#9.find the largest of two numbers

# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))

# if a>b and a>c:
#     print(a,"is greater")
# elif b>a and b>c:
#     print(b,"is greater")
# elif c>a and c>b:
#     print(c,"is greater")
# else:
#     print("all are equal")

#10.check the number is even or not

# a=int(input("enter a number"))

# if a%2==0:
#     print(a,"is even")
# else:
#     print(a,"is not even")

#11.check if the number is odd or not

# a=int(input("enter a number"))

# if a%2!=0:
#     print(a,"is odd")
# else:
#     print(a,"is not odd")

#12.check the given number is divible by 2 and 5(nested if)

# a=int(input("enter a number"))

# if a%2==0 and a%5==0:
#     print("the number is divisible by 2 and 5")
# elif a%2==0 and a%5!=0:
#     print("the number is divisible by 2 but not divisible 5")
# elif a%2!=0 and a%5==0:
#     print("the number is not divisible by 2 but  divisible 5")
# else:
#     print("the number is not divisible by 2 and 5")

#13.check the given number is amstrong or not


# num = int(input("Enter a number: "))

# sum = 0

# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
   
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

#14.check the given number is palindrome or not


# num = int(input("enter a number"))
# temp = num
# reverse_num = 0
# while temp != 0:
#    digit = temp % 10
#    reverse_num = (reverse_num * 10) + digit
#    temp //= 10
# if num == reverse_num:
#    print(num, "is a palindrome number")
# else:
#    print(num, "is not a palindrome number")

#15.check the given number is prime or not

# a=int(input("enter a number"))
# i=2
# prime=True
# while i<a:
#     if a%i==0:
#         print("not a prime")
#         prime=False
#         break
#     i+=1
# if prime:
#     print("prime number")

#16.find the reverse of a number

# a=int(input("enter a number"))
# reverse=0
# while a>0:
#     digit=a%10
#     reverse=(reverse*10)+digit
#     a//=10
# print(reverse)

#17.print given number into words






#18.reverse a string

# a=input("enter a string ")

# print(a[::-1])

#19.print fibonnaci series


# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=' ')
#         a, b = b, a + b


# terms = 10  
# print(f"Fibonacci series for {terms} terms:")
# fibonacci(terms)

#20.write a program to print floyd triangle

# rows = 4  
# num = 1


# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(num, end=' ')
#         num += 1
#     print()  

#21.find the factorial of a given number

# a=int(input("enter a number"))
# factorial=1
# for i in range(1,a+1):
    
#     factorial*=i
# print(factorial)

#22.print numbers upto given limit

limit = 50  # Set your own limit

for num in range(2, limit + 1):
    # Assume num is prime until proven otherwise
    is_prime = True
    
    # Check divisibility by all numbers from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  # If divisible by any number, it's not prime
    
    if is_prime:
        print(num, end=' ')

#23.multiplication table of given number

# a=int(input("which number multiplication table you want "))

# for i in range(1,11):
#     print(a,"x",i,"=",a*i)


#24.sum of 10 numbers


# total = 0

# print("Enter 10 numbers:")

# for i in range(10):
#     num = float(input())  
#     total += num

# print(f"The sum of the 10 numbers is: {total}")

#25.print days of week using switch






#26.check the string is palindrome or not

# a=input("enter a string ")

# b=a[::-1]

# if a==b:
#     print("the string is palindrome")
# else:
#     print("not a palindrome")

#27.accept 10 numbers in array withn and wthout forloop


# Initialize an empty list to store the numbers
# numbers = []

# print("Enter 10 numbers:")


# for i in range(10):
#     num = float(input())  
#     numbers.append(num)  

# print("The numbers you entered are:", numbers)

#without fot loop
# numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(10)]

# print("The numbers you entered are:", numbers)

#28.reverse of an array

# a=[10,20,30,40]
# print(a[::-1])

#29.sum of the elements in array

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total_sum = sum(numbers)

# print("The numbers in the array are:", numbers)
# print("The sum of the elements is:", total_sum)


#30.addition of 2 array

# array1 = [1, 2, 3, 4, 5]
# array2 = [10, 20, 30, 40, 50]

# result = []

# if len(array1) == len(array2):
#     for i in range(len(array1)):
#         result.append(array1[i] + array2[i])
# else:
#     print("Arrays must be of the same length")

# print("Array 1:", array1)
# print("Array 2:", array2)
# print("Sum of arrays:", result)

#31.find the largest element in array

# numbers = [3, 5, 7, 2, 8, 10, 4]

# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

# print("The largest element in the array is:", largest)

#32..sort array in assending order

# numbers = [12, 4, 56, 23, 9, 45]

# numbers.sort()

# print("Sorted array in ascending order:", numbers)

#33.search a element in array

# numbers = [12, 4, 56, 23, 9, 45]

# target = 23

# found = False
# for num in numbers:
#     if num == target:
#         found = True
#         break

# if found:
#     print(f"Element {target} found in the array.")
# else:
#     print(f"Element {target} not found in the array.")

#34.check the 2 array are same or not
# Define two arrays
# a = [10, 20, 30]
# b = [10, 20, 30]

# # Check if the arrays are of the same length
# if len(a) == len(b):
#     # Initialize a flag to track if arrays are the same
#     arrays_same = True
    
#     # Compare each element
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             arrays_same = False
#             break  # No need to check further if any element is different

#     if arrays_same:
#         print("The arrays are the same.")
#     else:
#         print("The arrays are not the same.")
# else:
#     print("The arrays are not the same.")

#35.remove an element in an array

# Define the list of numbers
# numbers = [10, 20, 30, 40, 50]

# value_to_remove = 30

# if value_to_remove in numbers:
#     numbers.remove(value_to_remove)
#     print(f"List after removing {value_to_remove}:", numbers)
# else:
#     print(f"{value_to_remove} not found in the list.")

#36.display a 2x2 matrix

#2x2 matrix
# a=[[1,2],[3,4]]
# for i in a:
#     for j in i:
#         print(j,end=" ")
#     print()

#37.transpose of a matrix

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

#38.sum of 2 matrix

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

#39.3x3 matrix multiplication

# x=[[1,2,3],[4,5,6],[7,8,9]]
# y=[[1,2,3],[4,5,6],[7,8,9]]
# z=[[0,0,0],[0,0,0],[0,0,0]]

# for i in range(len(x)):
#     for j in range(len(y)):
#         for k in range(len(z)):
#             z[i][j]+=x[i][k]*y[k][j]
# print(z)

#40.check whether the given matrix are same or not

# Define two matrices
# matrix1 = [
#     [1, 2],
#     [3, 4]
# ]

# matrix2 = [
#     [1, 2],
#     [4, 4]
# ]

# if matrix1 == matrix2:
#     print("The matrices are the same.")
# else:
#     print("The matrices are not the same.")

#41.if upper diagonal element is lower than lower diagonal element,then replace lower diagonal element with 1 else replace upper diagnal element with zero



# n=int(input("enter a number"))
# a=0
# b=1
# count=0
# while count<n:
#     print(a,end=" ")
#     a=b
#     b=a+b
#     count+=1