
import socket

cli_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cli_socket.connect(("localhost",12345))
val = int(input("Enter value to multiply"))
cli_socket.sendall(str(val).encode())
data=cli_socket.recv(1024)
print(f"Received : {data}")


cli_socket.close()

