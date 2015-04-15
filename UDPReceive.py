#!/usr/local/bin/python3

import socket
import pymongo
from pymongo import MongoClient
import struct
from struct import unpack

UDP_IP = "192.168.1.100"
UDP_PORT = 5005

client = MongoClient()
db = client.mydb

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    test = unpack('1B', data)
    db.testData.update({ "_id": 1}, {'$push': { "x": {'$each': test}}}, True)
    print ("received message:", test)