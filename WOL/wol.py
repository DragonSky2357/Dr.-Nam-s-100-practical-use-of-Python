import struct
import socket

mycoms = {
    "pc1": "AA-BB-CC-DD-EE-FF",
    "pc2": "11-22-33-44-55-66",
    "XEON": "2C-FD-A1-34-32-10",
}
mac = "00-D8-61-2D-C6-40"
addrs = mac.split("-")
hw_addr = struct.pack("BBBBBB", int(addrs[0], 16), int(addrs[1], 16), int(
    addrs[2], 16), int(addrs[3], 16), int(addrs[4], 16), int(addrs[5], 16))
magic = b"\xFF"*6 + hw_addr*16

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(magic, ('192.168.0.255'), 7)
c.close()
