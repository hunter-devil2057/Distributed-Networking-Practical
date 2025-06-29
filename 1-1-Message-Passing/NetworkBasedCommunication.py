import socket
from threading import Thread

def server():
    s = socket.socket()
    s.bind(('localhost', 12345))
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(1024)
    print("Server received:", data.decode())
    conn.close()
    s.close()

# Client
def client():
    s = socket.socket()
    s.connect(('localhost', 12345))
    s.send(b"Hello from client")
    s.close()

Thread(target=server).start()
Thread(target=client).start()