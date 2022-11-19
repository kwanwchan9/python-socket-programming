import socket

HOST = socket.gethostbyname("localhost") # Get the IP address from the localhost
PORT = 9999
ADDR = (HOST, PORT)
FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket by IPV4 and TCP connection
s.bind(ADDR) # Bind the socket's IP address and Port
print("[STARTING] Server is starting...")
s.listen(5) # allow for max 5 connection at the same time
print(f"[LISTENING] Server is listening on {HOST}")

while True:
    c, addr = s.accept() 
    print(f"[NEW CONNECTION] Connection from {addr} has been established!")
    c.send("[Status]The server has been successfully connected".encode(FORMAT))

    height = c.recv(1024).decode(FORMAT)
    print(f"[MSG RECEIVED] User's height = {height}")

    weight = c.recv(1024).decode(FORMAT)
    print(f"[MSG RECEIVED] User's weight = {weight}")

    try:
        bmi = (round(float(weight) / ((float(height) / 100) ** 2),1))
        print(f"User's BMI = {bmi}") 

        if bmi <= 0:
            msg = f"There is an error with your input, please check your entered value."

        elif bmi < 18.5:
            msg = f"Your BMI is {bmi}, You are underweight."

        elif bmi >= 18.5 and bmi < 25:
            msg = f"Your BMI is {bmi}, You are normal." 

        elif bmi >= 25 and bmi < 30:
            msg = f"Your BMI is {bmi}, You are overweight."

        elif bmi >= 30:
            msg = f"Your BMI is {bmi}, You are obese."
    
        c.send(msg.encode(FORMAT))

    except ZeroDivisionError:
        print("Oops!! User has input a zero numbers")

        msg = f"There is an error with your input, please check your entered value."
        
        c.send(msg.encode(FORMAT))

s.close()