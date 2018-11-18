from gtts import gTTS
import speech_recognition as sr
import os
import time 
import webbrowser

def talk(audio):
	tts=gTTS(text=audio,lang ="en" )
	tts.save("file1.mp3")
	os.system("start file1.mp3")
	
def listenForCmd():

	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		print("Hello. i am SASHA. i'm online and ready")
		r.adjust_for_ambient_noise(source, duration = 1)
		audio = r.listen(source)
		
	try:
		command = r.recognize_google(audio)
		print(command)
	
	except sr.UnknownValueError:
		print("the mic isnt working right... i didnt hear any command")
		command =listenForCmd()
		
	return command
	
command = listenForCmd()

def cmd():
	if "hey" in command:
		os.system('start sounds/Bidding.mp3')

talk("ready when you are")

while True:
	listenForCmd()
	cmd()
	time.sleep(3)
