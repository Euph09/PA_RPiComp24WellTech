import socket
import time

#Setup server details
listenSocket=socket.socket()
port = 8000
maxConnections = 1
IP = socket.gethostname()

#Bind the socket to port 8000
listenSocket.bind(('',port))

#Listen for message, with a max of maxConnections connections
listenSocket.listen(maxConnections)

#Accept connection
clientsocket, addresss = listenSocket.accept()

#Recieve message with buffer of 8 and decode
message = clientsocket.recv(32).decode()
print(message)
