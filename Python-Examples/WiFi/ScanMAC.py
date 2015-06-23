#!/usr/bin/env python

"""
ScanMAC.py

This example shows how to check the MAC for the available networks.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	02-23-2015	Example created
Diego Villalobos	06-23-2015	Minor details added
"""

# Libraries required
import os
import time

# Color class for output messages
class text_colors:
	RED 	= '\033[91m'
	GREEN 	= '\033[92m'
	YELLOW 	= '\033[93m'
	BLUE  	= '\033[94m'
	MAGENTA = '\033[95m'
	CYAN 	= '\033[96m'
	END 	= '\033[0m'

def main():
	# Network information
	networkAddress = []
	networkSSID = []

	os.system("clear")
	print text_colors.CYAN + "ScanMAC.py" + text_colors.END
	
	# Enable 'wlan0' interface
	os.system('ifconfig wlan0 up')
	time.sleep(1)

	print ""
	print text_colors.GREEN + "Scanning..." + text_colors.END
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
		if "Address" in line:
			networkAddress.append(line[line.find('Address:')+9:len(line)-1])
		elif "ESSID" in line:
			networkSSID.append(line[line.find('ESSID:')+7:len(line)-2])

	# Print the information
	print "Networks available: " + text_colors.MAGENTA + str(len(networkAddress)) + text_colors.END
	for network in range(0,len(networkAddress)):
		print "-----------------------------------"
		print "SSID: \t " + text_colors.YELLOW + networkSSID[network] + text_colors.END
		print "Address: " + text_colors.YELLOW + networkAddress[network] + text_colors.END
		
	print ""

if __name__ == "__main__":
      main()
