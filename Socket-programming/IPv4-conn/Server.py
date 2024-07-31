import socket
#two way or 1 way communication endpoint
import threading 
#thread is seperated flow 
#importing multiple python threads 


HEADER = 64 #bit length of message but padded
PORT = 5050
SERVER = "100.115.92.195"
#Since im running it of this device 
#SERVER = socket.gethostbyname (socket.gethostname())
#When you dont want to search for ip ^
#It may return 127.0.0.1 (the loopback address) if the hostname is not properly configured or if the network configuration does not associate a proper IP address with the hostname.
ADDR = (SERVER, PORT)
#Binding socket to address
FORMAT = 'utf-8'
DISCONNECT_Message = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#creates socket(Family,type) of socket
server.bind(ADDR)#actual binding


def handle_client(conn, addr):
    print (f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_Message:
                connected = False

            print(f"[{addr} {msg}]")
            conn.send("Msg received".encode(FORMAT))
        
    conn.close()

    
#handles individual connections
#pass is just a place holder before use
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        #waits on new connection to store addrs of connection
        #conn = connection object 
        #addr = ip,port address
        #listen =for incoming connections
        #accepts =  connection
        #arg- argumenst
        #f string = a way to embed expressions inside string 
#handles new connections
#firewall may a problem
print("[STARTING] server is starting...")
start()
