import sys
from func import *
from subprocess import call
from capture import runTshark
program = "[run.py]: "
channel = -1

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
		elif sys.argv[1] == '-c' and len(sys.argv) >= 3:
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

print(program+ "Setting airmon, running Tshark on channel " + str(channel))
set(channel)
runTshark()

reset()
