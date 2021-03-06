import pprint

g_speeds = [6, 9, 12, 18, 24, 36, 48, 54]

def parsePacket(packet):
	# wireshark = packet.layers[0]
	radio = packet.layers[1]
	wlan = packet.layers[2]
	wlan2 = packet.layers[3]
	if not hasattr(wlan2, "ssid"):
		return None

	info = {
		"timestamp": float(packet.frame_info.time_epoch.show),
		"source": "beacon",
		"bandwith": 20,
		"mac": wlan.bssid.show,
		"channel": int(radio.channel.show),
		"phy_type": int(radio.phy.show),
		"ssid": wlan2.ssid.show,
		"b_supported": True,
		"g_supported": False,
		"n_supported": False
	}
	# print(float(packet.frame_info.time_epoch.show))
	# print(packet.frame_info.field_names)
	if hasattr(radio, 'data_rate'):
		info["data_rate"] = float(radio.data_rate.show)

	# print(wlan.bssid.show)

	if hasattr(wlan2, 'supported_rates'):
		for field in wlan2.supported_rates.all_fields:
			val = (field.hex_value & 0x7f) / 2
			if int(val) in g_speeds:
				info["g_supported"] = True

			info[val] = True

	if hasattr(wlan2, 'extended_supported_rates'):
		for field in wlan2.extended_supported_rates.all_fields:
			val = (field.hex_value & 0x7f) / 2
			if int(val) in g_speeds:
				info["g_supported"] = True

			info[val] = True

	if hasattr(wlan2, 'ht_capabilities'):
		info["n_supported"] = True
		# print(wlan2.ssid, wlan2.ht_capabilities_width.int_value)
		if wlan2.ht_capabilities_width.int_value == 1:
			info["bandwith"] = 40

	if hasattr(wlan2, 'vht_capabilities'):
		info["ac_supported"] = True
		widths = wlan2.vht_capabilities_supportedchanwidthset.int_value
		if widths == 1:
			info["bandwith"] = 40
		elif widths == 2:
			info["bandwith"] = 80
		elif widths == 3:
			info["bandwith"] = 160

	# print(info)
	return info

def packetToInfo(packet):
	wlan = packet.layers[2]

	# Beacon
	if int(wlan.fc_type_subtype) == 8:
		return parsePacket(packet)

	if int(wlan.fc_type_subtype) == 5:
		return parsePacket(packet)

	return None

class packageFiltered:
	def packagefiltered():
		print ("Constructor called")
