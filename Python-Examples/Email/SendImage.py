#!/usr/bin/env python

"""
SendImage.py

This example shows how to send an image by email.

This example code is in the public domain.

Revision History
----------------------------------------------------------
    Author		   Date		  Description
----------------------------------------------------------
Diego Villalobos	01-29-2015	Example created

"""

# Libraries required
import smtplib

from email.mime.image import MIMEImage
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

# Set the image name that will be attached to the email
image2attach = "image.jpg"

# Building the message
message = MIMEMultipart()
message['From'] = emailSender
message['To'] = emailReceiver
message['Subject'] = "Email sent by Edison"

# Create the content in HTML format
text = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       This is an email sent by Edison.<br>
       There is an attached image to this email. Don't forget to check it.<br>
    </p>
  </body>
</html>
"""

# Open the image file
try:
    print "Searching image..."
    imageFile = open(image2attach, 'rb')
except:
    print "Error. Image not found."
    exit()
else:
    image = MIMEImage(imageFile.read())
    imageFile.close()
    print "Image found." 

# Attach the text and the image to the message
htmlText = MIMEText(text, "html")

message.attach(htmlText)
message.attach(image)

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
