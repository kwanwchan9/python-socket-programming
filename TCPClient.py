import socket

HOST = socket.gethostbyname("localhost")  # get the IP address from localhsot
PORT = 9999
ADDR = (HOST, PORT)
FORMAT = 'utf-8'

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(ADDR)
print(c.recv(1024).decode(FORMAT))

height = input("Enter your height(cm): ")
c.send(height.encode(FORMAT))
weight = input("Enter your weight(kg): ")
c.send(weight.encode(FORMAT))

print(c.recv(1024).decode(FORMAT))

c.close