
import pyshark

for channel in range(1, 14):
	file = './captures/channel_' + str(channel) + '.cap'
	capture = pyshark.FileCapture(input_file=file)

	for packet in capture:

		print(channel, packet)