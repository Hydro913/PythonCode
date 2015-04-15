#!/usr/local/bin/python3

import socket
import struct
from struct import pack

UDP_IP = "192.168.1.100"
UDP_PORT = 5005
MESSAGE = pack('1B', 100)

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
