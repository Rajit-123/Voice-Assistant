from re import A
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import winsound
from playsound import playsound
from gtts import gTTS
from googletrans import Translator, LANGUAGES
import os
import webbrowser
import requests
from bs4 import BeautifulSoup
import smtplib
import urllib.request
from tkinter import *
from threading import Thread
import random
import cv2
from PIL import Image, ImageTk
import PIL
import json
from urllib.request import urlopen
root=Tk()



engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


dic=('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am',
	'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn', 'bosnian',
	'bs', 'bulgarian', 'bg' , 'catalan', 'ca',
'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)',
	'zh-cn', 'chinese (traditional)', 'zh-tw',
'corsican', 'co', 'croatian', 'hr', 'czech', 'cs', 'danish',
	'da', 'dutch', 'nl', 'english', 'en', 'esperanto',
'eo', 'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi',
	'french', 'fr', 'frisian', 'fy', 'galician', 'gl',
'georgian', 'ka', 'german', 'de', 'greek', 'el', 'gujarati',
	'gu', 'haitian creole', 'ht', 'hausa', 'ha',
'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi', 'hmong',
	'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo',
'ig', 'indonesian', 'id', 'irish', 'ga', 'italian', 'it',
	'japanese', 'ja', 'javanese', 'jw', 'kannada', 'kn',
'kazakh', 'kk', 'khmer', 'km', 'korean', 'ko', 'kurdish (kurmanji)',
	'ku', 'kyrgyz', 'ky', 'lao', 'lo',
'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish',
	'lb', 'macedonian', 'mk', 'malagasy',
'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori',
	'mi', 'marathi', 'mr', 'mongolian', 'mn',
'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no',
	'odia', 'or', 'pashto', 'ps', 'persian',
'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa',
	'romanian', 'ro', 'russian', 'ru', 'samoan',
'sm', 'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho',
	'st', 'shona', 'sn', 'sindhi', 'sd', 'sinhala',
'si', 'slovak', 'sk', 'slovenian', 'sl', 'somali', 'so',
	'spanish', 'es', 'sundanese', 'su',
'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil',
	'ta', 'telugu', 'te', 'thai', 'th', 'turkish', 'tr',
'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug', 'uzbek',
	'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu')

def speak(audio):
    AITaskStatusLbl['text'] = 'Speaking...'
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        attachTOframe("Good Morning Sir!",True)
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        attachTOframe("Good afternoon Sir!",True)
        speak("Good afternoon Sir!")
    else:
        attachTOframe("Good evening Sir!",True)
        speak("Good evening Sir!")
    attachTOframe("my self chitti , how may i help u!",True)
    speak("my self chitti , how may i help u!")

