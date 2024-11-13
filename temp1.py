import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("localhost",12345))
server_socket.listen(1)
print("Listening on socket!")

while True:
    conn,addr = server_socket.accept()
    print(f"Connected from {addr}")
    filename = conn.recv(1024).decode()
    with open(filename,"wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    conn.sendall(b"File has been recevied by server")
    print("File received")
    conn.close()


server_socket.close()
