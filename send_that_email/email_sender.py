import smtplib
import speech_recognition as sr
import winspeech

def talk(audio):
	winspeech.say(audio)
	
def listenForCmd():

	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		print("Hello. i am SASHA. i'm online and ready")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration = 1)
		audio = r.listen(source)
		
	try:
		command = r.recognize_google(audio).lower()
		print("Your command:", command)
	
	except sr.UnknownValueError:
		print("the mic isnt working right... i didnt hear any command")
		command = listenForCmd()
		
	return command

def sender(command):

    if 'email' in command:
        
        talk('What is the subject?')
        subject = listenForCmd()

        talk('What do you want to say?')
        msg = listenForCmd()

        message = "Subject: {}  {}".format(subject, msg)
        
        print(message)

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        
        #identify to server
        mail.ehlo() 
        
        #encrypt session
        mail.starttls()

        #login
        mail.login('Username (not email)', 'Your_Password')

        #send message contained in variable msg
        mail.sendmail('Recipient_First_Name Recipient_Last_Name', 'recipient@email.com', message)

        #close mail connection
        mail.close()

        talk('Email sent successfully.')

    else:
        talk('sorry, I did not get that')

if __name__ == '__main__':

    sender(listenForCmd())
