import pyttsx3 #text to audio
import os
import webbrowser #for webbrowser
import speech_recognition as ssr #audio to text
import nltk 
from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator
import datetime
import pywhatkit# for youtube like
import yfinance as yfin #to get share market
import pyjokes #to get jokes
import wikipedia #to get wikipedia
import subprocess #to run system tools and anything
import json

#Listen to Microphone and return Audio  as Text using google
def audioToText():
    recognise = ssr.Recognizer()
    with ssr.Microphone() as src:
        src.pause_threshold = 0.8
        heard=recognise.listen(src)
        try:
            print("I am listening...")
            q=recognise.recognize_google(heard, language="en")
            #write to awav file
            with open("microphone-results.wav", "wb") as f:
                f.write(audio.get_wav_data())
            print(q)
            nltk.download('vader_lexicon')
            analyzer=SentimentIntensityAnalyzer()
            scores=analyzer.polarity_scores(q)
            print(scores)
            if(scores[compound]>0):
                print('Positive speech')
            else:
                print('Negetive Speech')
            return q
        except ssr.UnknownValueError:
            print("I am not able to listen")
            return "I am waiting.."
        except ssr.RequestError:
            print("Sorry service is down")
            return "I am waiting.."
        except:
            return "I am waiting..."

def textToAudio(textmessage):
    eng=pyttsx3.init()
    for voice in eng.getProperty('voices'):
        print(voice)
    id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    eng.setProperty('voice',id) #voice selection
    eng.setProperty('volume',1.0) #volume of speech
    eng.setProperty('rate',120) #speeking slow setting
    eng.say(textmessage)
    eng.runAndWait()

def translate(message):
    translator=Translator()
    translation=translator.translate(message,encoding="utf-8",src='te',dest='en')
    print(translation.text)

def dictionary(sentence):
    with open("dictionary.json",'r') as worddictionary:
        word=json.load(worddictionary)
        if sentence in word:
            print(word[sentence])
    

def giveMeTodaysDate():
    day=datetime.date.today()
    print (day)
    textToAudio(f'todays date is {day}')
    return day

def giveMeTodaysWeekDay():
   td = giveMeTodaysDate()
   weekday = td.weekday()
   days= {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
   textToAudio(f'and todays day is {days[weekday]}')

def giveMeCurrentTime():
    tim=datetime.datetime.now()
    print(tim)
    currenttime=tim.strftime('%I:%M:%S')
    print(f'current time is {currenttime[0:2]} {currenttime[3:5]}')
    textToAudio(f'current time is {currenttime[0:2]} {currenttime[3:5]}')

def welcomeAboard():
    textToAudio(''' Hi, My name is Aphrodite 
    how may i help you
     ''')
    text=audioToText()
    name=text[8:13]
    print(name)
    status=True
    while(status):
        getVoice=audioToText().lower()
        print(f'voice {getVoice}')
        if('the time' in getVoice):
            textToAudio("Please be hold getting current time")
            giveMeCurrentTime()
            continue
        
        elif('date' in getVoice):
            textToAudio("Please be hold getting current date")
            giveMeTodaysDate()
            continue

        elif('day' in getVoice):
            textToAudio("Please be hold getting current day")
            giveMeTodaysWeekDay()
            continue
    
        elif('open youtube' in getVoice):
            textToAudio("Please be hold getting opening youtube")
            webbrowser.open('http://www.youtube.com/watch')
            continue

        elif('relax music' in getVoice):
            textToAudio("Please be hold playing nice music")
            webbrowser.open('https://www.youtube.com/watch?v=NvRL6TPgQcU')

        elif('open browser' in getVoice):
            textToAudio("Please be hold getting opening browser")
            webbrowser.open('http://www.google.com')
            continue

        elif('shutdown' in getVoice):
            textToAudio("Shutting down")
            textToAudio(f'Thank you {name}')
            break
        
        elif('search' in getVoice):
            textToAudio("Please be hold searching on web")
            pywhatkit.search(getVoice.replace('search',''))
            textToAudio("This is i got")
            continue

        elif('wiki' in getVoice):
            textToAudio("Please be hold searching on wikipedia")
            getVoice = getVoice.replace('wiki','')
            result=wikipedia.summary(getVoice,sentences=2)
            textToAudio("Found on wikipedia")
            textToAudio("Please find the result")
            textToAudio(result)
            continue

        elif('joke' in getVoice):
            textToAudio("Please be hold to fetch nice joke")
            textToAudio(pyjokes.get_joke())
            continue

        elif('find in youtube' in getVoice):
            textToAudio("Please be hold to search in youtube")
            pywhatkit.playonyt(getVoice.replace('find in youtube',''))
            textToAudio('Please find your search video')
            continue

        elif('open toolkit' in getVoice):
            textToAudio("Opening ACE toolkit")
            subprocess.run("C:\Program /Files\IBM\ACE\11.0.0.15\tools\IIBToolsLauncher.exe",shell=True)
            textToAudio("Is there anything else")
            continue

        elif('mq' in getVoice):
            textToAudio("Opening MQ")
            subprocess.run("strmqcfg",shell=True)
            textToAudio("Is there anything else")
            manager=audioToText().lower()
            if("create manager" in manager):
                qmanager=manager.replace("create manager","")
                subprocess.run("crtmqm {qmanager}")
            elif("create q" in manager):
                manager=manager.replace("create q","")
                subprocess.run("define qlocal({manager})|runmqsc {qmanager}")
            continue


#audioToText()
#textToAudio("Hello")
#giveMeDateAndDay()
#giveMeTodaysWeekDay()
#giveMeCurrentTime()
#welcomeAboard()
#translate('pette')
dictionary("culture")
