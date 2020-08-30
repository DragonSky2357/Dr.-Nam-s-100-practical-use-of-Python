import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 12000))

sock.sendall("Hello socket programming".encode())

sock.close()
