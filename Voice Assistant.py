import os
import pyttsx3
import speech_recognition as sr
import random
import requests
import datetime, time
import wikipedia
import webbrowser
import subprocess
import pywhatkit
import pyjokes
import wolframalpha
import json

# voice based commands
engine = pyttsx3.init('sapi5')              # sapi5 is a API of Microsoft
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def welcome():
    """Greet the user."""
    print("Intialzing Alexa....")
    time.sleep(1)
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello Sir! Good Morning.")
    elif hour >= 12 and hour < 18:
        speak("Hello Sir! Good Afternoon.")
    else:
        speak("Hello Sir! Good Evening.")
    time.sleep(1)
    speak("I am Alexa your virtual Assistant here. Please tell me How may i Help you?")
    time.sleep(1)


def takeCommand():
    """It takes input from the user microphone & returns string output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300
        r.pause_threshold = 1           # seconds of non-speaking audio before a phrase is considered complete.
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User : {query}\n")
        time.sleep(1)

    except Exception as e:
        print(e)
        print("Sorry! unable to hear.... say that again Please...")
        return "None"
    return query


if __name__ == '__main__':
    welcome()
    while True:
        query = takeCommand().lower()
        print(query)

        if 'video song' in query:
            song = query.replace('video song', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'play music' in query:
            music_dict = "E:\MUSIC"
            songs = os.listdir(music_dict)
            os.startfile(os.path.join(music_dict, random.choice(songs)))
            time.sleep(5)

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening Youtube")
            webbrowser.open("https://www.youtube.com/")
            time.sleep(5)

        elif 'open Chrome' in query:
            speak('opening Google Chrome')
            Goc_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(Goc_path)
            time.sleep(5)

        elif 'open google' in query:
            speak("okay,what should i search on google")
            cmd = takeCommand().lower()
            webbrowser.open(f"{cmd}")
            time.sleep(5)

        elif 'open stack overflow' in query:
            url = "https://stackoverflow.com/"
            speak("opening stack overflow")
            webbrowser.open(url)
            time.sleep(5)

        elif 'open visual studio code' in query:
            speak('opening Visual code')
            vs_path = "C:\\Users\\Akash Arora\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_path)
            time.sleep(5)

        elif 'open whatsapp' in query:
            speak("opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
            time.sleep(5)

        elif 'open instagram' in query:
            speak("opening Instagram")
            webbrowser.open("https://www.instagram.com")
            time.sleep(5)

        elif 'open Github' in query:
            speak("opening Github")
            webbrowser.open("https://www.github.com")
            time.sleep(5)

        elif 'time' or 'what the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The Time is {strtime}")

        elif 'tell me fun facts' or 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)

        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("For which City")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " + str(current_temperature) +
                      "\n humidity (in %) " + str(current_humidiy) + "\n description = " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " + str(current_temperature) +
                      "\n humidity (in %) " + str(current_humidiy) + "\n description = " +
                      str(weather_description))
            else:
                speak("Sorry,City Not Found ")

        elif "Make notes" or 'write a note' in query:
            speak("What should i write")
            note = takeCommand()
            file = open('Notes.txt', 'w')
            speak("Sir, Should i include date and time? -> Yes/Okay/No")
            snfm = takeCommand()
            if 'yes' in snfm or 'okay' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" or "open my notes" in query:
            speak("Showing Notes")
            file = open("Notes.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'who are you' in query:
            speak('I am Alexa sir your virtual Assistant')

        elif 'help me' in query:
            speak("Yes sir How may I help you")

        elif 'open cmd' in query:
            speak("opening Command Prompt")
            os.system("start cmd")
            time.sleep(5)

        elif 'open powershell' in query:
            speak("opening Window Powershell")
            os.system("start powershell")
            time.sleep(5)

        elif 'lock windows' in query:
            speak('Your system is being locked')
            ctypes.windll.user32.LockWorkStation()

        elif "shut down" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif 'goodbye' or 'exit' in query:
            speak("okay, GoodBye sir! It's nice conservation with you.")
            exit()
