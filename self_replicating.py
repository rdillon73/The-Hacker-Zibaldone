# simple example of self replicating code in python. 
# HANDLE WITH CARE! 

# self_replicating.py

import os
import datetime

def replicate():
	# Open the current file and save its contents
	with open(__file__, 'r') as f:
		code = f.read()
	
	# get the current timestamp to create a unique name
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
	file_name = "replica.py"
	replica = f"{timestamp}_{file_name}"

	# then copy code to a new file 
	with open(replica, 'w') as f:
		f.write(code)

	# Run the newly created replica to repeat the process for ever
	# os.system('python3 .\'' + replica)


if __name__ == '__main__':
replicate()