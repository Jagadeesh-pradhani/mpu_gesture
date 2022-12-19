import time
import socket

UDP_IP = "192.168.43.50"  #ip address of RPI on which this code is running
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
x =0
y = 0
z = 0

while True:
        msg, addr = sock.recvfrom(1024) # buffer 1024 bytes
        if msg == "[":
           x, addr = sock.recvfrom(1024)
           x = float(x)
        elif msg == ",":
           y, addr = sock.recvfrom(1024)
           y = float(y)
        elif msg == ".":
            z, addr = sock.recvfrom(1024)
            z = float(z)
        
        print(x, y, z)
        
        f = open("filex", "a")
        f.write(str(x))
        f.write("\n")
        
        f = open("filey", "a")
        f.write(str(y))
        f.write("\n")
        
        f = open("filez", "a")
        f.write(str(z))
        f.write("\n")
