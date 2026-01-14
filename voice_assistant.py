import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import time   

engine = pyttsx3.init()

def speak(text: str):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def get_time():
    now = datetime.now()
    return now.strftime("It is %I:%M %p")

def get_date():
    today = datetime.now()
    return today.strftime("Today is %d %B %Y")

def listen() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Calibrating for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 0.4
        r.non_speaking_duration = 0.3
        r.energy_threshold = 300
        print("Listening...")
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No speech detected in time.")
            return ""

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print("You said:", query)
        return query.lower().strip()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
    except sr.RequestError:
        speak("Network error. Please check your connection.")
    return ""

def handle_command(command: str) -> bool:
    if not command:
        speak("Please say something again.")
        return True

    if "hello" in command or "hi" in command:
        speak("Hello, how can I help you?")

    elif "time" in command:
        speak(get_time())

    elif "date" in command or "day" in command:
        speak(get_date())

    elif "search" in command or "google" in command:
        speak("What should I search for?")
        time.sleep(1)              
        search_query = listen()
        if search_query:
            url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
            webbrowser.open(url)
            speak("Here are the search results for " + search_query)
        else:
            speak("I did not catch the search query.")

    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye! Stopping now.")
        return False

    else:
        speak("Right now I only understand hello, time, date, search, and exit.")
    return True

if __name__ == "__main__":
    speak("Hello, I am your voice assistant. Say hello, time, date, search, or exit.")
    running = True
    while running:
        cmd = listen()
        running = handle_command(cmd)
