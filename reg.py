users={}
def register():
    username=input("enter a user name: ")
    password=input("enter a password")
    confirm_pswd=input("confirm password")

    if password==confirm_pswd:
        users[username]=password
        print("registeration succesfully")
    else:
        print("password not match. Try again")

def login():
    username=input("enter a user name: ")
    password=input("enter a password")
    if username in users and users[username]==password:
        print("login succesfully")
    else:
        print("invalid login")
w=True
while w:
    print("main menu","\n","1.register\n2.login\n3.exit")
    choice=int(input("enter a choice: "))
    if choice<=3:
        if choice==1:
            register()
        elif choice==2:
            login()
        elif choice==3:
            print("exit")
            w=False
        else:
            print("invalid login")
            w=False