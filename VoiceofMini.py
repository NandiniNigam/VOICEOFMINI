import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from tqdm import tqdm
import wikipedia
import pyjokes
from turtle import *
from emoji import emojize
from time import sleep
import os
from tqdm import *

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 
engine.setProperty('rate',160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
    

def wish():
    
    print("\n\n\nHello User I am VoiceofMini.\nYou can simply ask me what to do or just refer to the USER GUIDE by saying 'User Guide'.")
    speak("Hello user I am Voice of Mini.\nYou can simply ask me what to do or just refer to the USER GUIDE by saying 'User Guide'.")  
    print("\nHow may I help you?")   
    speak("How may I help you?")
    
def Command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.......")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("RECOGNIZING......")
        query=r.recognize_google(audio,language='en-in')
        print(f"You said:{query}\n")
    
    except Exception as e:
        print("Please repeat")
        return "None"
    return query

def clear():
    os.system('cls')

def bar():
    for i in tqdm(range(0,100),desc='LOADING',unit='instructions'):
        sleep(0.02)

if __name__=="__main__":

    clear()
    bar()
    clear()
    wish()
    while True:
        query=Command().lower()

        if 'wikipedia' in query:
            speak("Sure Searching on Wikipedia.....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        

        elif 'open google' in query:
            speak("Sure Opening Google for you right away!")
            webbrowser.open("google.com")
        

        elif 'open youtube' in query:
            speak("Sure Opening Youtube for you right away!")
            webbrowser.open("youtube.com")


        elif 'the day' in query:
            strDay=datetime.datetime.now().strftime("%A")
            print(strDay)
            speak(f"The day is {strDay}")


        elif 'the date' in query:
            strDate=datetime.datetime.now().strftime("%d:%B:%y")  
            print(strDate)
            speak(f"The date is {strDate}")


        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}") 
              
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
                
        elif 'hello' in query:
            speak("hello there")
        

        elif 'name' in query:
            speak("My name is Voice of Mini")
        

        elif 'who are you' in query:
            speak("I am Voice of Mini, your Voice Assistant")

        
        elif 'what are you' in query:
            speak("I am a voice assistant")

        
        elif 'sad' in query:
            speak("Here are some flowers for you Don't be sad")
            print(emojize(":rose:"))
            print(emojize(":rose:"))
            print(emojize(":rose:"))
            print(emojize(":rose:"))
            print(emojize(":rose:"))


        elif 'user guide' in query:
            speak("This is the user guide")
            print("Functions of the voice assistant-VOICEOFMINI\n1. Can answer some of your questions\n2. Can tell you jokes\n3. Can open YouTube and Google using simple commands\n4. Can search for you on Wikipedia\n5. Can tell you the current time,date and day\n6. Gets disabled on being asked to 'quit'\n7. Gives the user a surprise when the user uses words 'love' or 'sad'! ")
 

        elif 'love' in query:
            speak("Dear user I have something for you")
            color("red","pink")
            begin_fill()
            left(50)
            forward(100)
            circle(40,180)
            left(260)
            circle(40,180)
            forward(100)
            end_fill()
            done()


        elif 'voice of mini' in query:
            speak("Hi user What can I help you with") 


        elif 'quit' in query:
            speak("Glad to help you out Have a good day!")
            print("Glad to help you out. Have a good day!")
            break


        else:
            speak("Sorry I dont understand what you mean by that")

exit
