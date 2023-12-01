## Import necessary modules
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application
import os

## Initiate email sending and send email 
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
s = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
s.login(os.environ['my_email'], os.environ['SMTP_pass'])


msg = MIMEMultipart()
msg['Subject'] = 'New Employee Details'
msg['From'] = os.environ['my_email']
msg['To'] = os.environ['it_admin_mail']

txt = MIMEText('Attached is a json with the new employee details. \nKindly provision a user account and other necessary resources')
msg.attach(txt)

filename = 'employee_json.json'
fo=open(filename,'rb')
attach = email.mime.application.MIMEApplication(fo.read(),_subtype="json")
fo.close()
attach.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(attach)
s.send_message(msg)
print("Email sent succesfully")
s.quit()