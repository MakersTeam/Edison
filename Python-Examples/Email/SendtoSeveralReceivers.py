#!/usr/bin/env python

"""
SendtoSeveralReceivers.py

This example shows how to send an email to several receivers using HTML text format.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	01-29-2015	Example created

"""

# Libraries required
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

COMMASPACE = ', ' # Use this to concatenate all the receivers spaced by a comma.

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
emailReceiverList = ["receiver1@domain.com",
                     "receiver2@domain.com",
                     "receiver3@domain.com"]

# Building the message
message = MIMEMultipart()
message['From'] = emailSender
message['To'] = COMMASPACE.join(emailReceiverList)
message['Subject'] = "Email sent by Edison"

# Create the content in HTML
text = """\
<html>
  <head></head>
  <body>
    <p>Hi all!<br>
       This is an email sent by Edison to several receivers.<br>
       Here is an interesting <a href="https://communities.intel.com/community/makers/edison/">link</a> that all of you can visit.
    </p>
  </body>
</html>
"""

# Attach the text to the message
contentText = MIMEText(text, "html")

message.attach(contentText)

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
    mailServer.sendmail(emailSender,emailReceiverList,message.as_string())
    
except:
    print "Error. The email couldn't be sent."
    
else:
    print "Email sent successfully."
    
finally:
    mailServer.quit()
    exit()
