"""
I2Ctest.py
This example test the functionality of I2C to check the writing process
Using the Arduino Expansion Board:
SCL = Pin A5
SDA = Pin A4

This example code is in the public domain.

Revision History
------------------------------------------------
Author			  Date			  Description
------------------------------------------------
Carlos Mata			1-29-2015		Example created
"""

import mraa
x = mraa.I2c(0) #Initialization of I2C
x.address(4) #Address of the device

try:
        while True:
                x.writeByte(0x30)       
                x.writeReg(0x01, 0x50)
except KeyboardInterrupt:
        print ""
