from socket import socket, AF_INET, SOCK_STREAM
import CountWords
import json

s = socket(AF_INET, SOCK_STREAM)
s.bind(("127.0.0.1", 2345))
s.listen(3)
while True:
    conn, addr = s.accept()
    print "connect to: ", addr
    data = conn.recv(1024)
    print 'receive: ', data
    num = CountWords.Count(data)
    num = json.dumps(num)
    conn.send(num)
    conn.close()
