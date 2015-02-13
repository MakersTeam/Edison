#!/usr/bin/env python

"""
SendHTMLText.py

This example shows how to send a text in HTML and plain format by email.

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
message = MIMEMultipart()
message['From'] = emailSender
message['To'] = emailReceiver
message['Subject'] = "Email sent by Edison"

# Create the content in HTML and plain text
plain = "Hi!\nThis is an email sent by Edison.\nHere is an interesting link that you can visit:\nhttps://communities.intel.com/community/makers/edison/"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       This is an email sent by Edison.<br>
       Here is an interesting <a href="https://communities.intel.com/community/makers/edison/">link</a> that you can visit.
    </p>
  </body>
</html>
"""

# Attach both types of text to the message
plainText = MIMEText(plain, "plain")
htmlText = MIMEText(html, "html")

message.attach(plainText)
message.attach(htmlText)

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
