#!/usr/bin/env python

"""

BoardDetector.py

This example recognizes the expansion board where the Intel Edison module is.
The board could be the Arduino Expansion Board or the Mini-Breakout Board.

This example code is in the public domain.

Revision History

----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	09-24-2015	Example created

"""

import os

BOARD = "???"

class text_colors:
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	BLUE  = '\033[94m'
	MAGENTA = '\033[95m'
	CYAN = '\033[96m'
	END = '\033[0m'

def checkPlatform():
	"""
	Returns the board used. If the board is not the Arduino Expansion Board
	we assume the board is the Mini-Breakout Board.
	"""
	os.system("echo 214 > /sys/class/gpio/export 2> tmp_log.txt")
	f = open('tmp_log.txt', "r")
	content = f.readline()
	os.system('rm tmp_log.txt')
	
	if "No such device" in content:
		return "MINIBOARD"
	else:
		return "ARDUINOBOARD"

def main():
	global BOARD
	
	# Make sure which board is currently used
	BOARD = checkPlatform()
	
	if BOARD == "ARDUINOBOARD":
                print text_colors.CYAN + "Arduino Expansion Board Detected" + text_colors.END
	else:
		print text_colors.YELLOW + "Mini-Breakout Board Detected" + text_colors.END

if __name__ == "__main__":
      main()
      
