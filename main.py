import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
import webbrowser
import pyjokes
import pyautogui
import psutil
import time
import winshell
import sys
import socket
import imdb


# Initialize the speech engine
engine = pyttsx3.init('sapi5')

# Set the voice (voices[1] usually refers to a female voice in Windows)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
from camera import*


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

def movie():
    moviesdb = imdb.IMDb()
    speak("Please tell me the movie name")
    text = takeCommand()

    movies = moviesdb.search_movie(text)
    speak("Searching for " + text)

    if len(movies) == 0:
        speak("No result found!")
    else:
        speak("I found these results:")

        for movie in movies:
            title = movie["title"]
            year = movie.get("year", "Unknown")  # Handle cases where year might be missing
            speak(f"{title} - {year}")

            info = movie.getID()
            movie_details = moviesdb.get_movie(info)

            rating = movie_details.get("rating", "No rating available")  # Handle missing rating
            plot = movie_details.get("plot outline", "No plot available")  # Handle missing plot

            current_year = int(datetime.datetime.now().strftime("%Y"))

            if isinstance(year, int) and year < current_year:
                speak(f"{title} was released in {year} and has an IMDb rating of {rating}. The plot summary is: {plot}")
            else:
                speak(
                    f"{title} will be released in {year} and has an IMDb rating of {rating}. The plot summary is: {plot}")

            break  # Stop after the first match


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

        # elif "play music" in order or "play song" in order:
        #     speak("Playing music.")
        #     music_dir = "C:\\Users\\Vaishnavi\\Music"
        #     songs = os.listdir(music_dir)
        #     if songs:
        #         rd = random.choice(songs)
        #         os.startfile(os.path.join(music_dir, rd))
        #     else:
        #         speak("I couldn't find any songs in your music folder.")

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

        elif "joke" in order or "jokes" in order:
            speak(pyjokes.get_joke(language="en", category = "neutral"))

        elif "time" in order:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well the time is {strTime}")

        elif "shutdown" in order or "turn off" in order:
            speak("Shutting down your system. Make sure to save your work.")
            os.system("shutdown /s /t 5")

        elif "restart" in order:
            speak("Restarting your system now.")
            os.system("shutdown /r /t 5")

        elif "log off" in order or "sign out" in order:
            speak("Logging off your system.")
            os.system("shutdown /l")

        elif "hybernate" in order:
            speak("Hybernating....")
            os.system("shutdown / l")

        elif "switch window" in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif "take a screenshot" in order or "screenshot this" in order:
            speak("Please tell me the name for this file.")
            name = takeCommand().lower()
            if name == "none" or name.strip() == "":
                name = "screenshot"
            speak("Please hold the screen.")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot captured successfully!")

        elif "cpu status" in order:
            usage = psutil.cpu_percent(interval=1)
            speak(f"CPU usage is at {usage} percent.")

        elif "empty recycle bin" in order:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin recycled successfully!")

        elif "camera" in order :
            cam()

        elif "exit" in order or "stop" in order or "quit" in order:
            speak("Thank you for using me. Have a good day!")
            sys.exit()

        elif "ip" in order:
            host = socket.gethostname()  # Get the hostname
            ip = socket.gethostbyname(host)  # Get the IP address of the hostname
            speak("Your IP address is " + ip)

        elif "bmi" in order:
            speak("Please tell me your height in centimeters")
            height = takeCommand()

            speak("Please tell me your weight in kilograms")
            weight = takeCommand()

            try:
                height = float(height) / 100  # Convert height to meters
                weight = float(weight)  # Convert weight to float
                BMI = weight / (height * height)  # BMI calculation

                speak(f"Your Body Mass Index is {BMI:.2f}")

                if BMI <= 16:
                    speak("You are severely underweight")
                elif BMI <= 18.5:
                    speak("You are underweight")
                elif BMI <= 25:
                    speak("You are healthy")
                elif BMI <= 30:
                    speak("You are overweight")
                else:
                    speak("You are obese")

            except ValueError:
                speak("Invalid input. Please try again.")

        elif "movie" in order:
            movie()

        else:
            speak("I didn't catch that. Could you please repeat?")

print("I love Clifton so much!")