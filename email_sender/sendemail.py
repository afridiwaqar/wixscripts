# Import smtplib for our actual email sending function
import smtplib
import csv


# Helper email modules 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# sender email address
email_user = ''
print(email_user) 
# sender email passowrd for login purposes
email_password = ''

# list of users to whom email is to be sent
#email_send = ['afridi.waqar@gmail.com']
subject = 'Subject'
msg = MIMEMultipart()

msg['From'] = email_user

# converting list of recipients into comma separated string

#msg['To'] = ", ".join(email_send)
#msg['Subject'] = subject

#msg.attach(MIMEText(body,'plain'))
#text = msg.as_string()

a = server = smtplib.SMTP('smtp.gmail.com',587)
print(a)

b = server.starttls()
print(b)

c = server.login(email_user,email_password)
print(c)

with open('User_IMSciences.csv', 'r') as file:
	reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
	for row in reader:
		msg['To'] = (str(row[2]))
		msg['Subject'] = subject
		print(str(row[2]))
		body = """
		
		Email Body Goes here
		
		Regards
		Waqar Afridi
		       """
		msg.attach(MIMEText(body,'plain'))
		text = msg.as_string()
		server.sendmail(email_user,str(row[2]),text)
server.quit()
