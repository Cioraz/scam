import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost',12345))

server_socket.listen(1)
print("Listening for incoming connections...")

connection, client_address = server_socket.accept()
print("Connection from", client_address)

data = connection.recv(1024)
print("Received", data)

connection.sendall(b'Hello from the server!')
connection.close()

server_socket.close()
