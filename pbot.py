import speech_recognition as sR
import pyttsx3
import pywhatkit
import os
import datetime
import wikipedia
import pyjokes
listener = sR.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text): #conversion of string to speech
    engine.say(text)
    engine.runAndWait()
def takeCommand(): #for recognisation
        try:
            with sR.Microphone() as source: #open microphone
                print('listening...')
                voice = listener.listen(source) #listen user
                cmd = listener.recognize_google(voice)
                print(cmd)
        except:
            pass
        return cmd
def run(): # for interaction
    command = takeCommand()
    print(command)
    if 'play' in command: #condition statement for command
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'open' in command:
        app = command.replace('open', '')
        speak('Starting ' + app)
        os.system('start ' + app)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        details = wikipedia.summary(person, 1)
        print(details)
        speak(details)
    
    else:
        speak('Please repeat the command')
        
while True:
    run()
