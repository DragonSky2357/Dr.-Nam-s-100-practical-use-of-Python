import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("", 12000))

sock.listen()

c_sock, addr = sock.accept()

receive_data = c_sock.recv(1024)
print("수신된 데이터: {}".format(receive_data.decode()))

c_sock.close()
sock.close()
