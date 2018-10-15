from configs import CONFIG
from callback_manager import Callback

import paho.mqtt.client as mqtt
import time

class IotClient:

	def __init__(self):
		self.client = mqtt.Client()
		# setup all the callback functions here
		self.callback = Callback()
		self.client.on_connect = self.callback.on_connect
		self.client.on_disconnect = self.callback.on_disconnect

	def connect_broker(self):
		self.client.connect(CONFIG["broker"])

	def start_service(self):
		print "Starting service loop...."
		self.client.loop_start()

	def stop_service(self):
		self.client.loop_stop()
		print "Ending service loop...."
		time.sleep(2)
		self.client.disconnect()

	def subscribe(self, channel):
		return self.client.subscribe(channel)

	def publish(self, channel, data):
		return self.client.publish(channel, data)

