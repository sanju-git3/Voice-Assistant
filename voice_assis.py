import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engin=pyttsx3.init('sapi5')
voices=engin.getProperty('voices')
#print(voices[1].id)
engin.setProperty('voice',voices[0].id)

def speak(audio):
    engin.say(audio)
    engin.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Mornig!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")   

    speak("i am Jarvis.Please tell me how ma i help you")

def takeCommand():
    #it takes microphone input from user and return string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...")
       r.pause_threshold = 1
       audio=r.listen(source)

    try:
       print("recording...")
       query=r.recognize_google(audio , language ='en-in')
       print(f"User said: {query}\n")  

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return query    

if __name__=="__main__":
    wishMe()
    while (True):
        query=takeCommand().lower()
        #logic for executing tasks based on query

        if "wikipedia" in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query or 'music'in query:
            music_dir="D:\\myfavmusic"
            songs=os.listdir(music_dir)
            print(songs)  
            os.startfile(os.path.join(music_dir,songs[0])) 


        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Mam, the time is{strTime}")

        elif 'open code' in query:   
           codepath= "C:\\Users\\Akash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codepath)

        elif 'open zoom' in query:   
           zoompath= "C:\\Users\\Akash\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
           os.startfile(zoompath)

        elif 'open facebook' in query:   
           webbrowser.open("facebook.com")

        elif 'open whatsapp web' in query:   
           webbrowser.open("web.whatsapp.com")   
  
