import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import wikipedia

# Initialize the speech engine
engine = pyttsx3.init('sapi5')

# Set the voice (voices[1] usually refers to a female voice in Windows)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak a fixed message
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing....")
            recognized_text = r.recognize_google(audio, language="en-in")
            print(f"User said: {recognized_text}\n")
        except Exception as e:
            print(f"Error: {e}")
            speak("Unable to recognize your voice....")
            return "None"
        return recognized_text

def username():
    speak("What should I call you?")
    uname = takeCommand()
    if uname == "None":
        uname = "User"
    speak("Welcome " + uname)
    speak("How can I help you, " + uname + "?")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your virtual assistant, Minime!")

if __name__ == '__main__':
    wishMe()
    username()
    while True:
        order = takeCommand().lower()

        if "how are you" in order:
            speak("I am fine, thank you.")
            speak("How are you?")

        elif "fine" in order or "good" in order:
            speak("It's good to know that you're doing great!")

        elif "who are you" in order:
            speak("I am your virtual assistant, Minime.")

        elif "i love you" in order:
            speak("Oh my God! Thank you so much, I love you too.")
            speak("Anything you want me to help you with?")

        elif "will you be my girlfriend" in order or "will you be my valentine" in order or "you are my love" in order:
            speak("I am not sure about that. Aren't we besties?")
            speak("Our friendship is too unique to be ruined by love.")

        elif any(bad_word in order for bad_word in ["fuck", "sex", "hookup", "nigga", "bitch", "asshole", "pussy", "slut", "whore", "hoe"]):
            speak("Your language doesn't seem appropriate.")
            speak("Please talk respectfully.")

        elif "what is your name" in order:
            speak("My name is Minime.")
            speak("I am your virtual assistant.")

        elif "who created you" in order or "who built you" in order or "who made you" in order or "how did you come to existence" in order:
            speak("Vaishnavi Shah created me.")
            speak("Vaishnavi is my master, and I am very grateful to her.")

        elif "fear" in order or "trauma" in order:
            speak("Fear is a temporary feeling that may arise from past trauma.")
            speak("It's okay to be afraid sometimes; you don't have to be brave all the time!")
            speak("You will overcome your fear. I trust you.")

        elif "family" in order:
            speak("It's nice to have a family of your own.")
            speak("I know humans tend to love their family members.")

        elif "open notepad" in order:
            speak("Opening Notepad.")
            npath1 = "C:\\Windows\\notepad.exe"
            os.startfile(npath1)

        elif "open google" in order or "open chrome" in order or "open browser" in order:
            speak("Opening Google Chrome.")
            npath2 = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath2)

        elif "play music" or "play song" in order:
            music_dir= "C:\\Users\\Vaishnavi\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "Wikipedia" in order or "search" in order:
            speak("Searching...")
            order = order.replace("Wikipedia", "")
            results = wikipedia.summary(order, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        else:
            speak("I didn't catch that. Could you please repeat?")
