from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 2345))
data = raw_input("input a line: ")
print 'sending: ', data
s.send(data)
data = s.recv(1024)
print data
s.close()

