"""
AnalogReadSerial.py
This example reads an analog input on pin 0, prints the result from the ADC buffer and converts it 
to a decimal value to represent the voltage in the pin.

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
DecimalValue = 0.0  #Initialization of value converted
ADCValue = 0.0      #Initialization of value to be read
x = mraa.Aio(0)     #We are going to use pin A0 in the Arduino Expansion Board

try:
	while True:
		x.setBit(12)         #Use 12 bits of the ADC
		ADCValue = x.read()  
		DecimalValue = ADCValue/819.0 #Conversion to a Decimal Value
		print "ADCValue = ", ADCValue,"\t DecimalValue =", DecimalValue
		time.sleep(1)   #Wait a second and read again the ADC buffer
except KeyboardInterrupt:
        print ""
