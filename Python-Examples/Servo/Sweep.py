#!/usr/bin/env python

"""
Sweep.py

This example shows how to use a servo motor attached to a PWM pin.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	02-12-2015	Example created

"""

# Libraries required
from Servo import *
import time

# Create a new servo object with a reference name
myServo = Servo("First Servo")

# Attaches the servo to pin 3 in Arduino Expansion board
myServo.attach(3)

# Print servo settings
print ""
print "*** Servo Initial Settings ***"
print myServo
print ""

try:
    # Sweeps the servo motor forever
    while True:
        # From 0 to 180 degrees
        for angle in range(0,180):
            myServo.write(angle)
            time.sleep(0.005)

        # From 180 to 0 degrees
        for angle in range(180,-1,-1):
            myServo.write(angle)
            time.sleep(0.005)
            
except KeyboardInterrupt:
        print "Sweep ended."
