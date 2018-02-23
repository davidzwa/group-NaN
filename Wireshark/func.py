from subprocess import call
program = "[func.py]: "

def set(channel=0):
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
		try:
			call("sudo pip install --no-index --find-links ./pip pyshark", shell=True)
			import pyshark
		except:
			print program + "Attempting downloading pyshark. If this fails, check connection."
			try:
				call("mkdir pip", shell=True)
				call("sudo pip install --download ./pip pyshark", shell=True)
			except:
				exit("Pyshark pip-package download not succesful. Try and download it again.")
		
def help():
	helpDict = {'-h': 'Help', 
		'-r': 'Stop airmon-ng wlan0mon + start network-service.',
		'-s': 'Stop airmon-ng wlan0mon.',
		'-c #': 'Set channel to sniff.',
		'-ch #': 'Set channel hop interval [ms] (TODO).'}
	print("Command : function") 
	for key, val in helpDict.iteritems():
		print(key + ": " + val)
