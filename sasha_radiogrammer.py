import speech_recognition as sr
import os
import time 
import webbrowser
import winspeech 
import simpleaudio as sa
import pygame
from pygame import mixer
import smtplib
import emailConfig

def talk(audio):
	winspeech.say(audio)

contacts= {
			"grandma": "NeedsEmail@yahoo.com"
		}
recipient = []	
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
		#time.sleep(5)
		print("the mic isnt working right... i didnt hear any command")
		command = listenForCmd()
		
	return command
#The pitch was controlled by the freqency argument in mixer.init(). So I just set that higher
def email(toAddr,subject,msg):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(emailConfig.EMAIL_UN,emailConfig.EMAIL_PW)
		message =listenForCmd().format(subject,msg)
		print(message)
		print("sent it on over")
		server.sendmail(emailConfig.EMAIL_UN,toAddr,message)
		server.quit()
		talk('message sent as requested')
	except:
		talk("transfer unsuccessful")
		
def cmd(command): #function for playing user's commands
	

	if "what up" in command:
		mixer.init()
		mixer.music.load("C:/Users/wolfp/Desktop/Sasha/modified/sounds/Bidding.mp3")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(10)
	

	elif "defeated by victory" in command:
		mixer.init(frequency = 30000)
		mixer.music.load("C:/Users/wolfp/Desktop/Sasha/modified/sounds/defeated_by_victory.ogg")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(10)

		
	elif "shakespeare" in command:
		mixer.init(frequency = 30000)
		mixer.music.load("C:/Users/wolfp/Desktop/Sasha/modified/sounds/shakespeare (1).ogg")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(13)
		
		
	elif "you're weird" in command:
		mixer.init()
		mixer.music.load("C:/Users/wolfp/Desktop/Sasha/modified/sounds/eatmyshorts.wav")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(1)
	
	elif "email" in command:
		talk(" who is recieving this")
		toAddr = listenForCmd()
		#if "grandma" in toAddr:
		#recipient.append(contacts[toAddr])
		talk("subject please")
		subject=listenForCmd()
		talk("what is the message")
		msg=listenForCmd()
		email(contacts,subject,msg)
		
	elif 'listen here' in command: 
		mixer.init(frequency = 30000)
		mixer.music.load("C:/Users/wolfp/Desktop/Sasha/modified/sounds/listening.mp3")
		mixer.music.play()
		while mixer.music.get_busy():
			pygame.time.Clock().tick(1)

		#mixer.quit()
	
	elif "stop" in command:
		quit()
	mixer.quit()
talk("ready when you are")

while True:
	cmd(listenForCmd())
