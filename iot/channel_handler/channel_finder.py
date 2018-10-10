class ChannelFinder(object):

	def __init__(self, data_channels, control_channels):
		self.operation = ""
		self.component = ""
		self.device = ""
		self.device_id = ""
		self.channel_type = ""
		self.channel = ""
		self.data_channels = data_channels
		self.control_channels = control_channels

	def process_command(self, command_string):
		command_buffer = command_string.split('/')
		self.operation = command_buffer[0]
		self.component = command_buffer[1]
		self.channel_type = command_buffer[2]
		self.device = command_buffer[3]
		self.device_id = command_buffer[4]

	def find_channel(self):
		
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
			print self.component
			print component
			if component == self.component:
				for device, details in devices.iteritems():
					if device == self.device and details["id"] == self.device_id:
						self.channel = details["channel"]

		return self.channel

	def control_channel_finder(self, dataset):
		for component, devices in dataset.iteritems():
			print self.component
			print component
			if component == self.component:
				for device, details in devices.iteritems():
					if device == self.device and details["id"] == self.device_id:
						if self.channel_type == "feedback":
							self.channel = details["feedback"]
						else:
							self.channel = details["channel"]
		return self.channel		

# sample command structure
# data/Chilled Water Pump 1/data/EM/146
# sample control command structure
# control/Chilled Water Pump 1/feedback/start/69