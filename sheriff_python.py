# sheriff_python.py
import psutil

# Define the name of the process to check for
process_name = "suspect_process"

# Check if the process is running
for process in psutil.process_iter(["pid", "name"]):
    if process.info["name"] == process_name:
        # The process is running, so get a list of its open file handles
        file_handles = process.open_files()
        for handle in file_handles:
            # Check if the file handle is being deleted
            if handle.mode == "wb" and handle.closed:
                print(f"Process {process.info['pid']} is deleting {handle.path}")
                # Kill the process
                process.kill()
