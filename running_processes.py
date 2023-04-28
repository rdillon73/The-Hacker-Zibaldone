# runnin_processes.py

import psutil

# Get a list of all running processes
processes = psutil.process_iter()

# Loop through the list and print the process name and ID
for process in processes:
    try:
        # Get process details
        process_name = process.name()
        process_id = process.pid

        # Print process details
        print(f"Process name: {process_name} - Process ID: {process_id}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Ignore any processes that can't be accessed or don't exist
        pass
