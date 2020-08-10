#!python3

'''
Remote keyboard

08/08/2020 12:04am initial version
08/10/2020 03:40pm ui added. able to receive some data in chunks
'''

import keyboard
import socket
import ui

# Make an UI
view = ui.View()
view.background_color = '#5d5959'
label = ui.Label(frame=view.bounds.inset(0, 4, 0, 36), flex='WH')
label.font = ('Menlo', 12)
label.text_color = 'white'
label.number_of_lines = 0
view.add_subview(label)

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)

if True :#keyboard.is_keyboard():
	if True: #keyboard.has_full_access():
		#keyboard.play_input_click()
		
		# set the view and show the hostname
		#view.present()
		keyboard.set_view(view)
		label.text = hostname+'\n'+ipAddress
		
		# set the server
		tcpIP = ''
		tcpPort = 50005
		bufferSize = 20
		
		label.text = 'setting server'
		
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((tcpIP, tcpPort))
			s.listen(1)
			conn, addr = s.accept()
			with conn:
				label.text = 'Connected to '+str(addr)
				while True:
					data = conn.recv(bufferSize)
					if not data:
						break
					else:
						keyboard.insert_text(data.decode())
						label.text = data.decode()
			
else:
	# For debugging in the main app:
	print(f'Keyboard input: {hostname}')
