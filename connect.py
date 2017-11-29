#!/usr/bin/python

import socket
import sys

if len(sys.argv)!=3:
    print("Expected 2 args, got",len(sys.argv)-1)
    exit()

ipAddress = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[INFO] connecting to: ("+ipAddress+", "+str(port)+")")

try:
    s.connect((ipAddress, port))
    print("[SUCCESS] Connection established!")
except:
    print("[ERROR] Connection refused!")
    exit()

