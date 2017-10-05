from socket import socket, AF_INET, SOCK_STREAM
import time
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 2345))
timeNow = time.asctime()
print timeNow
s.send(timeNow)
data = s.recv(1024)
print data
s.close()

