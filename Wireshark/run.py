import sys
from func import *
from subprocess import call
program = "[run.py]: "

if len(sys.argv) > 0:
	if len(sys.argv) > 1:
		if sys.argv[1] == '-r':
			print(program + "Resetting airmon-ng.")
			reset()
			exit()
		elif sys.argv[1] == '-h':
			help()
			exit()
		elif sys.argv[1] == '-c' and len(sys.argv) >= 3:
			try:
				if int(sys.argv[2]):
					print(program+ "Setting airmon, running Tshark on channel " + str(int(sys.argv[2])))
					set(sys.argv[2])
				else:
					set(0)			
			except Exception as e:
				print(str(e))
		else:
			print(program+ "Didn't recognize command. Setting airmon, running Tshark.")
			set(0)
	else:
		set(0)		
runTshark()



