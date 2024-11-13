import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b'Hello from the client!', ('localhost', 12345))

data, server_address = client_socket.recvfrom(1024)
print("Received", data, "from", server_address)


client_socket.close()
