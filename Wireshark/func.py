from subprocess import call
program = "[func.py]:"

def set(channel=0):
	print program + " Setting channel to " + str(channel)
	call("airmon-ng check kill", shell=True)
	if channel and int(channel):
		call("airmon-ng start wlan0 " + channel, shell=True)
	else:
		call("airmon-ng start wlan0", shell=True)
def stop():
	call("airmon-ng stop wlan0mon", shell=True)	
def reset():
	call("airmon-ng stop wlan0mon", shell=True)
	call("service network-manager start", shell=True)
def checkPyshark():
	try:
		import pyshark
	except:
		call("pip install pyshark", shell=True)
		import pyshark
def help():
	helpDict = {'-h': 'Help', 
		'-r': 'Stop airmon-ng wlan0mon + start network-service',
		'-s': 'Start airmon-ng wlan0',
		'-s': 'Start airmon-ng wlan0, run Tshark',
		'-ch #': 'Set channel hop interval [ms] (TODO)'}
	print("Command : function") 
	for key, val in helpDict.iteritems():
		print(key + ": " + val)
def runTshark():
	checkPyshark()
	import pyshark
	import trollius as asyncio
	a =  packageFiltered()
	try:
		capture = pyshark.LiveCapture(interface='wlan0mon', only_summaries=True)
		print(capture.interfaces)
		while (1):
			for packet in capture.sniff_continuously(packet_count=1000):
				print("Packet: " + str(packet))
#		for packet in capture.sniff_continuously(packet_count=50):
#			print 'Just arrived... ' + str(packet['radiotap'].wlan)
	except Exception as e:
		print("wlan0mon excepted " + str(e))

class packageFiltered:
	def packagefiltered():
		print "Constructor"
