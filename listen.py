#!/usr/bin/python

import socket
import sys
import myutils as mu

if len(sys.argv)!=2:
    print("Expected one argument, got", len(sys.argv)-1)
    exit()

ipAddress = ""#"127.0.0.1"
try:
    port = int(sys.argv[1])
except:
    print("Wrong type for first arg, I was expecting a port number!")
    exit()

myName = mu.askName()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipAddress, port))
s.listen(1)
conn, addr = s.accept()
print('[INFO] listening on port: '+str(port))
username = conn.recv(1024)[:-1]
conn.send(myName+"\n")
#while True:
received = conn.recv(1024)[:-1]
print(str(username)+": "+str(received))
conn.close()
