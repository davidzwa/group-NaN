import os
import json
import csv


from func import timestampToExcelDatetime

prefix = ""
# aps = None
with open('./aps.json', 'r') as file:
	aps = json.load(file)

channels_per_minute = {}
channels_per_half_minute = {}
for key in aps:
	info = aps[key]

	info["time"] = timestampToExcelDatetime(info["timestamp"])

	minute = int(info["timestamp"] / 60) * 60
	half_minute = int(info["timestamp"] / 30) * 30

	if minute not in channels_per_minute:
		channels_per_minute[minute] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	channels_per_minute[minute][info["channel"]] += 1

	if half_minute not in channels_per_half_minute:
		channels_per_half_minute[half_minute] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	channels_per_half_minute[half_minute][info["channel"]] += 1


fieldnames = []
for mac in aps:
	for field in aps[mac]:
		if field not in fieldnames:
			fieldnames.append(field)


csv.register_dialect('fixed', delimiter=";")
# with open(prefix + 'aps.csv', 'w') as csvfile:
# 	writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='fixed')
#
# 	writer.writeheader()
# 	for mac in aps:
# 		writer.writerow(aps[mac])


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