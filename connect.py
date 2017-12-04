#!/usr/bin/python

import socket
import sys
import myutils as mu

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
myName = mu.askName()
s.send(myName+"\n")
username = s.recv(1024)[:-1]
mu.sendMsg(s, "Hello how are you?")
exit()
while True:
    received = s.recv(1024)
    print '{}: {}'.format(username, received)
    s.send("Hello how are you\n")
