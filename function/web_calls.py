import speech_recognition as sr
from random import choice
from utils import openning_text
from datetime import datetime
import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    """Used to speak whatever text is passed to it"""
    
    engine.say(text)
    engine.runAndWait()

def greet_user():
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"This is {BOTNAME}. Your personal assistant, How may I assist you?")

def take_user_input():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listenning.....')
		r.pause_threshold = 1
		audio = r.listen

	try:
		print('Recognizing...')
		query = r.recognize_google(audio, language='en-US')
		if not 'exit' in query or 'stop' in query:
			speak(choice(openning_text))
		else:
			hour >= datetime.now().hour
			if hour >=21 and hour <6:
				speak('Good night {USERNAME}, Take care!')
			else:
				speak('Have a Good day, Bye for now!')
			exit()
	except Exception:
		speak ('Sorry, I could not recoginze, please try again')
		query = None
	return query