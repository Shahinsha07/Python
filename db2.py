import sqlite3
mydb=sqlite3.connect('abcd.db')
print("database created")

cursor1=mydb.cursor()
# cursor1.execute('create table table111(id integer primary key autoincrement,name varchar(20),place varchar(20))')
# print("table created")

# x='insert into table111(name,place) values("ammu","kochi")'
# cursor1.execute(x)
# mydb.commit()

# x='insert into table111(name,place) values(?,?)'
# y=[("appu","kottayam"),("akku","malabar")]
# cursor1.executemany(x,y)
# mydb.commit()
# print("values inserted")


# x=cursor1.execute('select id,name,place from table111')
# print(x)
# for i in x:
#     print(i)
#     print(type(i))
#     print("id= ",i[0])
#     print("name= ",i[1])
#     print("place= ",i[2])

# cursor1.execute('update table111 set place="trivandrum" where id=2')
# mydb.commit()

# cursor1.execute('delete from table111 where id=3')
# mydb.commit()

x='insert into table111(name,place) values("abu","kochi")'
cursor1.execute(x)
mydb.commit()