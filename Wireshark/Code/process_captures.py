
import pyshark
import model
import os
from pprint import pprint
import glob
import json
import csv

from func import timestampToExcelDatetime

# Prefix to give the output files
# By default they will be called 
# 	aps.json
# 	aps.csv
# 	per_minute.csv
# 	per_half_minute_cumulative.csv
# This prefix is added to the front of the file which makes is easier to distinguish different parsed datasets
prefix = ""
# Pattern for the files to parse
# For parsing a single file just change to file path
pattern = "./captures/*.pcapng"

aps = {}
channels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
phy_types = {
	"b": 0,
	"g": 0,
	"n": 0
}
speed_types = {
	1.0: 0,
	2.0: 0,
	5.5: 0,
	6.0: 0,
	9.0: 0,
	11.0: 0,
	12.0: 0,
	18.0: 0,
	24.0: 0,
	36.0: 0,
	48.0: 0,
	54.0: 0,
	63.5: 0
}


channels_per_minute = {}
channels_per_half_minute = {}

num_packets = 0
for file in glob.glob(pattern):
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
		# 	previousinfo = aps[info["mac"]]
		# 	if previousinfo["ssid"] != info["ssid"]:
		# 		if not hasattr(previousinfo, 'ssids'):
		# 			previousinfo["ssids"] = [previousinfo["ssid"]]
		# 		if info.ssid not in previousinfo["ssids"]:
		# 			previousinfo["ssids"].append(info["ssid"])
			continue

		aps[info["mac"]] = info
		channels[info["channel"]] += 1
		if info["b_supported"]:
			phy_types["b"] += 1

		if info["g_supported"]:
			phy_types["g"] += 1

		if info["n_supported"]:
			phy_types["n"] += 1

		for key in speed_types:
			if key in info:
				speed_types[key] += 1

		info["time"] = timestampToExcelDatetime(info["timestamp"])

		minute = int(info["timestamp"] / 60) * 60
		half_minute = int(info["timestamp"] / 30) * 30

		if minute not in channels_per_minute:
			channels_per_minute[minute] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		channels_per_minute[minute][info["channel"]] += 1

		if half_minute not in channels_per_half_minute:
			channels_per_half_minute[half_minute] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		channels_per_half_minute[half_minute][info["channel"]] += 1

pprint(channels)
pprint(phy_types)
pprint(speed_types)

data = json.dumps(aps, indent='\t')
with open(prefix + 'aps.json', 'w') as file:
	file.write(data)
	file.close()

fieldnames = []
for mac in aps:
	for field in aps[mac]:
		if field not in fieldnames:
			fieldnames.append(field)


csv.register_dialect('fixed', delimiter=";")
with open(prefix + 'aps.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='fixed')

	writer.writeheader()
	for mac in aps:
		writer.writerow(aps[mac])


with open(prefix + "per_minute.csv", 'w') as csvfile:
	writer = csv.writer(csvfile, dialect='fixed')
	writer.writerow(["time", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])
	for key in sorted(channels_per_minute.keys()):
		v = channels_per_minute[key]
		writer.writerow([
			timestampToExcelDatetime(key),
			v[1],
			v[2],
			v[3],
			v[4],
			v[5],
			v[6],
			v[7],
			v[8],
			v[9],
			v[10],
			v[11],
			v[12],
			v[13]
		])

with open(prefix + "per_half_minute_cumulative.csv", 'w') as csvfile:
	writer = csv.writer(csvfile, dialect='fixed')
	writer.writerow(["time", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])

	previous_key = None
	for key in sorted(channels_per_half_minute.keys()):
		v = channels_per_half_minute[key]
		if previous_key is not None:
			pv = channels_per_half_minute[previous_key]
			for i in range(1, 14):
				v[i] = v[i] + pv[i]
		writer.writerow([
			timestampToExcelDatetime(key),
			v[1],
			v[2],
			v[3],
			v[4],
			v[5],
			v[6],
			v[7],
			v[8],
			v[9],
			v[10],
			v[11],
			v[12],
			v[13]
		])
		previous_key = key