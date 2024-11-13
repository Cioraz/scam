import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(("localhost",12345))
print("Listening for incoming connections...")

data, client_address = server_socket.recvfrom(1024)
print("Received", data, "from", client_address)
server_socket.sendto(b'Hello from the server!', client_address)
server_socket.close()
