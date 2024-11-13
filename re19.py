import re

# '''special squences'''
# s="this is something special"
# x=re.findall("i",s)
# print(x)

# s="this is something special"
# x=re.findall("y",s)
# print(x)

# s="this is something special"
# x=re.findall("is",s)
# print(x)

# s="this is something special"     ## find spaces b/w the words
# x=re.findall("\s",s)
# print(x)

# s="this is something@@## special12345"
# x=re.findall("\S",s)                ## print all words without spaces
# print(x)

# s="this is something@@## special12345"    ## print all numbers
# x=re.findall("\d",s)
# print(x)


# s="this is something@@## special12345"    ## print all items ina given set without number
# x=re.findall("\D",s)
# print(x)


# s="this is something@@## special12345"    ## print all items ina given set without special character
# x=re.findall("\w",s)
# print(x)

# s="this is something@@## special12345"    ## print all special character and spaces in set
# x=re.findall("\W",s)
# print(x)

# s="this is something@@## special12345"    ## to check start with "this"
# x=re.findall("\Athis",s)
# print(x)

# s="this is something@@## special12345"    ## to check end with "special12345"
# x=re.findall("special12345\Z",s)
# print(x)

# s="this is something@@## special12345"    
# x=re.findall(r"\bthis",s)
# print(x)

# s="this is something@@## special12345"    
# x=re.findall(r"\bsome",s)
# print(x)

# s="this is something@@## special12345"    
# x=re.findall(r"12345\b",s)
# print(x)

# s="this is something@@## special12345"       ## find the middle part
# x=re.findall(r"\Bthin",s)
# print(x)


'''sets'''

# s="this is something@@## special12345"       
# x=re.findall("[agsret]",s)
# print(x)

# s="this is something@@## special12345"       ## print a to z small alphabets
# x=re.findall("[a-z]",s)
# print(x)


# s=" AAGSFSFSFSFSFSFSF this is something@@## special12345"       ## print A to Z capital alphabets
# x=re.findall("[A-Z]",s)
# print(x)


# s="this is something@@## special12345"       ## print 1 to 9 numbers
# x=re.findall("[1-9]",s)
# print(x)


# s="ASDERFGHH this is something@@## special12345"       ## print all items in set include space without small alphabets
# x=re.findall("[^a-z]",s)
# print(x)

# s="ASDERFGHH this is something@@## special12345"       ## print all items in set include space without capital alphabets
# x=re.findall("[^A-Z]",s)
# print(x)

# s="ASDERFGHH this is something@@## special12345"       ## print all items in set include space without numbers
# x=re.findall("[^0-9]",s)
# print(x)

# s="ASDERFGHH this is something@@## special12345"       ## to check the set start with ASD
# x=re.findall("^ASD",s)
# print(x)

# s="ASDERFGHH this is something@@## special12345"       ## to check the set end with 12345
# x=re.findall("12345$",s)
# print(x)

# s="ASDERFGHH this is helo something@@## special12345"       ## to check the helo inthe set
# x=re.findall("he.o",s)
# print(x)

# s="hel ASDERFGHH this is helo something@@## special12345"       
# x=re.findall("he.+o",s)
# print(x)

# s="he ASDERFGHH this is helo something@@## special12345"       
# x=re.findall("he.*o",s)
# print(x)

# s="hel ASDERFGHH this is helo something@@## special12345"       
# x=re.findall("he.?o",s)
# print(x)

# s="hel ASDERFGHH this is helo something@@## special12345"       
# x=re.findall("hel|hell",s)
# print(x)

# s="hel ASDERFGHH this is helo something@@## special12345"       
# x=re.findall("[a-z]+",s)
# print(x)

# s="hel 123ASDERFGHH this is 456helo something@@## special12345"       
# x=re.findall("[0-9]+",s)
# print(x)