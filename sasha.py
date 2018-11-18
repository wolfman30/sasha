#from gtts import gTTS
import speech_recognition as sr
import os
import time 
import webbrowser
import winspeech 
import simpleaudio as sa

def talk(audio):
	#tts=gTTS(text=audio,lang ="en" )
	#tts.save("file1.mp3")
	#os.system("start file1.mp3")
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
		time.sleep(5)
		print("the mic isnt working right... i didnt hear any command")
		command =listenForCmd()
		
	return command
	
#command = listenForCmd()

def cmd(command):
	if "sasha" in command:
		os.system('start sounds/Bidding.mp3')
		
	elif "you're weird" in command:
		wave_obj = sa.WaveObject.from_wave_file("C:/Users/wolfp/Desktop/Sasha/modified/sounds/eatmyshorts.wav")
		play_obj = wave_obj.play()
		play_obj.wait_done()

	#stops the python program
	elif "stop" in command:
		quit()

talk("ready when you are")

while True:
	cmd(listenForCmd())
	time.sleep(2)
