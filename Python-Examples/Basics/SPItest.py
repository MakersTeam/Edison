"""
SPItest.py
This example test the functionality of SPI to check the writing process
Using the Arduino Expansion Board:
SCLK = Pin 13
MISO = Pin 12
MOSI = Pin 11
EN = Pin 10

This example code is in the public domain.

Revision History
------------------------------------------------
Author			  Date			  Description
------------------------------------------------
Carlos Mata			1-29-2015		Example created
Carlos Mata                     3-18-2015               Last Modification
"""

import time
import mraa

spi= mraa.Spi(0)
#buff = bytearray('\x02\xee\x10')
try:
        while True:
                spi.writeByte(0x12)
                spi.writeByte(0x35)
                #spi.write(buff)
except KeyboardInterrupt:
        print ""
