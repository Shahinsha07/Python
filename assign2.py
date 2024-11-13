class Book:
    def __init__(self, di):
        self.di = di

    def add_mail(self):
        self.y = []
        self.mail = input("Enter email: ")
        self.y.append(self.mail)
        em = True
        while em:
            b = input("Add another email? Type 'Y' or 'N': ")
            if b.lower() == 'y':
                self.mail = input("Enter email: ")
                self.y.append(self.mail)
            else:
                em = False
        return self.y

    def add_phone(self):
        self.x = []
        self.phone = input("Enter phone: ")
        self.x.append(self.phone)
        ph = True
        while ph:
            b = input("Add another phone no? Type 'Y' or 'N': ")
            if b.lower() == 'y':
                self.phone = input("Enter phone: ")
                self.x.append(self.phone)
            else:
                ph = False
        return self.x

    def update(self):
        t = True
        while t:
            if not self.di:
                print("Phone Book is empty. Add details first. Choose option 1 to add a contact.")
                print()
                break
            else:
                print("1. ADD\n2. UPDATE\n3. Exit")
                b = int(input("Enter the operation: "))
                print()
                if b == 1:
                    print("Is the value a Number or String?\n1. Number\n2. String\n3. Already existing field")
                    type_choice = int(input("Enter your choice: "))
                    person = input("Whose details do you want to add?: ")
                    if person not in self.di:
                        print(f"No contact found for {person}.")
                        continue
                    if type_choice == 1:
                        key = input("Enter the key: ")
                        value = int(input("Enter the value: "))
                        self.di[person].update({key: value})
                        print(self.di)
                    elif type_choice == 2:
                        key = input("Enter the key: ")
                        value = input("Enter the value: ")
                        self.di[person].update({key: value})
                        print(self.di)
                    elif type_choice == 3:
                        key = input("Enter the key (PhoneNumber/Email): ")
                        if key == 'PhoneNumber':
                            p = self.di[person][key]
                            val = input("Enter the new phone number: ")
                            p.append(val)
                            self.di[person][key] = p
                            print(self.di)
                        elif key == 'Email':
                            p = self.di[person][key]
                            val = input("Enter the new email: ")
                            p.append(val)
                            self.di[person][key] = p
                            print(self.di)
                elif b == 2:
                    person = input("Whose details do you want to update?: ")
                    if person not in self.di:
                        print(f"No contact found for {person}.")
                        continue
                    field = input("What field do you want to update (PhoneNumber/Email/Name/other): ")
                    if field == "PhoneNumber":
                        print(self.di[person]["PhoneNumber"])
                        choice = int(input("Enter the index of the number to update (starting from 0): "))
                        no = input("Enter the updated number: ")
                        self.di[person]["PhoneNumber"][choice] = no
                        print(self.di)
                    elif field == "Email":
                        print(self.di[person]["Email"])
                        choice = int(input("Enter the index of the email to update (starting from 0): "))
                        no = input("Enter the updated email: ")
                        self.di[person]["Email"][choice] = no
                        print(self.di)
                    elif field == "Name":
                        new_name = input("Enter the updated name: ")
                        self.di[new_name] = self.di.pop(person)
                        self.di[new_name]["Name"] = new_name
                        print(self.di)
                    else:
                        data = input(f"Enter the updated value for {field}: ")
                        self.di[person][field] = data
                        print(self.di)
                elif b == 3:
                    c = input("Do you want to continue? Yes/No: ")
                    if c.lower() == "yes":
                        t = True
                    elif c.lower() == "no":
                        t = False
                else:
                    print("*Invalid Choice*")
                    t = False

di = {}
w = True
while w:
    print("\nSelect your choice\n1. ADD a contact\n2. UPDATE a contact\n3. DELETE a key from a contact\n4. VIEW a contact\n5. VIEW all contacts\n6. EXIT")
    a = int(input("Enter your choice: "))
    d = Book(di)

    if a == 1:
        o = {}
        name = input("Enter name: ")
        addr = input("Enter Address: ")
        y = d.add_mail()
        x = d.add_phone()
        o["Name"] = name
        o["Address"] = addr
        o["Email"] = y
        o["PhoneNumber"] = x
        di[name] = o
        print(di)

    elif a == 2:
        d.update()

    elif a == 3:
        person = input("Enter the name of the contact to delete from: ")
        if person in di:
            field = input(f"Which field do you want to delete from {person}'s contact (Name/Address/Email/PhoneNumber): ")
            if field in di[person]:
                if isinstance(di[person][field], list):
                    print(di[person][field])
                    index = int(input(f"Enter the index of the {field} to delete (starting from 0): "))
                    if 0 <= index < len(di[person][field]):
                        del di[person][field][index]
                        print(f"{field} at index {index} deleted.")
                    else:
                        print(f"Invalid index for {field}.")
                else:
                    del di[person][field]
                    print(f"{field} deleted from {person}'s contact.")
            else:
                print(f"{field} not found in {person}'s contact.")
        else:
            print(f"No contact found for {person}.")

    elif a == 4:
        person = input("Enter the name of the contact to view: ")
        if person in di:
            print(di[person])
        else:
            print(f"No contact found for {person}.")

    elif a == 5:
        if not di:
            print("No contacts available.")
        else:
            for key, value in di.items():
                print(f"{key}: {value}")

    elif a == 6:
        print("Exiting...")
        w = False

    else:
        print("Invalid choice. Please try again.")
