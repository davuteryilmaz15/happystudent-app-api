import smtplib
import ssl
from email.mime.text import MIMEText
from django.conf import settings

def send_mail_via_gmail_smtp(to_addr, message):
    # send email

    # gmail sender email address and password.
    from_addr = settings.SMTP_EMAIL.from_addr
    from_addr_password = settings.SMTP_EMAIL.from_addr_password

    # create MIMEText object which represent the email message.
    msg = MIMEText(message, 'html', 'utf-8')
    # set email message from, to and subject attribute value.
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Email Activation'

    # create a ssl context object because gmail need ssl access.
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=None, capath=None, cadata=None)
    # start ssl encryption from very beginning.
    #print('starting connect gmail smtp server with ssl.')
    # smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ctx)
    # create SMTP connection object.
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    # start tls to make the connection secure.
    smtp_server.starttls(context=ctx)
    #print('start login gmail smtp server.')
    smtp_server.login(from_addr, from_addr_password)
    #print('start send message through gmail service.')
    smtp_server.send_message(msg, from_addr, to_addr)
    #print('Send email by python smtplib module through gmail smtp service complete.')