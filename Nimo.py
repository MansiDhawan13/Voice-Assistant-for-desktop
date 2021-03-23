import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import random
import datetime
import wikipedia 
import webbrowser

r1 = random.randint(1,10000000)
r2 = random.randint(1,10000000)

filename = str(r2)+"randomtext"+str(r1) +".mp3"
def speak(text):

    tts=gTTS(text=text,lang="en")
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
         audio=r.listen(source)
         said = ""

         try:
             said = r.recognize_google(audio)
             print(said)
         except Exception as e :

              
             print("Exception:" +str(e))
    return said
  
if __name__ == "__main__":
    wishMe()
    speak("hello madam, i am nemo, how may i help you")
    while True:
    # if 1:
        said = get_audio().lower()

        # Logic for executing tasks based on said
        if 'wikipedia' in said:
            speak('Searching Wikipedia...')
            said = said.replace("wikipedia", "")
            results = wikipedia.summary(said, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in said:
            webbrowser.open("youtube.com")

        elif 'open google' in said:
            webbrowser.open("google.com")

        elif 'open github' in said:
            webbrowser.open("github.com")   


        elif 'play music' in said:
            webbrowser.open("gaana.com")
        
        
            

        elif 'the time' in said:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Madam, the time is {strTime}")

        elif 'exit' in said:
            speak("thanks for intereacting with me")
            break

          


os.remove(filename)
    



