import re

'''search case'''

text="hello my name is ammu"
x=re.search("ammu",text) #first occurence only will give
print(x)
# text="hello my name is ammu"
# x=re.search("hello",text)
# print(x)

print(x.span())
print(x.start())
print(x.end())
print(x.group())
print(x.string)

'''ignore case'''
text="hello AMMU, my name is ammu"
x=re.search("ammu",text) #first occurence only will give
print(x)
x=re.search("ammu",text,re.IGNORECASE) #IGNORECASE consider capital and small letters are same
print(x)

text="hello AMMU, my name is ammu"
x=re.search("^hello",text) #check hello is starting
print(x)

text="hello AMMU, my name is ammu"
x=re.search("ammu$",text) #it will check ammu is last
print(x)

text="hello AMMU123, my name456 is ammu789"
x=re.search("\d",text) #first occurence only will give
print(x)

text="hello AMMU123, my name456 is ammu789"
x=re.search("\d+",text) #first group of number will return
print(x)

text="hello AMMU123, my name456 is ammu789"
x=re.split(" ",text) #split space wiil occur 
print(x)

text="hello AMMU123, my name456 is ammu789"
x=re.split(" ",text,2) #split first 2
print(x)

text="hello AMMU123, my name456 is ammu789"
x=re.split("\d+",text) #split number will occur
print(x)

text="apple-orange:grapes|mango"
x=re.split("[-:|]",text)
print(x)

text="hello hello hello"
x=re.sub("ll","@",text) #2 l will change @
print(x)

text="hello hello hello"
x=re.sub("ll","@",text,2) # fist 2 will change
print(x)

text="hello my number is 9876543210"
x=re.sub("\d{10}","xxxxxxxxxx",text) #phonenumber will change to x
print(x)

'''match it will check the word will start the string.otherwise it will return none'''

text="hello my name is ammu"
x=re.match("hello",text)
print(x)

text="hello my name is ammu"
x=re.match("ammu",text)
print(x)