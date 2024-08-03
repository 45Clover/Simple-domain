#server side chat room
import socket, threading
#Define constants

HOST_IP = "100.115.92.195"
#change it later 
HOST_PORT = 5050
ENCODER = "utf-8"
BYTESIZE = 1024
DISCONNECT_Message = "!DISCONNECT"


#Create a server socket, bind to ip/port and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()


#accept connection and response

#..\n newline




#blank list store connected client sockets 
client_socket_list = []
client_name_list = []

def handle_client(conn, addr):
    print (f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            msg_length = conn.recv(BYTESIZE).decode(ENCODER)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(ENCODER)
                if msg == DISCONNECT_Message:
                    connected = False
                    client_socket_list.remove(conn)
                    print(f"[DISCONNECTED] {addr} disconnected.")
                else:


                    print(f"[{addr} {msg}]")
                    broadcast_message(f"[{addr} {msg}]")
                
        except:
            connected = False
            client_socket_list.remove(conn)
            print(f"[ERROR] {addr} disconnected unexpectedly.")

    conn.close()
            


def broadcast_message(message):
    for client_socket in client_socket_list:
        try:
            client_socket.send(message.encode(ENCODER))
        except:
            client_socket_list.remove(client_socket)



def start_server(message=""):
     server_socket.listen()
     print(f"[LISTENING] Server is listening on {HOST_IP}")
     while True:
        conn, addr = server_socket.accept()
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
start_server()
#send message to all connected clients



def receive_message(client_socket):
    server_socket.recv()
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

receive_message()


    



#receive from allvclients and fowardbto be bradcasted


def connect_client():



    pass
#connects incoming clients
