import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os





engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

print("\n==== MIA Voice Assistant MENU ====")
print("Say or type one of the following commands:")
print("  1. Wikipedia [topic]      → Search a topic on Wikipedia")
print("  2. Open YouTube           → Open youtube.com")
print("  3. Open Google            → Open google.com")
print("  4. Open Stack Overflow    → Open stackoverflow.com")
print("  5. Open Facebook          → Open facebook.com")
print("  6. Open VTOP              → Open VIT Bhopal VTOP portal")
print("  7. Open Vidyarthi         → Open Vityarthi courses")
print("  8. Open GitHub            → Open github.com")
print("  9. Open Spotify           → Open spotify.com")
print(" 10. The time               → Speak current time")
print(" 11. Open code              → Launch VS Code")
print(" 12. Terminate              → Exit the assistant")
print("===================================\n")
print("Example: Say 'Wikipedia VIT Bhopal' or 'Open YouTube'")



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, I am mia , your personal voice assistance, how may I help you?")
        print("Good Morning, I am mia , your personal voice assistance, how may I help you?")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon,I am mia , your personal voice assistance, how may I help you?")
        print("Good Afternoon,I am mia , your personal voice assistance, how may I help you?")
        
    else:
        speak("Good Evening, I am mia , your personal voice assistance, how may I help you?")
        print("Good Evening, I am mia , your personal voice assistance, how may I help you?")


    
    
def takeCommand():
    #microphone le leta hai user se 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query







if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak(f"According to Wikipedia,{results}!")
            print(results)
    
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open Google' in query :
            webbrowser.open('www.google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open Facebook' in query:
            webbrowser.open('https://www.facebook.com/')
        elif 'open v-top'in query :
            webbrowser.open('https://vtop.vitbhopal.ac.in/vtop/login')
        elif 'open vidyarthi' in query :
            webbrowser.open('https://vityarthi.com/my-courses')
        elif 'open GitHub' in query :
            webbrowser.open('https://github.com/')
        elif 'open spotify' in query :
            webbrowser.open('https://open.spotify.com/')
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H,%M,%S')
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\OMEN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'terminate' in query:
            speak('Goodbye Sir, have a nice day.')
            print('Goodbye Sir, have a nice day.')
              

  


