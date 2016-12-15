import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8000))
sock.listen(10)

while True:
    c, a = sock.accept()
    data = c.recv(2048).decode('UTF-8')
    data = data.split()
    data = data[1]
    f = open(data, 'rb')
    c.send(f.read())
c.close
sock.close()