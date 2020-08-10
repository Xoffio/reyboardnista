#!/usr/bin/env python

import socket

tcpIP = '192.168.1.11'
tcpPort = 50005
BUFFER_SIZE = 1024
msg = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((tcpIP, tcpPort))

while True:
    msg = input("> ")
    s.send(msg.encode())

    if (msg == "exit"):
        break
s.close()
