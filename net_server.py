import socket
def main():
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   addr = ("0.0.0.0", 40000)
   sock.bind(addr)
   sock.listen(5)
   #count = 0 
   while True:
      (connectedSock, clientAddress) = sock.accept()

      while True:
         
         try:
            message = connectedSock.recv(1024).decode()
            #msg = "WoW Queue: " + message
            connectedSock.sendall(("WoW Queue: " + message).encode())
            count += 1
            if len(message) == 0:
               connectedSock.close()

         except ConnectionAbortedError:
            connectedSock.close()
            break

         except BrokenPipeError:
            print(count)
            break

main()
