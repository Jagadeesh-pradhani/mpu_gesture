# mpu_gesture
## gesture controlled drone
![image](https://user-images.githubusercontent.com/97280653/208385762-b7bd9eb0-25f6-449c-9d24-94130a76f3ae.png)

### Making a gesture controlled drone using MPU-6050
1) We used 2 Raspberrypi, One to send MPU data to Drone, another to recive MPU data and give commands to Drone using Dronekit
2) Follow this link to know about communication between RPI and Pixhawk 
https://github.com/Jagadeesh-pradhani/AeroKLE

### MPU and RPI communication
1) connect as following

![image](https://user-images.githubusercontent.com/97280653/208387055-dc45fb20-47b6-4b93-922d-12613e2e7e90.png)

2) Connect both RPI to same a network.

3) Get the IP-adress of reciver RPI from terminal
```
ifconfig
```

### Client or MPU
1) Here client side is MPU which will be in our hand.
2) You need to open 1 terminal to send data to drone, and run the send.py prgram

### Server or Drone
1) Here the server side is the RPI present in drone.
2) Open 2 terminal 1 to send data, other to run dronekit program.
