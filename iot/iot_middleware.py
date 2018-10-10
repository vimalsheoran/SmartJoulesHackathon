from server_config import SERVER_CONFIG
from channel_handler import ChannelFinder

import socket
import json

DATA_CHANNELS = json.load(open("data_channel.json","r"))
CONTROL_CHANNELS = json.load(open("control_channel.json", "r"))

CHANNEL_FINDER = ChannelFinder(DATA_CHANNELS, CONTROL_CHANNELS)

iot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

iot_socket.bind(SERVER_CONFIG["HOST_PORT_CONF"])
iot_socket.listen(1)

incoming_conn, incoming_addr = iot_socket.accept()
print 'Connected to', incoming_addr
while True:
	data = incoming_conn.recv(1024)
	if not data:
		break
	else:
		CHANNEL_FINDER.process_command(data)
		channel = CHANNEL_FINDER.find_channel()
	incoming_conn.send(channel)

iot_socket.close()
