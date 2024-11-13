import mysql.connector

data=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database2024"
)
print("connected")

#create a cursor object using the cursor() method
#the cursor object allows you to execute sql queries aand retrieve results from the databse.

cursor1=data.cursor()
# cursor1.execute("create database database2024")
# print("database created")

# cursor1.execute('create table table11(id int primary key auto_increment,name varchar(20),place varchar(20))')
# print("table created")

# x='insert into table11(name,place) values("ammu","kochi")'
# cursor1.execute(x)
# data.commit()
# print("value inserted")


# x='insert into table11(name,place) values(%s,%s)'
# y=[("appu","kottayam"),("akku","malabar")]
# cursor1.executemany(x,y)
# data.commit()
# print("values inserted")


# cursor1.execute('select * from table11')
# # x=cursor1.fetchall() #all values
# # print(x)
# # for i in x:
# #     print(i)

# x=cursor1.fetchone()
# print(x)
# for i in x:
#     print(i)

# cursor1.execute('update table11 set place="trivandrum" where id=2')
# data.commit()

# cursor1.execute('delete from table11 where id=3')
# data.commit()

cursor1.execute('drop table table11')
data.commit()