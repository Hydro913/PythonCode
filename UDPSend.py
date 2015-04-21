#!/usr/local/bin/python3

import math
import socket
import struct
import time
from struct import pack

UDP_IP = "192.168.1.100"
UDP_PORT = 5005

Fs = 1200          #Sampling Frequency
T = 1/Fs            #Sample Times
#L = 100*(Fs/60)     #Length of Signal
L = 1000

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
packer = struct.Struct('f')


for i in range(0, L-1):
    t = i*T

    testData = 15*math.sin(60*2*math.pi*t)
    MESSAGE = packer.pack(testData)
    print ("message:", MESSAGE)
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    time.sleep(0.002)
