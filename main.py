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
    img.save('./ss.png')


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
        # speak("Please say that again")
        return "Try Again"

# def takecommand():
#     n = input("enter string: ")
#     return n


def main():
    wishme()
    while True:
        query = takecommand().lower()
        print(query)
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm bob. Here to help you!")
            print("I'm bob. Here to help you!")

        elif "hello" in query:
            speak("Hello, I'm bob. I am here to help you!")
            print("Hello, I'm bob. Here to help you!")

        elif "hi" in query:
            speak("Hello, I'm bob. I am here to help you!")
            print("Hello, I'm bob. Here to help you!")

        elif "what's up" in query:
            speak("Nothing much sir")
            print("Nothing much sir")

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
                query = query.replace('wikipedia', '')
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")

        elif "what" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace('what', '')
                query = query.replace('is', '')
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")

        elif "open youtube" in query:
            wb.open('https://www.youtube.com/')

        elif "open google" in query:
            wb.open("https://www.google.com/")

        elif "overflow" in query:
            wb.open("stackoverflow.com")

        elif "open spotify" in query:
            subprocess.run(["open", "-a", "Spotify"])

        elif "play" in query:
            subprocess.run(
                ["osascript", "-e", 'tell application "Spotify" to play'])

        elif "resume" in query:
            subprocess.run(
                ["osascript", "-e", 'tell application "Spotify" to play'])

        elif "pause" in query:
            subprocess.run(
                ["osascript", "-e", 'tell application "Spotify" to pause'])

        elif "next" in query:
            subprocess.run(
                ["osascript", "-e", 'tell application "Spotify" to next track'])

        elif "previous" in query:
            subprocess.run(
                ["osascript", "-e", 'tell application "Spotify" to previous track'])

        elif "open chrome" in query:
            subprocess.run(["open", "-a", "Google Chrome"])

        elif "search" in query:
            try:
                search = query.replace('search', '')
                search = search.replace('for', '')
                print(search)
                search = search.replace(' ', '+')
                wb.open(f"https://www.google.com/search?q={search}")

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

        elif "show my reminders" in query:
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
