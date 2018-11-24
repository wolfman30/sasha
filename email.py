import smtplib
from sasha import talk, listenForCmd

def send_email(command):
    
    email_whoever = {
					 'email grandma':['full name', 'email@host.com'], 
					 'email dad':['full name', 'email@host.com'], 
					 'email justin':['Justin Livingston', 'email@host.com']
	                }

    try: 
        if command in email_whoever.keys():
            
            #Connect to smtp.gmail.com on port 465, if you're using SSL. 
            #Connect on port 587 if you're using TLS. 
            mail = smtplib.SMTP(host='smtp.gmail', port=587)
            
            talk('What is the subject?')
            subject = listenForCmd()

            talk('What do you want to say?')
            msg = listenForCmd()

            message = "Subject: {}  {}".format(subject, msg)

            #identify to server
            mail.ehlo() 
            #encrypt session
            mail.starttls()

            #login
            mail.login('YourEmail@gmail.com', 'password')

            #send message contained in variable msg
            mail.sendmail(yourEmailAdress@gmail.com, email_whoever[command][0], message)

            #close mail connection
            mail.close()

            talk('Email sent successfully.')

    except:
        talk('sorry, I did not get that')