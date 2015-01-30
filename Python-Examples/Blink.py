"""
Blink.py
This example makes a LED blink every second. It uses the Python programming language
and the MRAA library.

This example code is in the public domain.

Revision History
------------------------------------------------
Author			  Date			  Description
------------------------------------------------
Carlos Mata			1-22-2015		Example created
"""

import mraa #calls the MRAA library
import time #calls the time library

#Setup - Allows to choose the pin 13 (Built-in LED) as an output.

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)

#Process - The process is going to change the state of the pin every second

try:
	print "It's blinking"
	while True:
		x.write(1)
		time.sleep(1)  #Maintain the status of the pin for a second
		x.write(0)
		time.sleep(1)
except KeyboardInterrupt:
        print ""
