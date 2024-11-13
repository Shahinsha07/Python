# Write a Python program that takes two strings as input and performs the following operations:

# Sorts both strings alphabetically.
# Compares the sorted strings to check if each character from the first sorted string is present in the second sorted string.
# Prints whether each character from the first sorted string is present or absent in the second sorted string.
# Use the following example strings to verify your program:

# Example 1:
# Input: a = "TRAVIDUX", b = "VRIDAUTX"
# Expected Output: All characters in the first string are present in the second string.
# Example 2:
# Input: a = "NOON", b = "OLONSEIGHCET"
# Expected Output: All characters in the first string are present in the second string.



# a = input("Enter the first string: ")
# b = input("Enter the second string: ")


# sorted_a = sorted(a)
# sorted_b = sorted(b)


# for i in sorted_a:
#     if i in sorted_b:
#         print("The character '" + i + "' is present in the second string.")

#     else:
#         print("Character '"+i+"' from the first string is absent in the second string.")

a = input("Enter the first string: ")
b = input("Enter the second string: ")

sorted_a = sorted(a)
sorted_b = sorted(b)


all_present = True


for i in sorted_a:
    if i not in sorted_b:
        print("Character '" + i + "' from the first string is absent in the second string.")
        all_present = False


if all_present:
    print("All characters in the first string are present in the second string.")

