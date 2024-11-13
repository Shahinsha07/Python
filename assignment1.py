# contact={}

# while True:
#     d={}
#     print("\nselect your choice :")
#     print("\n","1.ADD\n","2.VIEW\n","3.ADD/UPDATE\n","4.DELETE","5.EXIT")

#     a=int(input("enter a number:"))

#     if a==1:
#         name=input("enter name:")
#         address=input("enter your adderss:")
        
#         a=int(input("How many ph_numbers do you want to add:"))
#         x=[]
#         for i in range(a):
#             num=int(input("enter the ph_number:"))
#             x.append(num)
        
#         b=int(input("How many email do you want to add:"))
#         y=[]
#         for i in range(b):
#             mail=input("enter the email:")
#             y.append(mail)
#         d["name"]=name
#         d["address"]=address
#         d["phone number"]=x
#         d["mail"]=y
#         contact[name]=d
#     elif a==2:
#         print(contact)
    

#     elif a == 3:
#         name = input("Enter the name of the contact you want to update: ")

#         if name in contact:
#             print("\n1. Update address\n2. Update phone numbers\n3. Update emails\n4. Update name\n")
#             choice1 = int(input("Enter your choice: "))

#             if choice1 == 1:
#                 updated_address = input("Enter your new address: ")
#                 contact[name]["address"] = updated_address
#             elif choice1 == 2:
                
#                 print("\n1. add phone number \n2. Update phone number")

#                 choice=int(input("enter your choice: "))

#                 if choice==1:

#                     num_count = int(input("How many phone numbers do you want to add: "))
#                     up=contact[name]["phone number"]
#                     for i in range(num_count):
#                         phone_number = int(input("Enter the phone number: "))
#                         up.append(phone_number)
#                     contact[name]["phone number"] = up

#                 elif choice==2:
#                         pos=int(input("enter position"))
#                         up_num=int(input("enter update number"))
#                         contact[name]["phone number"][pos]=up_num


#             elif choice1 == 3:
#                 print("\n1. add email \n2. Update email")

#                 choice=int(input("enter your choice: "))

#                 if choice==1:

#                     num_count = int(input("How many email do you want to add: "))
#                     up=contact[name]["mail"]
#                     for i in range(num_count):
#                         email = (input("Enter the mail: "))
#                         up.append(email)
#                     contact[name]["mail"] = up

#                 elif choice==2:
#                         pos=int(input("enter position"))
#                         up_mail=(input("enter update mail"))
#                         contact[name]["mail"][pos]=up_mail
        
#     elif a==4:
#         name = input("Enter the name of the contact you want to delete: ")
#         if name in contact:
#             print("\n1. delete address\n2. delete phone numbers\n3. delete emails\n4. delete full data\n")
#             choice2 = int(input("Enter your choice: "))

#             if choice2==1:
#                 del contact[name]["address"]

#             elif choice2==2:
#                 print("\n 1. del all ph no \n2. delete phone number")

#                 choice=int(input("enter your choice"))

#                 if choice==1:
#                     del contact[name]["phone number"]

#                 elif choice==2:
#                     pos=int(input(" enter  position: "))
#                     del contact[name]["phone number"][pos]            

#             elif choice2==3:
#                 print("\n 1. del all mail \n2. delete mail")

#                 choice=int(input("enter your choice"))

#                 if choice==1:
#                     del contact[name]["mail"]

#                 elif choice==2:
#                     pos=int(input(" enter  position: "))
#                     del contact[name]["mail"][pos]
