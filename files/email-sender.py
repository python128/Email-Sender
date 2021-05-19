#Windows
import smtplib #For sending mails
import os #Clearing screen

def send_mail():
    sender = input('From(mail): ')
    reciever = input('To(mail): ')
    mail_text = input('Message: ')
    PWD = input('Password(Keep in mind after this, it will clear the screen): ')
    os.system('clear')
    
    #This is for gmail, if you have some other, say outlook, change to smtp.outlook.com
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo() #Encryption 
    server.starttls()
    server.ehlo() #Second Encryption
    print('Encrypted!')
    server.login(sender, PWD)
    print('Login Success!')
    server.sendmail(sender,
                    reciever,
                    mail_text
                    )
    print('Email is being sent to ' + str(reciever))

send_mail()
print('Mail sent!')
