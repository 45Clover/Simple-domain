# Chat client side 
import socket, threading

#define constants to be used 
DEST_IP = "100.115.92.195"
#change later 
DEST_PORT = 5050
ENCODER = "utf-8"
BYTESIZE = 1024


#create client socket and connect to server 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def receive_messages():
    # Receive messages from the server
    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            if message:
                print(f"\n{message}")
            else:
                # If the message is empty, the server has closed the connection
                print("Connection closed by the server.")
                break
        except:
            # Handle any exceptions that occur
            print("An error occurred. Connection closed.")
            break

def send_messages():
    # Send messages to the server
    while True:
        message = input()
        if message.lower() == "quit":
            client_socket.send("!DISCONNECT".encode(ENCODER))
            print("You have left the chat.")
            break
        else:
            message_length = len(message)
            client_socket.send(f"{message_length}".encode(ENCODER))
            client_socket.send(message.encode(ENCODER))

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

# Wait for both threads to complete
receive_thread.join()
send_thread.join()

# Close the client socket
client_socket.close()

