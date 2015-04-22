#!/usr/local/bin/python3

from numpy.fft import fft
from numpy import array, log10, arange
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydb
Fs = 1200           #Sampling Frequency
T = 1/Fs            #Sample Times

data = db.testData.find_one()
data.pop('_id',None)
values = list(data.values())

a = array(values)
test = a.ravel()

n = len(test)
k = arange(n)
T = n/Fs
frq = k/T
frq = frq[range(n//2)]

Y = fft(test)/n
Y = Y[range(n//2)]

YdB = 20*log10(abs(Y))
YdB = YdB - max(YdB)

print( ' '.join("%5.3f" % g for g in frq ))
print( ' '.join("%5.3f" % f for f in YdB ))



