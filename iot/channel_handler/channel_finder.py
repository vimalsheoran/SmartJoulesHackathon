class ChannelFinder(object):

	def __init__(self, data_channels, control_channels):
		self.operation = ""
		self.component = ""
		self.device = ""
		self.device_id = ""
		self.command = ""
		self.channel = ""
		self.data_channels = data_channels
		self.control_channels = control_channels

	def process_command(self, command_string):
		
		print "processing command........."
		command_buffer = command_string.split('/')
		self.operation = command_buffer[0]
		self.component = command_buffer[1]
		self.command = command_buffer[2]
		self.device = command_buffer[3]
		self.device_id = command_buffer[4]

		if self.operation == "data":
			return "subscribe", ""
		elif self.operation == "control" and self.command == "feedback":
			return "subscribe", ""
		else:
			return "publish", self.command

	def find_channel(self):
		
		print "generating channel........."
		if self.operation == "data":
			dataset = self.data_channels
			return self.data_channel_finder(dataset)
		elif self.operation == "control":
			dataset = self.control_channels
			return self.control_channel_finder(dataset)
		else:
			return "Invalid device type"

	def data_channel_finder(self, dataset):
		for component, devices in dataset.iteritems():
			if component == self.component:
				for device, details in devices.iteritems():
					if device == self.device and details["id"] == self.device_id:
						self.channel = details["channel"]

		return self.channel

	def control_channel_finder(self, dataset):
		for component, devices in dataset.iteritems():
			if component == self.component:
				for device, details in devices.iteritems():
					if device == self.device and details["id"] == self.device_id:
						if self.command == "feedback":
							self.channel = details["feedback"]
						else:
							self.channel = details["channel"]
		return self.channel