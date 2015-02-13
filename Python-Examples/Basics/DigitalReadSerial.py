"""
DigitalReadSerial.py
This example reads a digital input on pin 2, prints the result 
 
This example code is in the public domain.

Revision History
------------------------------------------------
Author			  Date			  Description
------------------------------------------------
Carlos Mata			1-29-2015		Example created
"""

import mraa #calls the MRAA library
import time #calls the time library

#Setup of variable and conditions
pushButton = mraa.Gpio(2)   #We are going to read values on pin 2
pushButton.dir(mraa.DIR_IN) #Defines the pin functionality as an input

try:
	while True:
		pushButton.read()    #Reads the pin
		if pushButton.read() == 1:     
			print "pushButton is High"     #Only when the pin is HIGH will print something
		time.sleep(0.5)      #Waits 500ms to read again.
except KeyboardInterrupt:
	print ""
