import socket

def start_ftp_client(filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print('Connected to server')
    
    client_socket.sendall(filename.encode())
    
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.sendall(data)
    
    print('File sent')
    print(client_socket.recv(1024).decode())
    client_socket.close()

if __name__ == '__main__':
    start_ftp_client("test.txt")
