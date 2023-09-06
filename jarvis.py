import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from AppOpener import run
import smtplib
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hii I am alexa how may i help you")
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recogniging.........")
        query=r.recognize_google(audio,language="en-in")
        print(f"User Said:{query}\n")
    except Exception as e:
        print (e)
        print("say that again...please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("kappaganthulastmaheswari.19.it@anits.edu.in","tripura8787")
    server.sendmail("kappaganthulastmaheswari.19.it@anits.edu.in",to,content)
    server.close()
if __name__=="__main__":
    wishMe()
    #while True:
    if 1:
        query=take().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open spotify" in query:
            run("spotify")
        elif "open word" in query:
            codePath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
            os.startfile(codePath)
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hey , time is {strTime}")
        elif "open code" in query:
            codePath="C:\\Users\\91701\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Code.exe"
            os.startfile(codePath)
        elif "email" in query:
            try:
                speak("what should I say..?")
                content=take()
                to="itsmedevaki@gmail.com"
                sendEmail(to,content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                print("Sorry Tripura I am not able to send this email")
            