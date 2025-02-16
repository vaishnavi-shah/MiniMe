import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
import webbrowser
import pyjokes

# Initialize the speech engine
engine = pyttsx3.init('sapi5')

# Set the voice (voices[1] usually refers to a female voice in Windows)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

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
            audio = r.listen(source, timeout=10, phrase_time_limit=15)
            print("Recognizing....")
            recognized_text = r.recognize_google(audio, language="en-in")
            print(f"User said: {recognized_text}\n")
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            speak("I didn't hear anything. Could you please repeat?")
            return "None"
        except sr.UnknownValueError:
            print("Could not understand audio.")
            speak("Sorry, I couldn't understand what you said.")
            return "None"
        except Exception as e:
            print(f"Error: {e}")
            speak("An error occurred while recognizing your voice.")
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

        elif "open chrome" in order or "open browser" in order:
            speak("Opening Google Chrome.")
            npath2 = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath2)

        elif "play music" in order or "play song" in order:
            speak("Playing music.")
            music_dir = "C:\\Users\\Vaishnavi\\Music"
            songs = os.listdir(music_dir)
            if songs:
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
            else:
                speak("I couldn't find any songs in your music folder.")

        elif "wikipedia" in order or "search" in order:
            speak("Searching...")
            order = order.replace("wikipedia", "").replace("search", "").strip()

            if not order:
                speak("Please specify what you want to search on Wikipedia.")
            else:
                try:
                    results = wikipedia.summary(order, sentences=2)
                    speak("According to Wikipedia")
                    speak(results)
                except wikipedia.DisambiguationError as e:
                    speak("Your query is too broad. Here are some possible options:")
                    speak(", ".join(e.options[:5]))
                except wikipedia.PageError:
                    speak("Sorry, I couldn't find any information on that topic.")
                except Exception as e:
                    speak(f"An unexpected error occurred: {str(e)}")


        elif "open google" in order:
            speak("Here you go to Google!")
            webbrowser.open("https://www.google.com/")

        elif "open youtube" in order:
            speak("Here you go to YouTube!")
            webbrowser.open("https://www.youtube.com/")

        elif "open myntra" in order:
            speak("Here you go to Myntra!")
            webbrowser.open("https://www.myntra.com/")

        elif "open meesho" in order:
            speak("Here you go to Meesho!")
            webbrowser.open("https://www.meesho.com/")

        elif "open flipkart" in order:
            speak("Here you go to Flipkart")
            webbrowser.open("https://www.flipkart.com/")

        elif "open amazon" in order:
            speak("Here you go to Amazon!")
            webbrowser.open("https://www.amazon.in/")

        elif "open nykaa" in order:
            speak("Here you go to Nykaa!")
            webbrowser.open("https://www.nykaa.com/")

        elif "open canva" in order:
            speak("Here you go to Canva!")
            webbrowser.open("https://www.canva.com/")

        elif any(keyword in order for keyword in ["open linkedin", "linkedin", "open my linkedin"]):
            speak("Here you go to LinkedIn!")
            webbrowser.open("https://www.linkedin.com/feed/")

        elif "open instagram" in order:
            speak("Here you go to Instagram!")
            webbrowser.open("https://www.instagram.com/")

        elif any(keyword in order for keyword in ["open lms", "lms", "open my lms"]):
            speak("Here you go to LMS!")
            webbrowser.open("https://aln.anudip.org/login/index.php")

        elif "open pinterest" in order:
            speak("Here you go to Pinterest!")
            webbrowser.open("https://in.pinterest.com/")

        elif "open gpt" in order:
            speak("Here you go to ChatGPT!")
            webbrowser.open("https://chatgpt.com/")

        elif "open grammarly" in order:
            speak("Here you go to Grammarly!")
            webbrowser.open("https://www.grammarly.com/")

        elif "open quillbot" in order:
            speak("Here you go to Quillbot!")
            webbrowser.open("https://quillbot.com/")

        elif "open threads" in order:
            speak("Here you go to Instagram Threads!")
            webbrowser.open("https://www.threads.net/?hl=en")

        elif "open facebook" in order:
            speak("Here you go to Facebook!")
            webbrowser.open("https://www.facebook.com/")

        elif "open github" in order:
            speak("Here you go to GitHub!")
            webbrowser.open("https://github.com/")

        elif "open spotify" in order:
            speak("Here you go to Spotify!")
            webbrowser.open("https://open.spotify.com/")

        elif "where is" in order:
            order = order.replace("where is","")
            location = order
            speak("Locating....")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"")

        elif "write a note" in order:
            speak("What should i write ?")
            note = takeCommand()
            file = open("minime.txt","w")
            speak("Should i include date and time as well?")
            sn = takeCommand()
            if "yes" in sn or "sure" in sn or "yeah" in sn:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(note)
                speak("Done!")
            else:
                file.write(note)
                speak("Done!")

        elif "show note" in order:
            speak("Showing notes")
            file = open("minime.txt","r")
            print(file.read())
            speak(file.read(6))

        elif "joke" or "jokes" in order:
            speak(pyjokes.get_joke(language="en", category = "neutral"))

        elif "time" in order:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well the time is {strTime}")


        else:
            speak("I didn't catch that. Could you please repeat?")






