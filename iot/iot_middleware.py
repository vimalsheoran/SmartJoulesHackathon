from server_config import SERVER_CONFIG
from channel_handler import ChannelFinder
from iot_client import IotClient

import socket
import json

DATA_CHANNELS = json.load(open("data_channel.json","r"))
CONTROL_CHANNELS = json.load(open("control_channel.json", "r"))

CHANNEL_FINDER = ChannelFinder(DATA_CHANNELS, CONTROL_CHANNELS)

IOT_CLIENT = IotClient()
IOT_CLIENT.connect_broker()
IOT_CLIENT.start_service()

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
		comm_type, command = CHANNEL_FINDER.process_command(data)
		channel = CHANNEL_FINDER.find_channel()
	if comm_type == "subscribe":
		incoming_conn.send(str(IOT_CLIENT.subscribe(channel)))
	elif comm_type == "publish":
		incoming_conn.send(str(IOT_CLIENT.publish(channel, command)))

IOT_CLIENT.stop_service()
iot_socket.close()

# Test channels

#### Subscribe #####

# data/Chilled Water Pump 1/data/EM/146

#### Publish ####

# control/Chilled Water Pump 1/command/start/69

#### Feedback ####

# control/Chilled Water Pump 1/feedback/start/69