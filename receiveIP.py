import socket
import threading

IP = '0.0.0.0'
PORT = 9998


def receiveIP():
    ret_IP=""
    ret_USER=""
    ret_PASS=""
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    for i in range(3):
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        
        if i == 0:  
            ret_IP = handle_client(client)
        if i == 1:
            ret_USER = handle_client(client)
        if i == 2:
            ret_PASS = handle_client(client)
    print(ret_IP, ret_USER, ret_PASS)
    return ret_IP, ret_USER, ret_PASS


def handle_client(client_socket):
    
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACKKK')
    
    return request.decode("utf-8")


if __name__ == '__main__':
    receiveIP()
