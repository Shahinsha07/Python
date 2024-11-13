class Book:
    def __init__(self,di):
        self.di=di
    def add_mail(self):
        self.y=[]
        self.mail=(input("Enter email:-"))
        self.y.append(self.mail)
        em=True
        while em==True:
            b=input("Add email? Type 'Y' or 'N'")
            if b=='Y' or b=='y':
                self.mail=(input("Enter email:-"))
                self.y.append(self.mail)
            else:
                em=False
        return self.y
    def add_phone(self):
        self.x=[]
        self.phone=int(input("Enter phone:-"))
        self.x.append(self.phone)
        ph=True
        while ph==True:
            b=input("Add email? Type 'Y' or 'N'")
            if b=='Y' or b=='y':
                self.phone=int(input("Enter phone:-"))
                self.x.append(self.phone)
            else:
                ph=False
        return self.x
    def update(self):
        t=True  
        while t==True:
            if self.di=={}:
                print("Phone Book Empty, Add Details First, Choose option 1 to add for the first Time")
                print()
                break
            else:
                print("1.ADD \n2.UPDATE \n3.Exit")
                b=int(input("Enter the operation:-"))
                print()
                if b==1:
                    print("Is value Number or String \n1.Number \n2.String \n3.Already existing feild")
                    type=int(input("Enter the choice:-"))
                    person=input("Whose details you want to add:-")
                    if type==1:
                        key=input("Enter the key:-")
                        value=int(input("Enter the value:-"))
                        self.di[person].update({key:value})
                        return self.di
                    elif type==2:
                        key=input("Enter the key:-")
                        value=input("Enter the value:-")
                        self.di[person].update({key:value})
                        return self.di
                    elif type==3:
                        key=input("Enter the key:-")
                        if key=='PhoneNumber':
                            p=self.di[person][key]
                            # print(p)
                            val=int(input("Enter the new value:-"))
                            p.append(val)
                            self.di[person][key]=p
                            return self.di
                        elif key=='Email':
                            p=self.di[person][key]
                            # print(p)
                            val=(input("Enter the new value:-"))
                            p.append(val)
                            self.di[person][key]=p
                            return self.di
                elif b==2:
                    self.person=input("whose details you want to update:-")
                    self.field=input("What field you want to update:-")
                    if self.field=="PhoneNumber":
                        print(self.di)
                        choice=int(input("Enter the position Of number:-"))
                        no=int(input("Enter the updated Number:-"))
                        self.di[self.person][self.field][choice]=no
                        return self.di
                    elif self.field=="Email":
                        choice=int(input("Enter the position of email:-"))
                        no=(input("Enter the updated Email:-"))
                        self.di[self.person][self.field][choice]=no
                        return self.di
                    else:
                        if self.field=="Name":
                            data=input("Enter the updated value:-")
                            k=self.di.pop(self.person)
                            k["Name"]=data
                            self.di[data]=k
                            return self.di
                            # print("hai")
                        else:
                            data=input("Enter the updated value:-")
                            self.di[self.person][self.field]=data
                            return self.di
                elif b==3:
                    print("Do yo want to continue")
                    c=input("Yes/No:-")
                    if c=="Yes":
                        t=True
                    elif c=="No":
                        t=False
                else:
                    print("*Invalid Choise*")
                    print()
                    t=False
    def delete(self):
        u=True
        while u==True:
            if self.di=={}:
                print("*Phone Book Empty, Add details*")
                print()
                break
            else:
                print("1.Full \n2.Specific \n3.Exit")
                d=int(input("Enter the operation:-"))
                print()
                if d==1:
                    person=input("whose details you want to Delete:-")
                    del self.di[person]
                    return self.di
                elif d==2:
                    person=input("whose details you want to Delete:-")
                    field=input("What field you want to delete:-")
                    if field=="PhoneNumber" or field=="Email":
                        choice=int(input("Enter the position:-"))
                        del self.di[person][field][choice]
                        return self.di
                    else:
                        del self.di[person][field]
                        return self.di
                elif d==3:
                    print("Do yo want to continue")
                    c=input("Yes/No:-")
                    if c=="Yes":
                        u=True
                    elif c=="No":
                        u=False
                else:
                    print("*Invalid Choise*")
                    print()
                    u=False
    def view_one(self):
        person=input("whose details you want to View:-")
        if self.di==person:
            return self.di[person]
        else:
            print("doesnot exist")
    def view_full(self):
        z=True
        while z==True:
            if self.di=={}:
                print("Phone Book Empty, Add details To View*")
                print()
                z=True
                break
            else:
                print()
                z=False
                return self.di
    def exit(self):
        print("Do yo want to continue")
        c=input("Yes/No:-")
        if c=="Yes":
            w=True
            return w
        elif c=="No":
            w=False
            return w
        
    

di={}    
r=True
while r==True:
    print("Select your choice \n1.ADD a contact \n2.Update a contact \n3.Delete a contact \n4.View a contact \n5.View all contact \n6.Exit")
    a=int(input("Enter your choice:-"))  
    d=Book(di)
    if a==1:
        o={}
        name=input("Enter name")
        addr=input("Enter Address")
        y=d.add_mail()
        x=d.add_phone()
        # print(name)
        # print(addr)
        # print(x)
        # print(y)
        o["Name"]=name
        o["Address"]=addr
        o["Email"]=y
        o["PhoneNumber"]=x
        di[name]=o
        print(di)
    elif a==2:
        z=d.update()
        print(z)
    elif a==3:
        g=d.delete()
        print(g)
    elif a==4:
        h=d.view_one()
        print(h)
    elif a==5:
        l=d.view_full()
        print(l)
    elif a==6:
        r=d.exit()