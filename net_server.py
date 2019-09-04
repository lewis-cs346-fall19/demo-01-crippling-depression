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
            msg = "WoW Queue: " + message
            connectedSock.sendall(msg.encode())

         except ConnectionAbortedError:
            connectedSock.close()
            break

main()
