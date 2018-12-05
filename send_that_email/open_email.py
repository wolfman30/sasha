import selenium 
import time 
from selenium import webdriver 
import webbrowser
import speech_recognition as sr
import winspeech

def talk(text_to_audio):
    winspeech.say(text_to_audio)

def listenForCmd():

	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		talk("Hello, online and ready")
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

def open_email(command):
    try: 
        
        if 'open email' in command: 

            talk('opening email')

            browser = webdriver.Chrome('The path to your downloaded chromedriver.exe file')
            browser.maximize_window()

            browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

            email_field = browser.find_element_by_id('identifierId')
            email_field.clear()
            email_field.send_keys('YOUR_EMAIL_ADDRESS')

            submit_button = browser.find_element_by_id('identifierNext')
            submit_button.click()

            time.sleep(3)

            pass_field = browser.find_element_by_name('password')
            pass_field.clear()
            pass_field.send_keys('YOUR_EMAIL_PASSWORD')

            pass_sub_button = browser.find_element_by_id('passwordNext')
            pass_sub_button.click()
    except:
        talk('Sorry, that did not work')

if __name__ == '__main__':
    open_email(listenForCmd())

