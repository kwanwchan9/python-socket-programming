# Introduction

Simple TCP server and client socket programs scripted by python, to send and receive data about the user information and thus, calculate the Body Mass Index (BMI) of the user.

# Implementation Details

The socket is created by the function of socket.socket using IPV4 [AF_INET] and TCP connection [SOCK_STREAM] in the hosted IP address which is the localhost in the case and bind with an empty port no which is 9999 [s.bind()]. The maximum no of connections allowed for the server is set to be 5 [s.listen()] each time.

Once the connection of the client hit the port and IP address of the server requesting for connection [c.connect()], the server will accept [s.accept()] and build the connection.

The messages send and received by both side will be encoded or decoded in the format of utf-8. The calculation will take place on the serve side

# Screenshot

TCP server started and connection estabilished:
![Demo_Img_1](/image/screenshot1.png)

User input information from the client side and information are received in the server side:
![Demo_Img_2](/image/screenshot2.png)

Throw Error Message if received error information:
![Demo_Img_3](/image/screenshot3.png)
