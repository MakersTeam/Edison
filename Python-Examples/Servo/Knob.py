#!/usr/bin/env python

"""
Knob.py

This example shows how to use a servo motor attached
to a PWM pin through a potentiometer.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	02-12-2015	Example created

"""

# Libraries required
from Servo import *
import mraa
import time

# Create a new servo object with a reference name
myServo = Servo("First Servo")

# Attaches the servo to pin 3 in Arduino Expansion board
myServo.attach(3)

# Attaches the potentiometer to analog input A0
# in Arduino Expansion Board
pot = mraa.Aio(0)
pot.setBit(12)
valuePot = 0

# Print servo settings
print ""
print "*** Servo Initial Settings ***"
print myServo
print ""

print "Move the knob."
print ""

try:
    # Move the servo using the potentiometer
    while True:
        # Read the analog value from pot
        valuePot = pot.read()

        # mapValue() is in the Servo library
        angle = mapValue(valuePot, 0, 4096, 0, 180)

        # Write the angle
        myServo.write(angle)
        time.sleep(0.005)
            
except KeyboardInterrupt:
        print "Knob ended."
