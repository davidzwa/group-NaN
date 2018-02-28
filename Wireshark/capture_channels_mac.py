# from subprocess import call, Popen, CREATE_NEW_PROCESS_GROUP
import time
import subprocess
import os
# import pyshark
# output = call('')
# print(output)

# log_file = 'tmp.txt'
for channel in range(1, 14):
	with open('tmp.txt', 'w') as log_file:
		proc = subprocess.Popen([
				'/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport en0 sniff ' + str(channel)
			],
			shell=True,
			stdout=log_file,
			stderr=log_file,
			close_fds=True)
		time.sleep(2)
		proc.send_signal(2)
		while proc.poll() is None:
			time.sleep(0.0001)

	with open('tmp.txt', 'r') as log_file:
		lines = log_file.readlines()
		file = lines[1][17:-2]
		print(file)
		os.rename(file, './captures/channel_' + str(channel) + '.cap')

		# log_file.close()
# for channel in range(1, 14):
# 	pyshark.ope