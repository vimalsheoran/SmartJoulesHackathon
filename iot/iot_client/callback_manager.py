from configs import CONFIG

import time

class Callback:

	def __init__(self):
		pass

	def on_connect(self, client, userdata, flags, rc):
		if rc == 0:
			print "Establishing connection to %s........." %CONFIG["broker"]
			time.sleep(5)
			print "Connected to broker...OK!"
		else:
			print "Bad connection, returned code %s" %rc

	def on_disconnect(self, client, userdata, flags, rc):
		print "Disconnected from broker...."
		print "OK Code %s" %rc
