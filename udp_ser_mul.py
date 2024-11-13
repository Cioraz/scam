import socket

ser_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ser_socket.bind(("localhost",12345))
print("Listening on server")

data,addr=ser_socket.recvfrom(1024)
print(f"Connected to client {addr}")
data=int(data.decode())
data=data*2
ser_socket.sendto(str(data).encode(),addr)
print("New data sent to client")


ser_socket.close()
