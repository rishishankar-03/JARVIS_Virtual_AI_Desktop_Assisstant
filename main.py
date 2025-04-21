import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyautogui
import time
import subprocess
import re
import pygetwindow as gw
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

recognizer = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def beep():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.Sound("beep.wav").play()
    pygame.time.delay(600)
    pygame.quit()

def open_notepad_and_type():
    speak("Opening Notepad. Start speaking after the beep.")
    subprocess.Popen(['notepad.exe'])
    time.sleep(2)
    speak("Notepad is ready. Start speaking now. Say 'stop listening' to finish.")
    beep()
    while True:
        try:
            with sr.Microphone() as source:
                print("Beep....Listening for dictation...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=50)
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                if "stop listening" in text.lower():
                    speak("Stopping Listening.")
                    break
                pyautogui.typewrite(text + '\n')
        except sr.WaitTimeoutError:
            speak("Listening timed out. Stopping dictation.")
            break
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except Exception as e:
            print("Error:", e)
            break

def open_calculator():
    speak("Opening calculator.")
    subprocess.Popen("calc.exe")
    time.sleep(2)

def open_calculator_and_solve():
    speak("What should I calculate? Give me the question after the beep sound")
    beep()
    try:
        calc_win = None
        for w in gw.getWindowsWithTitle('Calculator'):
            if 'Calculator' in w.title:
                calc_win = w
                break

        if calc_win:
            calc_win.activate()
            time.sleep(1)
        else:
            speak("Calculator is not open. Please open it first.")
            return

    except Exception as e:
        print("Window error:", e)
        speak("I couldn't bring up the calculator.")
        return

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for math problem...")
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")

            query = query.lower()
            query = query.replace("plus", "+").replace("add", "+")
            query = query.replace("minus", "-").replace("subtract", "-")
            query = query.replace("multiplied by", "*").replace("multiply", "*").replace("times", "*")
            query = query.replace("divided by", "/").replace("divide", "/")
            query = query.replace("x", "*")

            expression = re.findall(r'[\d\.\+\-\*/]+', query)
            expression = ''.join(expression)

            if not expression:
                speak("Sorry, I couldn't understand the calculation.")
                return

            pyautogui.typewrite(expression)
            pyautogui.press('enter')
            speak(f"Calculating {expression}")

    except Exception as e:
        speak("Sorry, I couldn't perform the calculation.")
        print("Error:", e)

def processCommand(command):
    command_lower = command.lower()

    if "open google" in command_lower:
        speak("What should I search for on Google?")
        with sr.Microphone() as source:
            search_query = recognizer.listen(source)
            search_query = recognizer.recognize_google(search_query)
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif "play" in command_lower and ("on youtube" in command_lower or "on youtube music" in command_lower):
        if "on youtube music" in command_lower:
            song = command_lower.replace("play", "").replace("on youtube music", "").strip()
            if song:
                speak(f"Playing {song} on YouTube Music.")
                webbrowser.open(f"https://music.youtube.com/search?q={song}")
            else:
                speak("Please tell me the song name to play on YouTube Music.")
        elif "on youtube" in command_lower:
            song = command_lower.replace("play", "").replace("on youtube", "").strip()
            if song:
                speak(f"Playing {song} on YouTube.")
                pywhatkit.playonyt(song)
            else:
                speak("Please tell me the song name to play on YouTube.")

    elif "close youtube music" in command_lower:
        try:
            closed = False
            for window in gw.getWindowsWithTitle("YouTube Music"):
                window.close()
                closed = True
            speak("YouTube Music window has been closed." if closed else "No YouTube Music window was found.")
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't close YouTube Music.")

    elif "close youtube" in command_lower:
        try:
            closed = False
            for window in gw.getWindowsWithTitle("YouTube"):
                window.close()
                closed = True
            speak("YouTube window has been closed." if closed else "No YouTube window was found.")
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't close YouTube.")

    elif "time" in command_lower:
        now = datetime.datetime.now().strftime('%I:%M %p')
        print(now)
        speak('Current time is ' + now)

    elif "who" in command_lower:
        person = command_lower.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak('According to Wikipedia, ' + info)

    elif any(q in command_lower for q in ["what", "when", "how", "why"]):
        info = wikipedia.summary(command_lower, 2)
        print(info)
        speak('According to Wikipedia, ' + info)

    elif "open notepad" in command_lower:
        speak("Opening Notepad")
        os.system('start notepad')

    elif "write in notepad" in command_lower:
        open_notepad_and_type()

    elif "open paint" in command_lower:
        speak("Opening Paint")
        os.system('start mspaint')

    elif "open command prompt" in command_lower or "open cmd" in command_lower:
        speak("Opening Command Prompt")
        os.system('start cmd')

    elif "open control panel" in command_lower:
        speak("Opening Control Panel")
        os.system('start control')

    elif "open file explorer" in command_lower:
        speak("Opening File Explorer")
        os.system('start explorer')

    elif "open word" in command_lower:
        speak("Opening Microsoft Word")
        os.system('start winword')

    elif "open excel" in command_lower:
        speak("Opening Microsoft Excel")
        os.system('start excel')

    elif "open calculator" in command_lower:
        speak("Opening Calculator")
        os.system('start calc')

    elif "calculate" in command_lower or "solve" in command_lower:
        open_calculator_and_solve()

    elif "open burnout paradise" in command_lower:
        speak("Opening Burnout Paradise")
        os.system(r'"D:\Games\Burnout Paradise - The Ultimate Box\BurnoutParadise.exe"')

    elif "close notepad" in command_lower:
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "close paint" in command_lower:
        speak("Closing Paint")
        os.system("taskkill /f /im mspaint.exe")

    elif "close command prompt" in command_lower or "close cmd" in command_lower:
        speak("Closing Command Prompt")
        os.system("taskkill /f /im cmd.exe")

    elif "close word" in command_lower:
        speak("Closing Microsoft Word")
        os.system("taskkill /f /im WINWORD.EXE")

    elif "close excel" in command_lower:
        speak("Closing Microsoft Excel")
        os.system("taskkill /f /im EXCEL.EXE")

    elif "close calculator" in command_lower:
        speak("Closing Calculator")
        os.system("taskkill /f /im calc.exe")

    elif "close game" in command_lower:
        speak("Closing Burnout Paradise")
        os.system("taskkill /f /im BurnoutParadise.exe")

    elif "close control panel" in command_lower:
        speak("Closing Control Panel")
        os.system('taskkill /f /im control.exe')

    elif "close code app" in command_lower:
        speak("Closing Code Editor")
        os.system('taskkill /f /im Code.exe')  # For VS Code, adjust for other editors

    elif "exit" in command_lower or "stop" in command_lower or "quit" in command_lower:
        speak("Goodbye! Shutting down.")
        exit()

    else:
        print('Sorry, I cannot understand')
        speak('Sorry, I cannot understand')

if __name__ == "__main__":
    print("Hello there, I am Jarvis. Your personal voice assistant")
    speak("Hello there, I am Jarvis. Your personal voice assistant")
    while True:
        with sr.Microphone() as source:
            print("Recognizing...")
            r = sr.Recognizer()
            try:
                with sr.Microphone() as source:
                    r.energy_threshold = 1000
                    r.adjust_for_ambient_noise(source, 1.2)
                    print("Listening....")
                    audio = r.listen(source, timeout=5, phrase_time_limit=1)
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes. What can I do for you?")
                    with sr.Microphone() as source:
                        print("Jarvis Active....")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)
            except Exception as e:
                print("Error {0}".format(e))
