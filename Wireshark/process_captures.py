
import pyshark
import model
import os
from pprint import pprint
import glob
import json
import csv

aps = {}
channels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for file in glob.glob("./captures/*.pcapng"):
	print(file)
	capture = pyshark.FileCapture(input_file=file)

	for packet in capture:
		info = model.packetToInfo(packet)
		if info is None:
			continue

		if info["mac"] in aps:
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
