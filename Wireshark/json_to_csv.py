import os
import json
import csv

data = None
with open('./aps.json', 'r') as file:
	data = json.load(file)

fieldnames = []
for mac in data:
	for field in data[mac]:
		if field not in fieldnames:
			fieldnames.append(field)

# dia = csv.Dialect()
# dia.delimiter = ";"
# dia.quoting = csv.QUOTE_MINIMAL
# dia.doublequote
csv.register_dialect('fixed', delimiter=";")
with open('aps.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='fixed')

	writer.writeheader()
	for mac in data:
		writer.writerow(data[mac])