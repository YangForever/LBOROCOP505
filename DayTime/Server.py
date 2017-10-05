from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.bind(("127.0.0.1", 2345))
s.listen(3)
while True:
    conn, addr = s.accept()
    print "connect to: ", addr
    time = conn.recv(1024)
    print time
    conn.send("see you")
    conn.close()
