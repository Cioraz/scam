import socket

ser_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ser_socket.bind(("localhost",12345))
ser_socket.listen(1)
print("Listening on server")

conn,addr = ser_socket.accept()
print(f"Connected to client {addr}")
data = int(conn.recv(1024).decode())
data=data*2
conn.sendall(str(data).encode())
print(f"New data sent to client {addr}")
conn.close()


ser_socket.close()

