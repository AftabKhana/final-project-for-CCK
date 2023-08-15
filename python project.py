import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time
# import pyjokes
import webbrowser



listener = sr.Recognizer()
# listener.pause_threshold = 67867867
engin=pyttsx3.init()
voices=engin.setProperty('rate',150)
voices=engin.getProperty("voices")
engin.setProperty('voice',voices[0].id)
a=("Good Morning sir...\nI am created by Cadet Aftab Khan of jinnah house.\n I'm your personal AI assistant. I'm here to help you with a wide range of tasks and answer your questions Whether it's providing information, automating tasks, I've got you covered. Feel free to interact with me and let's make things easier together!\nwhat can i do for you today. \n please speak sir")
print(a)
engin.say(a)
engin.runAndWait()

def talk(text):
 engin.say(text)
 engin.runAndWait()
def take_command():
  try:
     with sr.Microphone() as source:
        print("listining...")
        voice = listener.listen(source)
        command =listener.recognize_google(voice)
        command=command.lower()
        if "python" in command:
         command=command.replace("python","")
         print("user said :",command)

  except Exception as e:
      print("Waiting for you command respected Sir:")
      print("---")
      return "---"



  return command
def run_alexa():
    command = take_command()
    song=command.replace("play","")
    if "play" in  command:
        talk("playing" + song)
        pywhatkit.playonyt(song)
        print("A.I Assistant respnse :","playing",song)
    elif 'time' in command:
      time = datetime.datetime.now().strftime('%I:%M %p')
      print("A.I Assistant respnse\n", time)
      talk("sir the current time is " + time)
    elif 'tell me' in command:
       person=command.replace('tell me','')
       # info=wikipedia.summary(person,1)
       info=("A brief history of cadet college kohat:  \nCadet College Kohat  is a military high school located on the "
             "outskirts of Kohat,Pakistan. The foundation-stone was laid by late Malik Amir Muhammad Khan, on 19 April "
             "1964. The first entry of cadets was accepted in April 1965. Academic work started with 58 cadets and one "
             "boarding house called Jinnah House Lieutenant Colonel (Retired) Faizullah Khattak  was its founding "
             "Principal.\n Some information regarding cadet college kohat:\nMotto: from darkness into "
             "light\nPrincipal: 	Brigadier Tufail Muhammad Khan (retired)\nOpened:	1965\nColours:	Navy blue\nArea:	"
             "144 acres")
       print("A.I Assistant respnse:\n:",info)
       talk(info)
    elif "open google" in command:
        a=("A.I Assistant respnse:\nOpening Google sir......")
        print(a)
        b=("Opening Google sir....")
        talk(b)
        webbrowser.open('google.com')

    elif "website of cadet college kohat" in command:
       a=("A.I Assistant respnse:\nOpening website of cadet college kohat sir......")
       print(a)
       b = (" Opening website of cadet college kohat sir....")
       talk(b)
       webbrowser.open('https://www.cck.edu.pk/')
    elif "open youtube" in command:
        a=("A.I Assistant respnse:\nOpening youtube sir......")
        print(a)
        b=("Opening youtube sir....")
        talk(b)
        webbrowser.open('youtube.com')
    elif "ok  thank you for your help" in command:
         l=("A.I Assistant respnse:")
         d=("As we wrap up sir, remember that I'm here whenever you need assistance...\nWhether "
           "you have questions, tasks, or simply want to connect, I'll help you sir\nTake care and see you next time!\nbye sir")
         print(l)
         print(d)
         talk(d)
    elif "give us information about" in command:
        print("A.I Assistant respnse:")
        person=command.replace("give us information about","")
        info=wikipedia.summary(person, 3)
        print(info)
        talk(info)

while True:
  run_alexa()
