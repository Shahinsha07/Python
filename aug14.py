# from key is useful when we need to initialize a dictionary with a set of keys and common values

# key=["a","b","c"]
# value=10
# value1=[1,2,3]
# x=dict.fromkeys(key,value)
# y=dict.fromkeys(key,value1)
# print(x)
# print(y)


'''set default'''
#setdefault method in python is used to insert a key with a specified value into a dictionary if the key is not already present.if the key is present,
# it returns the value of that key this method is useful for ensuring a key is present in a dictionary and assigning a default value if it isn't


# my={"name":"ammu"}
# my.setdefault("age",10)
# print(my)
# my.setdefault("age",None)
# print(my)
# my.setdefault("name","anu")
# print(my)

#1 to 10 is keys and the values are square 

# d={}
# for i in range(1,11):
#     d[i]=i*i
# print(d)


'''dictionary comprehension'''


# d={key:value for i in  iterable if condition}

# d={i:i*i for i in range(1,11)}
# print(d)

#only print even number squares

# d={i:i*i for i in range(1,11) if i%2==0}
# print(d)

# swap keys and values using dictionary comprehension

# d={"a":1,"b":2,"c":3}

# d={v:k for k,v in d.items()}
# print(d)

#print dictionary which contain value(age) are even

# a={"ammu":10,"anu":20,"tintu":15,"pinky":25}

# a={v:i for v,i in a.items() if i%2==0}
# print(a)

#print dictionary which contain value(age) are even and greater than 20

# a={"ammu":15,"anu":18,"tintu":35,"pinky":30}
# a={v:i for v,i in a.items() if i%2==0 and i>20}
# print(a)

# print dictionary which contain value(age)   greater than 20 as "old" and less than 20 as "young"

# a={"ammu":15,"anu":18,"tintu":35,"pinky":30}
# a={i:"old" if j>20 else "young" for i,j in a.items()}
# print(a)

# increment everyone salary by 5000

# a={"ammu":15000,"anu":18000,"tintu":35000,"piny":30000}
# a={i:j+5000 for i,j in a.items()}
# print(a)

company={
    'E001':{'name':'alice','position':'manager','salary':85000,'department':'HR'},
    'E002':{'name':'bob','position':'developer','salary':95000,'department':'IT'},
    'E003':{'name':'Charlie','position':'designer','salary':70000,'department':'Design'},
    'E004':{'name':'Diana','position':'Developer','salary':90000,'department':'IT'},
    'E005':{'name':'Eve','position':'manager','salary':92000,'department':'Sales'}

}

# 1. get all employee in a specific department

# department=input("enter the department")
# for i in company.values():
#     if i['department']==department:
#         print(i['name'])



# 2. find the employee with highest salary


highest_salary = 0
highest_salary_employee = None


for emp_id, details in company.items():
    if details['salary'] > highest_salary:
        highest_salary = details['salary']
        highest_salary_employee = details

print("The employee with the highest salary is:")


print("name & salary: ",highest_salary_employee['name'])



# 3. promote an employee (eg:E002) by increasing salary and updating position

employee_id_to_promote = input("enter emp id: ")

new_position = input("enter emp new position: ")
salary_increase = 5000

# Promote the employee by updating their salary and position
if employee_id_to_promote in company:
    company[employee_id_to_promote]['salary'] += salary_increase
    company[employee_id_to_promote]['position'] = new_position
    promoted_employee = company[employee_id_to_promote]
    print("Employee promoted:")
    print(F"ID: {employee_id_to_promote}, Name: {promoted_employee['name']}, Position: {promoted_employee['position']}, Salary: ${promoted_employee['salary']}, Department: {promoted_employee['department']}")
else:
    print(f"Employee with ID {employee_id_to_promote} not found.")

