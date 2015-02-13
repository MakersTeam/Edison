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

"""

# Libraries required
import smtplib

from email.mime.text import MIMEText

#Set the local host to use
"""
If you want to send emails from a Google account
use as local host: smtp.gmail.com

If you want yo send emails from a Hotmail account
use as local host: smtp.live.com
"""
localHost = "smtp.gmail.com"

# Set the sender credentials
emailSender = "sender@gmail.com"
password = "password"

# Set the receiver email
emailReceiver = "receiver@domain.com"

# Building the message
message = MIMEText("This is an email text sent by Edison!")
message['From'] = emailSender
message['To'] = emailReceiver
message['Subject'] = "Email sent by Edison"

# Try to connect to the SMTP Server
try:
    print "Connecting to SMTP Server..."
    mailServer = smtplib.SMTP(localHost,587)
    mailServer.starttls()
    mailServer.login(emailSender,password)
    
except smtplib.SMTPAuthenticationError:
    print "Authentication Error. Can't login."
    mailServer.quit()
    exit()
    
except:
    print "Error. Can't connect to the SMTP Server."
    exit()

else:
    print "Login successfully."

# Try to send the email
try:
    print "Sending email..."
    mailServer.sendmail(emailSender,emailReceiver,message.as_string())
    
except:
    print "Error. The email couldn't be sent."
    
else:
    print "Email sent successfully."
    
finally:
    mailServer.quit()
    exit()
