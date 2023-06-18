#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('cls', shell=True)

# Ask for input
try:
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)
except socket.gaierror as err:
    print(f"Hostname {remoteServer} could not be resolved! with error {err}")
    sys.exit()


# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()
# Using the range function to specify ports
try:
    for port in range(1,1024):
        timeout = 0.5
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print (f"Port {format(port)} is Open")
        sock.close()

except socket.error as e:
    print(f"Could not connect to remote server! due to error {e}")
    sys.exit()
except KeyboardInterrupt:
    print("\n You pressed Ctrl+C. \n Exiting Program!")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)