import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import Emailpass

engine = pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
    hrs=int(datetime.datetime.now().hour)
    if hrs>=0 and hrs <12:
        speak("Good Morning Mam")
    elif hrs>=12 and hrs<18:
        speak("Good Afternoon Mam")
    else:
        speak("Good Evening Mam")
    speak("I am jarvis Mam, tell me how can i help you")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said; {query}\n")
    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query
def sendEmail(to,content):    
    e=Emailpass.getEmail()
    p=Emailpass.getPass()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(e,p)
    server.sendmail(e,to,content)
    server.close()
        
        
        

if __name__=="__main__":
    greet()
    while True:
        query=takeCommand().lower()
        
        if  'according to wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace('according to wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")
            
        elif 'github' in query:
            speak('opening github')
            webbrowser.open("github.com")   
        
        elif 'facebook' in query:
            speak('opening facebook')
            webbrowser.open("facebook.com")   
        
        elif 'according to google' in query:
            speak('opening google')
            query=query.replace('according to google','')
            webbrowser.open('http://google.com/#q='+query,new=2)
        
        elif 'play music' in query:
            music_dir="C:\\Users\\User\\Music"
            songs=os.listdir(music_dir)
            n = len(songs)
            index=random.randint(1,n)
            os.startfile(os.path.join(music_dir,songs[index]))
            
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Mam, the time is {strTime}")
            
        elif 'send email' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to="bobbyprathikshana@gmail.com"
                sendEmail(to,content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak("sorry mam, i am unable to send email")
            
         