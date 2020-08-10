#!python3

'''
Remote keyboard

08/08/2020 12:04 initial version
'''

import keyboard
import socket
import ui

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)

if keyboard.is_keyboard():
	keyboard.play_input_click()
	keyboard.insert_text(hostname)
	keyboard.insert_text(ipAddress)
else:
	# For debugging in the main app:
	print(f'Keyboard input: {hostname}')
