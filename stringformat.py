# #string formats

# print("my name is {} my age is {} my hobby is {}".format("shazz",18,"playing"))
# print("my name is {0} my age is {1} my hobby is {2}".format("shazz",18,"playing"))

# #keyword arguements
# print("my name is {a} my age is {b} my hobby is {c}".format(a="shazz",b=18,c="playing")) #igne chyumboll placeholdernte ullil key value nthayaalum kodkanm

# a="shazz"
# b=18
# c=10.23
# print("my name is %s"%a) #string aavumboll %s
# print("my age is %d"%b)  #integer aavumboll %d
# print("my age is %f "%c)  #float aavumboll %f

# a="shazz"
# print(f"my name is {a}") 

# a="hello\nhai\nhello"
# print(a.split()) #\n varilla 

# print(a.splitlines(True)) #\n varum true nthayaalum kodkanm

# a="heilo world"
# result=a.maketrans("heilo","02546")
# y=a.translate(result)
# print(y)

#format_map

# a={"name":"shazz","age":10}
# s={'"NAME":{name},"AGE":{age}'.format_map(a)}
# print(s)

# a="hello welcome hai"
# print(a.partition("welcome"))
# a="hello welcome hai"
# print(a.partition("hello"))
# a="hello welcome hai"
# print(a.partition("hai"))
# a="hello welcome hai"
# print(a.partition("abc"))
# a="hello welcome hai"
# print(a.rpartition("hello"))
# a="hello welcome hai"
# print(a.rpartition("abc"))

# a="wel\tcome" #space edkunth athinte multiple koodi consider chythit aavvum  
# print(a)
# print(a.expandtabs()) #default value 8 annu
# print(a.expandtabs(10))
# print(a.expandtabs(29))
# print(a.expandtabs(6))
# print(a.expandtabs(1))
# print(a.expandtabs(2))
# print(a.expandtabs(3))
# print(a.expandtabs(4))
# print(a.expandtabs(5))
# print(a.expandtabs(6))
# print(a.expandtabs(7))
# print(a.expandtabs(8))
# print(a.expandtabs(9))
# print(a.expandtabs(10))

# a="abc"
# print(a.isascii())
# a="ABC"
# print(a.isascii())  #emojis alpha gamma beta athpolle ullath ascii values alla
# a="123"
# print(a.isascii())
# a="@#$%"
# print(a.isascii())

# #ascii value find cheyaan
# a="a"
# print(ord(a))
# a="A"
# print(ord(a))
# a="Z"
# print(ord(a))
# a=91
# print(chr(a)) #ascii value athinte correspond value kittaan

#encode

# txt = "My name is Stale"

# x = txt.encode()

# print(x)
# print(type(x))

# y=x.decode()
# print(y)
# print(type(y))

