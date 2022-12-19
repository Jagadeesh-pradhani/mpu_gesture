from mpu6050 import mpu6050
import time
import socket
mpu = mpu6050(0x68)
flag=0


UDP_IP = "192.168.43.50"        # Recivers IP adress
UDP_Port = 5005             # Any empty port
sock = socket.socket(socket.AF_INET,    #Internet
socket.SOCK_DGRAM)      # UDP
start = "["
end = "]"
mid1 = ","
mid2 = "."

while True:
    accel_data = mpu.get_accel_data()
    x1 = float(accel_data['x'])
    y1 = float(accel_data['y'])
    z1 = float(accel_data['z'])
    x = str(round(x1, 4))
    y = str(round(y1, 4))
    z = str(round(z1, 4))
    sock.sendto(start, (UDP_IP, UDP_Port))
    sock.sendto(x, (UDP_IP, UDP_Port))
    sock.sendto(mid1, (UDP_IP, UDP_Port))
    sock.sendto(y, (UDP_IP, UDP_Port))
    sock.sendto(mid2, (UDP_IP, UDP_Port))
    sock.sendto(z, (UDP_IP, UDP_Port))
    sock.sendto(end, (UDP_IP, UDP_Port))
    print(x, y, z)
