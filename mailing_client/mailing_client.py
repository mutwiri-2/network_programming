import smtplib
import os
from pathlib import Path

from email import encoders
from email.mime.text import MIMEText # for text in the mail
from email.mime.base import MIMEBase # for attachments
from email.mime.multipart import MIMEMultipart # for the whole thing


# define a server
server = smtplib.SMTP(host='smtp.gmail.com', port=25)

# Identify yourself to the ESMTP server
server.ehlo()

# login to an existing gmail account
file_path = os.path.dirname(__file__) # get the path of the running file
with open((Path(file_path) / 'login_details.txt'), 'r') as f:
    email = f.readline().rstrip()
    password = f.readline()

server.login(email, password) # have less secure apps allowed to login to your account on Google settings

# compose email
msg = MIMEMultipart()

# define message header
msg['From'] = 'John Doe'
msg['To'] = 'mail@gmail.com'
msg['Subject'] = 'Just a Test'

# load text message
with open((Path(file_path) / 'message.txt'), 'r') as f:
    message = f.read()

# attach text message to the msg object
msg.attach(MIMEText(message, 'plain'))