import re
text="Hello,my name is john. I have two cats, Mia and Max."
x=re.findall(r"\b\w{3}\b",text)
print(x)

# text="contact info@examble.com or support@examble.com."
# x=re.findall(r"\b\w+@\w+\.\w+\b",text)
# print(x)

text="Improtant dates:2022-01-01,2023-05-15,and 2023-12-31"
# x=re.findall(r"\b[0-9]+-[0-9]+-[0-9]+\b",text)
# print(x)
# x=re.findall(r"\d{4}-\d{2}-\d{2}",text)
# print(x)

p="fdfdfgzsfsgf1234"
b=re.findall(r"\b\d{10}\b",p)
print(b)