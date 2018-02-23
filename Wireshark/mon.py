import sys
from func import *
from subprocess import call
program = "[Mon.py]:"

if len(sys.argv) > 0:
	if len(sys.argv) > 1:
		if sys.argv[1] == '-r':
			reset()
			exit()
		elif sys.argv[1] == '-s':
			print("Setting airmon-ng")
			set()
			exit()
		elif sys.argv[1] == '-h':
			help()
			exit()
		elif sys.argv[1] == '-T':
			print("Running Tshark")
			runTshark()
		elif sys.argv[1] == '-sT':
			print("Setting airmon, running Tshark")
			if len(sys.argv) >= 2:
				set(sys.argv[2])
			else:
				set(0)
			runTshark()
		else:
			reset()
			exit(program + " No recognized command given. Assumed reset. Give -h for help.")
	else:
		reset()
		exit(program + " No recognized command given. Assumed reset. Give -h for help.")



