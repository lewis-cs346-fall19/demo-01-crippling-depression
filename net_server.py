import socket
def main():
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   addr = ("0.0.0.0", 40000)
   sock.bind(addr)
   sock.listen(5)
   while True:
      (connectedSock, clientAddress) = sock.accept()

      while True:

         try:
            message = connectedSock.recv(1024).decode()
            
            connectedSock.sendall(("RECIEVED"+message).encode())

         except ConnectionAbortedError:
            giving_a_message = False
            connectedSock.close()
            break

main()
