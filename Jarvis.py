# from email.mime import audio
import pyttsx3   #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition
import wikipedia         #pip install wikipedia
import webbrowser
import os
import smtplib   #for email    \item 
import random

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# print(voices)
print(voices[1].id)
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate') 
engine.setProperty('rate',165)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")   
    speak("I am Jarvis , how can i help you?") 

def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.energy_threshold = 200
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold=1  #pause aane pe ruke 
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="eng-in")
        print("User said:",query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

# def sendEmail(to,content):
#     server=smtplib.SMTP("smtp.gmail.com",587)
#     server.ehlo()
#     server.starttls()
#     server.login("alisaif006123@gmail.com","passworddoc@123#")
#     server.sendemail("alisaif006123@gmail.com",to,content)
#     server.close()
        
if __name__=="__main__":
 wishMe()
 while True:
    query=takeCommand().lower()   
    #-->task-1
    #Logic of executing task based on query
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
     #-->task-2
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    #-->task-3
    elif "open google" in query:
        webbrowser.open("google.com")
    #-->task-4
    elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")
     #-->task-5(Music)
    elif " music" in query:
        music_dir="D:\\Music"
        songs=os.listdir(music_dir)
        print(songs)
        a=random.randint(0,5)
        os.startfile(os.path.join(music_dir,songs[a]))  #we can use random module to play any random song
    #-->task-
    elif "open notepad" in query:
        path="C:\\Windows"
        os.startfile(path)
    #-->task-6
    elif "time" in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir,the time is{strTime}")
    #-->task-7(for opening any application)
    elif "open code" in query:
        codePath="C:\\Users\\alisa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

     #-->task-8(email)
    elif "email" in query:
        try:
            speak("What should i say?")
            content=takeCommand    #It takes microphone input from the user and returns string output
            to="alisaif006123@gmail.com"
            # sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry saif bhai.I am not able to send this email")
    #-->task-9(quit)
    elif "quit" in query:
        exit()

    


