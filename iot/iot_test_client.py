from server_config import SERVER_CONFIG

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(SERVER_CONFIG["HOST_PORT_CONF"])

data_packet = raw_input(">")

while data_packet != 'q':
	client_socket.send(data_packet)
	data = client_socket.recv(1024)
	print(str(data))
	data_packet = raw_input('>')

client_socket.close()
