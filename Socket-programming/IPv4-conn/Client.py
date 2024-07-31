import socket



HEADER = 64 #bit length of message but padded
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_Message = "!DISCONNECT"
SERVER = "100.115.92.195"
ADDR = (SERVER, PORT)
#SERVER = socket.gethostbyname (socket.gethostname())
#When you dont want to search for ip ^
#It may return 127.0.0.1 (the loopback address) if the hostname is not properly configured or if the network configuration does not associate a proper IP address with the hostname.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)



def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World")
input()
send("Hello Does it work")
input()
send("Hello it should work")
input()
send("Hello I've got a lot to tell you")




send(DISCONNECT_Message)

# Send mutiple from client load smae script else where



