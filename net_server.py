import socket
 

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #choose_a_port_number = int(input())
    addr = ("0.0.0.0", 40000)
    sock.bind(addr)
    sock.listen(5)
    (connectedSock, clientAddress) = sock.accept()
    msg = sock.recv(1024).decode()
    sock.sendall(message.encode())
        

main()
