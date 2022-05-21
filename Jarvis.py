import pyttsx3  # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition, pip install pipwin, pipwin install pyaudio
import wikipedia  # pip install wikipedia
import webbrowser  # pip install webbroswer
import datetime
import os
import smtplib
import math
import random
import sys
import pygame
from pygame.locals import *


engine = pyttsx3.init('espeak') # use sapi5 instead of espeak if you are windows user
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishUser():
    local_time = int(datetime.datetime.now().hour)
    if local_time >= 0 and local_time < 12:
        speak("Good Morning Sir!")

    elif local_time >= 12 and local_time < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis - Your personal assitant. Please tell me how can I help you ?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 400
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        print("I didn't get you sir. Can you repeat ?")
        return "None"
    return query


def sendEmail(gmail, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', gmail, content)
    server.close()

def setAlarm(hour, minute, second, period, alarm):
    if period == datetime.datetime.now().strftime('%p'):
        hour += 12

    while True:
        if hour ==  datetime.datetime.now().hour and minute == datetime.datetime.now().minute and second == datetime.datetime.now().second:
            print(f'Alarm at: {hour}:{minute}:{second} {period}')
            speak(f'Alarm at: {hour}:{minute}:{second} {period}')
            alarm.play(-1)
            if input() == 'Stop' or input() == 'stop':
                pygame.quit()
                sys.exit()


if __name__ == "__main__":

    pygame.init()

    wishUser()
    if 1:
        query = takeCommand().upper()
        str(query)

        # Logic for executing tasks based on query
        if 'WIKIPEDIA' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query)
            speak("According to Wikipedia")
            speak(results)

        elif 'OPEN' in query:
            appsLink = {
                "GOOGLE": "https://Google.com",
                "YOUTUBE": "https://Youtube.com",
                "FACEBOOK": "https://Facebook.com",
                "TWITTER": "https://Twitter.com",
                "INSTAGRAM": "https://Instagram.com",
                "BAIDU": "https://Baidu.com",
                "YAHOO": "https://Yahoo.com",
                "WHATSAPP": "https://web.Whatsapp.com",
                "AMAZON": "https://Amazon.in",
                "ZOOM": "https://Zoom.us",
                "NETFLIX": "https://Netflix.com",
                "REDDIT": "https://Reddit.com",
                "PRINTEST": "https://Printest.com",
                "LINKEDIN": "https://Linkedin.com",
                "MICROSOFTWEBSITE": "https://Microsoft.com",
                "BING": "https://Bing.com",
                "TWITCH": "https://Twitch.tv",
                "DUCKDUCKGO": "https://Duckduckgo.com",
                "MSN": "https://Msn.com",
                "TRIPADVISOR": "https://tripadvisor.com",
                "ALIBABA": "https://Alibaba.com",
                "WALMART": "https://Walmart.com",
                "Y2MATE": "https://Y2mate.com",
                "PIXLR": "https://pixlr.com",
                "GOOGLEMEET": "https://meet.google.com",
                "SPEEDTEST": "https://speedtest.net",
                "STACKOVERFLOW": "https://stackoverflow.com",
                "FLIPKART": "https://flipkart.com",
                "APPLE": "https://Apple.com/in/",
                "PRIME": "https://primevideo.com",
                "HOTSTAR": "https://hotstar.com",
                "YANDEX": "https://yandex.com",
                "AMAZON": "https://amazon.com/in/",
                "GMAIL": "https://mail.google.com",
                "HACKERRANK": "https://hackerrank.com",
                "UNACADEMY": "https://unacademy.com",
                "VEDANTU": "https://vedantu.com",
                "GDRIVE": "https://drive.google.com",
                "GTRANSLATE": "https://translate.google.co.in",
                "GPHOTOS": "https://photos.google.com",
                "GDOCS": "https://docs.google.com/document/u/0/",
                "GSHEETS": "https://docs.google.com/spreadsheets/u/0/",
                "GPLAY": "https://play.google.com",
                "GMAPS": "https://maps.google.com",
                "GNEWS": "https://news.google.com",
                "GACCOUNT": "https://myaccount.google.com",
                "GFORMS": "https://forms.gle",
                "GBOOKS": "https://book.google.com",
                "GODADDY": "https://godaddy.com",
                "PAYPAL": "https://paypal.com",
                "BOOTSTRAP": "https://getbootstrap.com",
                "EBAY": "https://ebay.com",
                "BUYDOAMINS": "https://buydomains.com",
                "TIMESOFINDIA": "https://timesofindia.indiatimes.com",
                "BLOGGER": "https://blogger.com",
                "QUORA": "https://quora.com",
                "PYTHONWEBSITE": "https://python.org",
                "W3SCHOOLS": "https://w3schools.com",
                "OPERA": "https://opera.com",
                "SOUNDCLOUD": "https://soundcloud.com",
                "ANDROID": "https://android.com",
                "NASA": "https://nasa.gov",
                "MYSQL": "https://mysql.com",
                "BLOOMBERG": "https:bloomberg.com",
                "SHUTTERSTOCK": "https://shutterstock.com",
                "RESEARCHGATE": "https://researchgate.net",
                "IKEA": "https://ikea.com",
                "FORBES": "https://forbes.com",
                "SAMSUNG": "https://samsung.com",
                "ORACLE": "https://oracle.com",
                "GITHUB": "https://github.com",
                "CLOUDFLARE": "https://cloudfalre.com",
                "MOZILLA": "https://mozilla.org",
                "ESPN": "https://espn.com",
                "TELEGRAM": "https://telegram.me",
                "SNAPCHAT": "https://snapchat.com",
                "UDEMY": "https://udemy.com",
                "IMDB": "https://imdb.com",
                "UNSPLASH": "https://unsplash.com",
                "XBOX": "https://xbox.com",
                "PLAYSTATION": "https://playstation.com",
                "ASUS": "https://asus.com",
                "MEGA": "https://mega.nz",
                "MEDIAFIRE": "https://mediafire.com",
                "ADIDAS": "https://shop.adidas.co.in",
                "DELL": "https://dell.com",
                "LENOVO": "https://lenovo.com",
                "HP": "https://hp.com",
                "EA": "https://ea.com",
                "STEAM": "https://steampowered.com",
                "PUMA": "https://in.puma.com",
                "REBOOK": "https://shop4rebook.com",
                "ACER": "https://acer.com",
                "PEXELS": "https://pexels.com",
                "IBMWEBSITE": "https://ibm.com",
                "PIXABAY": "https://pixabay.com",
                "BRITANNICA": "https://britanica.com",
                "OUTLOOK": "https://outlook.com",
                "LG": "https://lg.com",
                "HUWAEI": "https://huwaei.com",
                "GIGABYTE": "https://gigabyte.com",
                "INTEL": "https://intel.in",
                "TUBI": "https://tubitv.com",
                "NIKE": "https://nike.com",
                "AMD": "http://amd.com",
                "NVIDIA": "https://nvidia.com",
                "MSI": "https:/msi.com",
                "CHROME": "C:/Program Files/Google/Chrome/Application/chrome.exe",
                "SPOTIFY": "C:/Users/Administrator/AppData/Roaming/Spotify/Spotify.exe",
                "BRAVE": "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",
                "CCLEANER": "C:/Program Files/CCleaner/CCleaner64.exe",
                "DISCORD": "C:/Users/Administrator/AppData/Local/Discord/Update.exe",
                "MICROSOFT EDGE": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
                "ACCESS": "C:/Program Files (x86)/Microsoft Office/root/Office16/MSACCESS.EXE",
                "POWERPOINT": "C:/Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE",
                "EXCEL": "C:/Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE",
                "ADOBEREADERDC": "C:/Program Files/Adobe/Acrobat DC/Acrobat/Acrobat.exe",
                "VISUALSTUDIOCODE": "C:/Users/Administrator/AppData/Local/Programs/Microsoft VS Code/Code.exe",
                "PYCHARM": "C:/Program Files/JetBrains/PyCharm Community Edition 2021.2/bin/pycharm64.exe",
                "MEMREDUCT": "C:/Program Files/Mem Reduct/memreduct.exe",
                "VLCMEDIAPLAYER": "C:/Program Files/VideoLAN/VLC/vlc.exe",
                "POWERSHELL": "%SystemRoot%/system32/WindowsPowerShell/v1.0/powershell.exe",
                "PUBLISHER": "C:/Program Files (x86)/Microsoft Office/root/Office16/MSPUB.EXE",
                "OUTLOOK": "C:/Program Files (x86)/Microsoft Office/root/Office16/OUTLOOK.EXE",
                "MICROSOFTEDGE": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
            }
            try:
                split_str = query.split()
                webbrowser.open(appsLink[str(split_str[1])], new=1)
            except Exception as e:
                print("Speech Error... Can't Proceed !")
                speak("Speech Error... Can't Proceed !")

        elif 'PLAY A MUSIC' in query:
            music_dir = "D:/Music/EDM/Music"
            songs = os.listdir(music_dir)
            random_music = random.choice(songs)
            speak(f"Okay, playing {random_music}")
            os.startfile(random_music)
            if 'STOP' in query:
                sys.exit()

        elif 'RANDOM NUMBER' in query:
            split_str = query.split()
            random_num = random.randint(1, 10)
            print(random_num)
            speak(random_num)

        elif 'MAKE ME LAUGH' in query:
            jokes_list = ["Why do we tell actors to break a leg?, because every play has a cast.",
                          "What did one trafic light say to the other?, stop looking I am changing.",
                          "What kind of tea is hard to swallow?, reality.",
                          "Why do bees have sticky hair?, because they use honeycombs.", ]

            random_joke = random.choice(jokes_list)
            print(random_joke)
            speak(random_joke)

        elif 'THE TIME' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif ('CREATE A FOLDER NAMED') in query:
            split_str = query.split()

            def createFile():
                folder = str(split_str[4])
                dir = "C:/Users/Administrator/Desktop/"
                if folder not in dir:
                    try:
                        path = os.path.join(dir, folder)
                        os.mkdir(path)
                        speak(f"Sucessfuly created {str(split_str[4])}")
                    except Exception as e:
                        speak(
                            f"{str(split_str[4])} is already there, do you want to create another folder named {str(split_str[4]) + str(2)}")
                        takeCommand()
                        if 'YES' in query:
                            folder = (str(split_str[4]) + str(2))
                            path = os.path.join(dir, folder)
                            os.mkdir(path)
                            speak(
                                f"Okay, sucessfully created a folder named {str(split_str[4]) + str(2)}")
                        elif 'NO' in query:
                            sys.exit()
            createFile()
        
        elif 'SET ALARM' in query:
            speak('Please provide the following information:')
            alarm = pygame.mixer.load('D:\\Productivity\\Python\\Projects\\Alarm Clock\\Alarm.mp3')
            hour = int(input('PLEASE SET THE HOUR:'))
            minute = int(input('PLEASE SET THE MINUTE:'))
            second = int(input('PLEASE SET THE SECOND:'))
            period = input('PLEASE SET AM/PM:').upper() 
            setAlarm(hour, minute, second, period ,alarm)         

        elif 'EMAIL TO' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("please enter the gmail id of the person")
                gmail = input()
                if gmail.endswith("@gmail.com"):
                    sendEmail(gmail, content)
                    speak("Email has been sent!")
                else:
                    print("Invalid email")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif '+' in query:
            split_str = query.split()
            answer = float(split_str[0]) + float(split_str[2])
            try:
                print(int(answer))
                speak(int(answer))
            except Exception as e:
                print(answer)
                speak(answer)

        elif '-' in query:
            split_str = query.split()
            answer = float(split_str[0]) - float(split_str[2])
            try:
                print(int(answer))
                speak(int(answer))
            except Exception as e:
                print(answer)
                speak(answer)

        elif '*' in query:
            split_str = query.split()
            answer = float(split_str[0]) * float(split_str[2])
            try:
                print(int(answer))
                speak(int(answer))
            except Exception as e:
                print(answer)
                speak(answer)

        elif '/' in query:
            split_str = query.split()
            answer = float(split_str[0]) / float(split_str[2])
            try:
                print(int(answer))
                speak(int(answer))
            except Exception as e:
                print(answer)
                speak(answer)
        elif 'cos' in query:
            split_str = query.split(" ")
            speak(f"cos of {split_str[1]} is {math.cos(split_str[1])}")

        elif 'sin' in query:
            split_str = query.split(" ")
            speak(f"cos of {split_str[1]} is {math.sin(split_str[1])}")

        elif 'tan' in query:
            split_str = query.split(" ")
            speak(f"cos of {split_str[1]} is {math.tan(split_str[1])}")

        elif 'EXIT' in query:
            sys.exit()