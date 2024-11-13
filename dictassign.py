contact = {}

while True:
    d = {}
    print("\nSelect your choice:")
    print("\n1. ADD\n2. VIEW\n3. ADD/UPDATE\n4. DELETE\n5. EXIT")

    a = int(input("Enter a number:"))

    if a == 1:
        name = input("Enter name: ")
        address = input("Enter your address: ")
        
        a = int(input("How many phone numbers do you want to add: "))
        x = []
        for i in range(a):
            num = int(input("Enter the phone number: "))
            x.append(num)
        
        b = int(input("How many emails do you want to add: "))
        y = []
        for i in range(b):
            mail = input("Enter the email: ")
            y.append(mail)
        
        d["name"] = name
        d["address"] = address
        d["phone number"] = x
        d["mail"] = y
        contact[name] = d
        print(contact)
        #add values into the file
        # f=open("phonebook.txt","w")
        # f.write(str(contact))
        # f.close()

        

    elif a == 2:
        print("1. view all contacts \n2. view only specified contact")
        choice=int(input("enter your your choice: "))
        if choice==1:
            print(contact)
        
        elif choice==2:
            name=input("enter name you want to view: ")
            print(contact[name])

    elif a == 3:
        name = input("Enter the name of the contact you want to update: ")

        if name in contact:
            print("\n1. Update address\n2. Update phone numbers\n3. Update emails\n4. Update name\n")
            choice1 = int(input("Enter your choice: "))

            if choice1 == 1:
                updated_address = input("Enter your new address: ")
                contact[name]["address"] = updated_address
            elif choice1 == 2:
                print("\n1. Add phone number\n2. Update phone number")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    num_count = int(input("How many phone numbers do you want to add: "))
                    up = contact[name]["phone number"]
                    for i in range(num_count):
                        phone_number = int(input("Enter the phone number: "))
                        up.append(phone_number)
                    contact[name]["phone number"] = up

                elif choice == 2:
                    pos = int(input("Enter position: "))
                    up_num = int(input("Enter update number: "))
                    contact[name]["phone number"][pos] = up_num

            elif choice1 == 3:
                print("\n1. Add email\n2. Update email")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    num_count = int(input("How many emails do you want to add: "))
                    up = contact[name]["mail"]
                    for i in range(num_count):
                        email = input("Enter the email: ")
                        up.append(email)
                    contact[name]["mail"] = up

                elif choice == 2:
                    pos = int(input("Enter position: "))
                    up_mail = input("Enter update email: ")
                    contact[name]["mail"][pos] = up_mail

            elif choice1 == 4:
                new_name = input("Enter the new name: ")
                x = contact.pop(name)
                x["name"]=new_name
                contact[new_name]=x


    elif a == 4:
        name = input("Enter the name of the contact you want to delete: ")
        if name in contact:
            print("\n1. Delete address\n2. Delete phone numbers\n3. Delete emails\n4. Delete full data\n")
            choice2 = int(input("Enter your choice: "))

            if choice2 == 1:
                del contact[name]["address"]

            elif choice2 == 2:
                print("\n1. Delete all phone numbers\n2. Delete phone number")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    del contact[name]["phone number"]

                elif choice == 2:
                    pos = int(input("Enter position: "))
                    del contact[name]["phone number"][pos]

            elif choice2 == 3:
                print("\n1. Delete all emails\n2. Delete email")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    del contact[name]["mail"]

                elif choice == 2:
                    pos = int(input("Enter position: "))
                    del contact[name]["mail"][pos]

            elif choice2 == 4:
                del contact[name]

    elif a == 5:
        break
    else:
        print("Invalid choice. Please try again.")