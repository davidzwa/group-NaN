import pyshark
from model import packageFiltered

def runTshark():
	a =  packageFiltered()
	try:
		capture = pyshark.LiveCapture(interface='wlan0mon', only_summaries=True)
		print(capture.interfaces)
		while (1):
			for packet in capture.sniff_continuously(packet_count=1000):
				print("Packet: " + str(packet))
	except Exception as e:
		print("wlan0mon excepted " + str(e))
