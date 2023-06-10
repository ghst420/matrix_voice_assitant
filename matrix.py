import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume', 2.0)
engine.setProperty('voice', 'english')
engine.setProperty('voice', voices[1].id)

engine.say("Welcome back sir, how can I help you today?")

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        engine.say("Listening")
        engine.runAndWait()
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        if "matrix" in command:
            engine.say("Hello, how are you master?")
        elif "fine" in command:
            engine.say("That's great. What's the plan for today?")

        elif "time" in command:
            now = datetime.datetime.now()
            times = now.strftime("%I:%M %p")
            engine.say(f"Sure sir! The time is {times}.")

        elif "what can you do for me" in command:
            engine.say("Sir, I'm your personal assistant. I can do anything for you.")
        
        elif "play" in command:
            song = command.replace('play', '')
            engine.say('Sure sir, playing ' + song)
            pywhatkit.playonyt(song)

        elif "who is" in command:
            person = command.replace('who is', '')
            engine.say(wikipedia.summary(person))

        elif "jokes" in command:
            engine.say(pyjokes.get_joke())

        elif "Instagram" in command:
            instagram = command.replace('instagram','')
            engine.say("Sure sir, I'm opening Instagram.")
            url = "https://www.instagram.com/"
            webbrowser.open(url,new=1)

        elif "WhatsApp"in command:
            engine.say("Sure sir, I'm opening Whatsaap.")
            url = "https://web.whatsapp.com/"
            webbrowser.open(url,new=1)

        elif "stop" in command:
            engine.say("OK, goodbye master. Have a nice day. Call me any time you need me.")
            engine.runAndWait()
            break

        else:
            engine.say("I'm sorry, I didn't catch that.")

        engine.runAndWait()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service;{e}")
        pass