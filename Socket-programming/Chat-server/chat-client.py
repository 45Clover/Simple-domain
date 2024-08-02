# Chat client side 
import socket

#define constants to be used 
DEST_IP = "100.115.92.195"
#change later 
DEST_PORT = 5050
ENCODER = "utf-8"
BYTESIZE = 1024


#create client socket and connect to server 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


#send and recieve
while True:
    #recieve information from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)


    #QUIT if connected wants to quit ,else keep sending
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat")
        break
    else:
        print(f"\n{message}")
        message = input("Message:")
        client_socket.send(message.encode(ENCODER))



#close client     
client_socket.close()
     
