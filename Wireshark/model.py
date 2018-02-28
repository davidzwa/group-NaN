def packetToInfo(packet):
	radio = packet.layers[1]
	wlan = packet.layers[2]

	# Beacon
	if int(wlan.fc_type_subtype) == 8:
		wlan2 = packet.layers[3]
		info = {
			"source": "beacon",
			"bandwith": 20,
			"channel": radio.channel,
			"ssid": wlan2.ssid
		}
		if hasattr(wlan2, 'ht_capabilities'):
			info["n"] = True
			if wlan2.ht_capabilities_width == 1:
				info["bandwith"] = 40

		if hasattr(wlan2, 'vht_capabilities'):
			info["ac"] = True
			widths = wlan2.vht_capabilities_supportedchanwidthset.int_value
			if widths == 1:
				info["bandwith"] = 40
			elif widths == 2:
				info["bandwith"] = 80
			elif widths == 3:
				info["bandwith"] = 160

		print(info)
		return info

	if int(wlan.fc_type_subtype) == 5:
		wlan2 = packet.layers[3]
		info = {
			"source": "probe response",
			"bandwith": 20,
			"channel": radio.channel,
			"ssid": wlan2.ssid
		}
		if hasattr(wlan2, 'ht_capabilities'):
			info["n"] = True
			if wlan2.ht_capabilities_width == 1:
				info["bandwith"] = 40

		if hasattr(wlan2, 'vht_capabilities'):
			info["ac"] = True
			widths = wlan2.vht_capabilities_supportedchanwidthset.int_value
			if widths == 1:
				info["bandwith"] = 40
			elif widths == 2:
				info["bandwith"] = 80
			elif widths == 3:
				info["bandwith"] = 160
		print(info)
		return info

	return None

class packageFiltered:
	def packagefiltered():
		print ("Constructor called")
