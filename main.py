import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import subprocess

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) +
          "/" + str(month) + "/" + str(year))


def wishme():
    print("Welcome back sir!!")
    speak("Welcome back")

    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir!")

    speak("I'm bob. Here to help you!")
    print("I'm bob. Here to help you!")


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\KISHAN\\OneDrive\\Documents\\Jarvis 2.0\\ss3.png")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        return query

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"


def main():
    while True:
        query = takecommand().lower()
        print(query)
        if "time" in query:
            time()

        elif "date" in query:
            date()

        # elif "who are you" in query:
        #     speak("I'm bob. Here to help you!")
        #     print("I'm bob. Here to help you!")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")

        elif "open youtube" in query:
            wb.open('https://www.youtube.com/')

        elif "open google" in query:
            wb.open("https://www.google.com/")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            subprocess.run(["open", "-a", "Spotify"])

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "/Applications/Google Chrome.app"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")

        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "remember anything" or "show my reminders" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif "offline" in query:
            quit()


if __name__ == "__main__":
    main()
