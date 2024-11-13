import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12345))

client_socket.sendall(b'Hello from the client!')

data = client_socket.recv(1024)
print("Received", data)

client_socket.close()
