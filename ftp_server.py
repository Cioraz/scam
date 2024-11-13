import socket

def start_ftp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print('FTP server started on localhost:12345')
    
    while True:
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        filename = client_socket.recv(1024).decode()
        print('Receiving', filename)

        with open(filename, 'wb') as f:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)

        print('File received')
        client_socket.sendall(b'File received')
        client_socket.close()

    server_socket.close()

if __name__ == '__main__':
    start_ftp_server()
