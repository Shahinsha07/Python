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