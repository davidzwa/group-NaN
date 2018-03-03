
import pyshark
import model
import os
from pprint import pprint
import glob
import json
import csv

aps = {}
channels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num_packets = 0
for file in glob.glob("./captures/*.pcapng"):
	print(file)
	capture = pyshark.FileCapture(input_file=file)

	for packet in capture:
		num_packets += 1
		if (num_packets % 100) == 0:
			print(num_packets)

		info = model.packetToInfo(packet)
		if info is None:
			continue

		if info["mac"] in aps:
			previousinfo = aps[info["mac"]]
			if previousinfo["ssid"] != info["ssid"]:
				if not hasattr(previousinfo, 'ssids'):
					previousinfo["ssids"] = [previousinfo["ssid"]]
				if info.ssid not in previousinfo["ssids"]:
					previousinfo["ssids"].append(info["ssid"])
			continue

		aps[info["mac"]] = info
		channels[info["channel"]] += 1

pprint(channels)

data = json.dumps(aps, indent='\t')
with open('aps.json', 'w') as file:
	file.write(data)
	file.close()

fieldnames = []
for mac in aps:
	for field in aps[mac]:
		if field not in fieldnames:
			fieldnames.append(field)


csv.register_dialect('fixed', delimiter=";")
with open('aps.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='fixed')

	writer.writeheader()
	for mac in aps:
		writer.writerow(aps[mac])
