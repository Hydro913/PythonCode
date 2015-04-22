#!/usr/local/bin/python3

import socket
import pymongo
from pymongo import MongoClient
import struct
from struct import unpack

UDP_PORT = 5005

client = MongoClient()
db = client.mydb

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind(('',UDP_PORT))

unpacker = struct.Struct('f')

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    test = unpacker.unpack(data)
    db.testData.update({ "_id": 1}, {'$push': { "x": {'$each': test}}}, True)
    print ("received message:", test)
