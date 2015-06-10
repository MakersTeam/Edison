#!/usr/bin/env python

"""
SendSimpleText.py

This example shows how to send a simple text by email.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	01-29-2015	Example created
Diego Villalobos	06-09-2015	Minor details added
"""

# Libraries required
import os
import smtplib
from email.mime.text import MIMEText
import getpass

# Color class for output messages
class text_colors:
	RED 	= '\033[91m'
	GREEN 	= '\033[92m'
	YELLOW 	= '\033[93m'
	BLUE  	= '\033[94m'
	MAGENTA = '\033[95m'
	CYAN 	= '\033[96m'
	END 	= '\033[0m'

#Set the local host to use
"""
If you want to send emails from a Google account
use as local host: smtp.gmail.com
If you want you send emails from a Hotmail account
use as local host: smtp.live.com
The local host will be selected properly once the user
enter the sender email.
"""
localHost = ""
	
def enter_credentials():
	print ""
	print text_colors.GREEN + "Provide the sender (password) and receiver email address." + text_colors.END
	print ""
	print text_colors.YELLOW + "Note: Currently the email can be sent only from gmail and hotmail accounts." + text_colors.END
	
	while True:
		print ""
		emailSender = raw_input("Email sender: ")
		if "@gmail." in emailSender:
			localHost = "smtp.gmail.com"
			break
		elif "@hotmail." in emailSender or "@live." in emailSender:
			localHost = "smtp.live.com"
			break
		else:
			print ""
			print text_colors.RED + "Error: The email entered is not validated. It has to be a gmail or hotmail account." + text_colors.END
			
	password = getpass.getpass(prompt="Password: ")
	
	emailReceiver = raw_input("Email receiver: ")
	
	return emailSender, password, emailReceiver, localHost
	
def build_message():
	print ""
	print text_colors.GREEN + "Build the email's content." + text_colors.END
	print ""
	
	emailSubject = raw_input("Email subject: ")
	emailContent = raw_input("Email content: ")
	
	return MIMEText(emailContent), emailSubject

def send_email():
	global emailSender, password, emailReceiver, localHost, message
	
	# Try to connect to the SMTP Server
	try:
		print ""
		print text_colors.GREEN + "Connecting to SMTP Server..." + text_colors.END
		
		mailServer = smtplib.SMTP(localHost,587)
		mailServer.starttls()
		mailServer.login(emailSender,password)
		
	except smtplib.SMTPAuthenticationError:
		print ""
		print text_colors.RED + "Authentication Error. Can't login." + text_colors.END
		mailServer.quit()
		exit()
		
	except:
		print ""
		print text_colors.RED + "Error. Can't connect to the SMTP Server." + text_colors.END
		exit()

	else:
		print ""
		print text_colors.GREEN + "Login successfully." + text_colors.END

	# Try to send the email
	try:
		print ""
		print text_colors.GREEN + "Sending email..." + text_colors.END
		mailServer.sendmail(emailSender,emailReceiver,message.as_string())
		
	except:
		print ""
		print text_colors.RED + "Error. The email couldn't be sent." + text_colors.END
		
	else:
		print ""
		print text_colors.GREEN + "Email sent successfully." + text_colors.END
		
	finally:
		mailServer.quit()
		exit()

def main():
	global emailSender, password, emailReceiver, localHost, message
	
	os.system("clear")
	print text_colors.CYAN + "SendSimpleText.py" + text_colors.END
	
	# Asks for the credentials prior to send the email
	emailSender, password, emailReceiver, localHost = enter_credentials()
	
	# Asks for the email's content
	message, message['Subject'] = build_message()
	message['From'] = emailSender
	message['To'] = emailReceiver
	
	# Sends the email
	send_email()

if __name__ == "__main__":
      main()
