import socket
def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    addr = ("lectura.cs.arizona.edu",40000)
    sock.connect(addr)

    for i in range(1, 101):
        print(i)
        sock.sendall(str(i))
        sock.recv()

main()
    

