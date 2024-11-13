import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
filename="test.txt"
client_socket.connect(("localhost",12345))
client_socket.sendall(filename.encode())

with open(filename,"rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        client_socket.sendall(data)

client_socket.close()
