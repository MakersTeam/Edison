#!/usr/bin/env python

"""
ScanMAC.py

This example shows how to check the MAC for the networks available.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	02-23-2015	Example created

"""

# Library required
import os
import time

# Variables needed
numNetworks = 0
networkAddress = []
networkSSID = []

# Auxiliary variables
index = 0
ssid = ""

# Enable 'wlan0' interface
os.system('ifconfig wlan0 up')
time.sleep(1)

print ""
print "Scanning..."
print ""

# Run the command 'iwlist' and save the output for 'wlan0 scan'
# in the file 'Scan_Record.txt'
os.system('iwlist wlan0 scan > Scan_Record.txt')

# Open the file just created, read its content, and then erase it.
Scan_Record_file = open('Scan_Record.txt', "r")
content = Scan_Record_file.readlines()
os.system('rm Scan_Record.txt')

# Check the content line by line
for line in content:
    if line[20:27] == "Address":
        numNetworks += 1
        networkAddress.append(line[29:46])
    elif line[20:25] == "ESSID":
        index = 27
        while line[index] != '"':
            ssid += line[index]
            index += 1
        networkSSID.append(ssid)
        ssid = ""

# Print the information
print "Networks available: " + str(numNetworks)
for network in range(0,numNetworks):
    print "-----------------------------------"
    print "SSID: " + networkSSID[network]
    print "Address: " + networkAddress[network]
    
print ""
