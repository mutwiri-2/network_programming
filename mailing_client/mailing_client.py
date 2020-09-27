import smtplib
import os
from pathlib import Path

# define a server
server = smtplib.SMTP(host='smtp.gmail.com', port=25)

# Identify yourself to the ESMTP server
server.ehlo()

# login to an existing gmail account
file_path = os.path.dirname(__file__) # get the path of the running file
with open((Path(file_path) / 'login_details.txt'), 'r') as f:
    email = f.readline().rstrip()
    password = f.readline()

server.login(email, password)