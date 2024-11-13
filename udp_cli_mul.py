import socket

cli_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data=int(input("Enter value to mul: "))
cli_socket.sendto(str(data).encode(),("localhost",12345))
data,addr=cli_socket.recvfrom(1024)
print(f"Data Received: {data.decode()}")

cli_socket.close()
