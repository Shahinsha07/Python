import socket
c=socket.socket()
c.connect(("localhost",9999))
name=input("enter your name")
c.send(name.encode())
x=c.recv(100).decode()
print(x)