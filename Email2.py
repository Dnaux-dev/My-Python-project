
from email.message import EmailMessage
import smtplib
import os
import ssl
username = os.environ.get('email')
password = os.environ.get('psw')


email_sender = 'ajiloredaniel33@gmail.com'
email_password = 'aizzapbocyqbauzt'
email_receiver = 'adeoyesamuel100@gmail.com'

subject = 'Check out my python email'
body = """
I've just sent you an email with python code
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("email sent!")
