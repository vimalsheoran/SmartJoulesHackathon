from channel_handler import CONFIG, generate_control_channel, generate_feedback_channel
import json
import requests

COMPONENT_DATA_MAP = {}

components_list = (requests.get(CONFIG["components"])).json()

for component in components_list:
	COMPONENT_DATA_MAP.update({
				str(component["name"]): {}
	})
	new_data = component["controls"]
	for control_pt, pt_id in new_data.iteritems():
		control_channel = generate_control_channel(str(pt_id))
		feedback_channel = generate_feedback_channel(str(pt_id))

		COMPONENT_DATA_MAP[component["name"]].update({
			str(control_pt): {"id": str(pt_id),
							"channel": control_channel,
							"feedback": feedback_channel
			}
		})

with open('control_channel.json', 'w') as file:
	json.dump(COMPONENT_DATA_MAP, file)