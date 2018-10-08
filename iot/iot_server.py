from server_config import SERVER_CONFIG

import socket

iot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

iot_socket.bind(SERVER_CONFIG["HOST_PORT_CONF"])
iot_socket.listen(1)

incoming_conn, incoming_addr = iot_socket.accept()
print 'Connected to', incoming_addr
while True:
	data = incoming_conn.recv(1024)
	if not data:
		break
	incoming_conn.send(data)
iot_socket.close()
