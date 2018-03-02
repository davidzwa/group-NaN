import sys
from func import *
from subprocess import call
program = "[run.py]: "
channel = -1
hop = True	# Set this True with -c flag

if len(sys.argv) > 0:
	if len(sys.argv) > 1:
		if sys.argv[1] == '-r':
			print(program + "Resetting airmon-ng, restarting network service.")
			reset()
			exit()
		elif sys.argv[1] == '-s':
			print(program + "Resetting airmon-ng.")
			stop()
		elif sys.argv[1] == '-h':
			help()
			exit()
		elif sys.argv[1] == '-ch' and len(sys.argv) >= 3:
			try:
				if int(sys.argv[2]):
					channel = sys.argv[2]
				else:
					channel = 0
			except Exception as e:
				print(str(e))
		else:
			print(program+ "Didn't recognize command " + sys.argv[1])
			channel = 0
	else:
			channel = 0

# Check required package (requirements?)
checkPyshark()

if not hop:
	print(program+ "Setting airmon, running Tshark with channel " + str(channel))
	set(channel)
else:
	print(program+ "Setting airmon, running Tshark with hopper.")	
	set(0)

from capture import runTshark
runTshark()
#reset()
