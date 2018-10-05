from channel_generator import generate_data_channel, CONFIG
import requests
import json

COMPONENT_DATA_MAP = {}

components_list = (requests.get(CONFIG["components"])).json()

for component in components_list:
	COMPONENT_DATA_MAP.update({
				str(component["name"]): {}
	})
	new_data = component["data"]
	for data_pt, pt_id in new_data.iteritems():
		data_channel = generate_data_channel(str(pt_id))
		COMPONENT_DATA_MAP[component["name"]].update({
			str(data_pt): {"id": str(pt_id),
							"channel": data_channel}
		})

with open('data_channel.json', 'w') as file:
	json.dump(COMPONENT_DATA_MAP, file)