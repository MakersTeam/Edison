"""
Fade.py
This example shows how to use PWM in order to modify the brightness in a LED

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
Brightness = 0.0
FadeAmount = 0.01
LED = mraa.Pwm(3)  #We are going to use pin 3 in the Arduino Expansion Board
#LED.dir(mraa.DIR_OUT)
LED.enable(True)
LED.period_us(700)
value = 0.0

try:
	while True:
		LED.write(Brightness)
		Brightness = Brightness + FadeAmount
		if ((Brightness >=  1.0) or (Brightness <= 0.0)): #Use numbers between 0.0 and 1.0, they are respective to 0% and 100%
			FadeAmount = -1 * FadeAmount
		time.sleep(0.03)

except KeyboardInterrupt:
        print ""
