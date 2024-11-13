import socket
s=socket.socket()
s.bind(("localhost",9999))
s.listen()
print("waiting for connection")
while True:
    l,address=s.accept()
    name=l.recv(100).decode()
    print("connection",address,name)
    l.send("thankyou for connecting".encode())
    while True:
        client=l.recv(100).decode()
        print("client:",client)
        socket=input("socket:")
        l.send(socket.encode())

