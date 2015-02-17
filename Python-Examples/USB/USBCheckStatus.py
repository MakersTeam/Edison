#!/usr/bin/env python

"""
USBCheckStatus.py

This example shows how to check the USB OTG connection status.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	02-17-2015	Example created

"""

# Library required
import os

# Connection status flag
status = False

# Runs the command 'dmesg' and save the output for USB OTG related messages
# in the file 'USB_Records.txt'
os.system('dmesg | grep "Notifying OTG driver" > USB_Record.txt')

# Opens the file created, read its content, and then erase it.
USB_Record_file = open('USB_Record.txt', "r")
content = USB_Record_file.readlines()
os.system('rm USB_Record.txt')

# Check the content line by line
for line in content:
    if "Detected" in line:
        status = True
    elif "Removed" in line:
        status = False

# Print an output message
if status:
    print "The USB OTG cable is connected."
else:
    print "The USB OTG cable is unconnected."
