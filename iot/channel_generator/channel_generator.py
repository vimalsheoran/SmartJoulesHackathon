from configs import CONFIG
import requests

DEVICE_LIST = (requests.get(CONFIG["devices"])).json()

def generate_data_channel(device_id):

	for device in DEVICE_LIST:
		channel_string = "1"
		if device["deviceId"] == device_id:
			channel_string = (channel_string+"/"+str(device["communicationType"])
							+"/"+str(device["communicationCategory"]
							+"/"+str(device["networkSlave2"]))
							+"/"+str(device["driverType"])+"/val")
			return channel_string

def generate_control_channel(device_id):
	for device in DEVICE_LIST:
		channel_string = "1"
		if device["deviceId"] == device_id:
			channel_string = (channel_string+"/"+str(device["communicationType"])
							+"/"+str(device["communicationCategory"])
							+"/"+str(device["networkSlave2"])
							+"/"+str(device["driverType"])+"/status"
				)
			return channel_string

def generate_feedback_channel(device_id):
	for device in DEVICE_LIST:
		channel_string = "1"
		if device["deviceId"] == device_id:
			channel_string = (channel_string+"/"+str(device["communicationType"])
							+"/"+str(device["communicationCategory"])
							+"/"+str(device["networkSlave2"])
							+"/"+str(device["driverType"])+"/status/F"
				)
			return channel_string
