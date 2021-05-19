import smtplib
from PWD import *

def send_mail():
    sender = input('From: ')
    reciever = input('To: ')
    mail_text = input('Message: ')
    
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.ehlo()
    print('Encrypted!')
    server.login(sender, pwdT)
    print('Login Success!')
    server.sendmail(sender,
                    reciever,
                    mail_text
                    )
    print('Email is being sent to ' + str(reciever))

send_mail()
print('Mail sent!')