def attachTOframe(text,bot=False):
	if bot:
		botchat = Label(top,text=text, bg="#007cc7", fg='white', justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
		botchat.pack(anchor='w',ipadx=5,ipady=5,pady=5)
	else:
		userchat = Label(top, text=text, bg="#007cc7", fg='white', justify=RIGHT, wraplength=250, font=('Montserrat',12, 'bold'))
		userchat.pack(anchor='e',ipadx=2,ipady=2,pady=5)

def takeCommand(x=0):
    AITaskStatusLbl['text'] = 'Listening...'
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold=400
        audio= r.listen(source)
    
    try:
        AITaskStatusLbl['text'] = "recornigeing..."
        query=r.recognize_google(audio)
        print(query)
        if x==1:
            clearChatScreen()
        attachTOframe(query,False)

    except Exception as e:
        print("say again")
        attachTOframe("say again",True)
        return "None"
    return query

def voiceMedium():
    while True:
        query = takeCommand(1)
        if query == 'None': continue
        elif "quit" in query:
            attachTOframe("thank you sir!!!",True)
            speak("thank you sir!!!")
            break
        else: main(query.lower())
imageName = ''
def clickPhoto():
    import cv2

    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    playsound('assets/audios/photoclick.mp3')

    if result:
        cv2.imshow("GeeksForGeeks", image)
        cv2.imwrite("GeeksForGeeks.png", image)
        cv2.destroyWindow("GeeksForGeeks")
        speak('Do you want to view your clicked photo?')
        query = takeCommand().lower()
        if "ok" in query:
            speak("Ok, here you go...")
            img = Image.open("GeeksForGeeks.png")
            resize=img.resize((350,300))
            test=ImageTk.PhotoImage(resize)
            botchat = Label(top,image=test, justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
            botchat.image=test
            botchat.pack(anchor='w',ipadx=5,ipady=5,pady=5)


        else:
            speak("No Problem ")

    else:
	    print("No image detected. Please! try again")

def imgg(query):
            URL = "https://www.google.com/search?tbm=isch&q=" + query
            result = requests.get(URL)
            src = result.content
            soup = BeautifulSoup(src, 'html.parser')
            imgTags = soup.find_all('img', class_='yWs4tf') # old class name -> t0fcAb

            if os.path.exists('Downloads')==False:
                os.mkdir('Downloads')
    
            count=0
            for i in imgTags:
                if count==4: break
                try:
                    urllib.request.urlretrieve(i['src'], 'Downloads/' + str(count) + '.jpg')
                    count+=1
                    print('Downloaded', count)
                except Exception as e:
                    raise e
	


def viewPhoto():
    img = PhotoImage(file="D:\\assitant\\GeeksForGeeks.png")
    resize=img.resize((330,300))
    test=ImageTk.PhotoImage(resize)
    botchat = Label(top,image=resize, justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
    botchat.pack(anchor='w',ipadx=5,ipady=5,pady=5)


def main(query):

    while True:
        if "hello" in query:
            wish()
            return
        if "wikipedia" in query or "who is" in query or "what is" in query:
            query = query.replace('wikipedia','')
            query = query.replace('what is','')
            query = query.replace('who is','')
            query = query.replace('search','')
            if len(query.split())==0: query = "wikipedia"
            try:
                imgg(query)
                img = Image.open("D:\\assitant\\Downloads\\1.jpg")
                resize=img.resize((100,100))
                test=ImageTk.PhotoImage(resize)
                botchat = Label(top,image=test, justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
                botchat.image=test
                botchat.pack(anchor='w',ipadx=5,ipady=5,pady=5)
                result=wikipedia.summary(query, sentences=2)
                print("\n"+result)
                attachTOframe(result,True)
                speak(result)
            except Exception as e:
                speak("Desired Result Not Found")
            return
        if "translate" in query:
            attachTOframe("What do you want to translate?",True)
            speak("What do you want to translate?")
            sentence = takeCommand().lower()
            attachTOframe("Which language to translate ?",True)
            speak("Which language to translate ?")
            language = takeCommand().lower()
            if language in LANGUAGES.values():
                translator = Translator()
                result = translator.translate(sentence, src='en', dest=language)
                print(result.text)
                attachTOframe(result.text,True)
                txt=result.text
                language=dic[dic.index(language)+1]
                sp=gTTS(text=txt,lang=language,slow=False)
                ii=random.randrange(1,100,1)
                st=str(ii)
                str0="captured_voice"+st
                str1=str0+".mp3"
                print(str1)
                sp.save(str1)
                playsound(str1)
                os.remove(str1)
            else:
                attachTOframe("This langauage doesn't exists",True)
                speak("This langauage doesn't exists")
            return
        if "image" in query:
            query = query.replace('images','')
            query = query.replace('image','')
            query = query.replace('search','')
            query = query.replace('show','')
            imgg(query)

            return
            
        if 'selfie' in query or ('click' in query and 'photo' in query):
                speak("Sure sir ...")
                clickPhoto()
                return
        if 'the time' in query:
            now = datetime.datetime.now()
            time=now.strftime("%H:%M:%S")
            attachTOframe(time,True)   
            speak(f"Sir, the time is {time}")

            return
        if 'joke' in query:
            URL = 'https://icanhazdadjoke.com/'
            result = requests.get(URL)
            src = result.content
            soup = BeautifulSoup(src, 'html.parser')
            try:
                p = soup.find('p')
                attachTOframe(p.text,True)
                speak(p.text)
            except Exception as e:
                print("")
            return
        if "youtube" in query:
            query = query.replace('play',' ')
            query = query.replace('on youtube',' ')
            query = query.replace('youtube',' ')

            webbrowser.open('https://www.youtube.com/results?search_query='+query)
            attachTOframe("Enjoy...",False)
            speak("Enjoy...")
            return
        if 'how are you' in query:
            attachTOframe("I am fine, Thank you",True)
            speak("I am fine, Thank you")
            attachTOframe("How are you, Sir",True)
            speak("How are you, Sir")
            return
 
        if 'fine' in query or "good" in query:
            attachTOframe("It's good to know that you are fine",True)
            speak("It's good to know that you are fine")
            return
        
        if 'news' in query:
            URL = 'https://indianexpress.com/latest-news/'
            result = requests.get(URL)
            src = result.content
            soup = BeautifulSoup(src, 'html.parser')
            headlineLinks = []
            headlines = []

            divs = soup.find_all('div', {'class':'title'})
            count=0
            for div in divs:
                count += 1
                if count > 4:
                    break
                a_tag = div.find('a')
                headlineLinks.append(a_tag.attrs['href'])
                headlines.append(a_tag.text)
            speak('Getting the latest news...')
            for head in headlines: 
                attachTOframe(head,True)
                speak(head)

            speak('Do you want to read the full news?')
            text = takeCommand().lower()
            if "no" in text or "don't" in text:
                speak("No Problem sir!!!")
            else:
                speak("Ok sir Opening browser...")
                webbrowser.open('https://indianexpress.com/latest-news/')
                speak("You can now read the full news from this website.")
            return

        if "write a note" in query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('d.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm or 'ok' in snfm:
                    now = datetime.datetime.now()
                    time=now.strftime("%H:%M:%S")
                    file.write(time)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
                return
         
        if "open note" in query:
                speak("Showing Notes")
                file = open("d.txt", "r")
                attachTOframe(file.read(),True)
                speak(file.read(6))
                return
            
        if "weather" in query:
             
                api_key = "Api key"
                base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                speak(" City name ")
                attachTOframe("City name : ")
                city_name = takeCommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()
             
                if x["code"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    attachTOframe(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description),True)
                    speak(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                else:
                    attachTOframe(" City Not Found ",True)
                    speak(" City Not Found ")
                return

        if "where is" in query:
            query = query.replace("where is", "")
            location = query
            attachTOframe("User asked to Locate",True)
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/" + location + "") 
 
        else:
            return

def clearChatScreen():
	for wid in top.winfo_children():
		wid.destroy()



if __name__=="__main__":
    root.title("deepak asistant")
    w_width, w_height = 400, 650
    s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
    root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
    root.configure(bg='#203647')
    root.pack_propagate(0)
    top=Frame(root,width=400,height=550,bg='#12232e')
    top.pack()
    top.pack_propagate(0)
    bop=Frame(root,width=400,height=100,bg='#dfdfdf')
    bop.pack()
    bop.pack_propagate(0)
    textimg=PhotoImage("button.png")
    cbl = Label(bop, fg='white', image=textimg, bg='#dfdfdf')
    cbl.pack(anchor=CENTER,pady=20)
    AITaskStatusLbl = Label(bop, text='Offline', fg='white', bg='#12232e', font=('montserrat', 16))
    AITaskStatusLbl.place(x=150,y=32)
    
    try:
		# pass
        Thread(target=voiceMedium).start()
    except:
        pass
    root.mainloop()
    
    
    