# Chat server side

import socket
#Define constant to be used 
HOST_IP = "100.115.92.195"
#change it later 
HOST_PORT = 5050
ENCODER = "utf-8"
BYTESIZE = 1024


#Create a server socket, bind to ip/port and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

#accept connection and response
print("Server running....\n")
client_socket, client_address = server_socket.accept()
client_socket.send("Your connected....\n".encode(ENCODER))
#..\n newline



#Send/recieve messades
while True:
    #recieve client info
    message = client_socket.recv(BYTESIZE).decode(ENCODER)


    #Quit if client wants to quit, else display the message
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\n Ending chat")
        break
    else:
        print(f"\n{message:}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))


#Close the socket
server_socket.close()
