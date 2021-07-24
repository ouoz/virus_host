import socket
import threading

IP = '0.0.0.0'
PORT = 9998


def receiveIP():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    client, address = server.accept()
    print(f'[*] Accepted connection from {address[0]}:{address[1]}')
    return handle_client(client)


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACKKK')
        return request.decode("utf-8")


if __name__ == '__main__':
    receiveIP()
