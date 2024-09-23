import gtts
import os

import speech_recognition as sr
import webbrowser as wb

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.corpus import stopwords as s
from nltk.stem import WordNetLemmatizer
import datetime
import psutil  # For battery status
import requests  # For internet connection check
import time

# creating take_commands() import randomfunction which
# can take some audio, Recognize and return
# if there are not any errors

def take_commands():
    stopwords = set(s.words('english'))
 
    r = sr.Recognizer()    # initializing speech_recognition
    r.punctuation = False  # Set the punctuation configuration
    
    # opening physical microphone of computer
    with sr.Microphone() as source:
        
        print('Listening')
        # adjusting for ambient noise
        r.adjust_for_ambient_noise(source, duration=1)# storing audio/sound to audio variable
        r.pause_threshold = 0.7
        
        
        
        print("Say something...")
        # storing audio/sound to audio variable
        audio = r.listen(source, phrase_time_limit=70)  # wait for 30 seconds
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            
            # returning none if there are errors
            Query = "None"
            keywords = []
            return Query, keywords
    # Preprocessing the user's input
    
    tokens = nltk.word_tokenize(Query)
    tokens = [token for token in tokens if token.lower() not in stopwords]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    pos_tags = nltk.pos_tag(tokens)
    named_entities = nltk.ne_chunk(pos_tags)
    # Extracting keywords from the user's input
    keywords = []
    for tag in pos_tags:
        if tag[1] in ['NNP', 'NNPS', 'NNS', 'NN']:
            keywords.append(tag[0])
    for entity in named_entities:
        if type(entity) == nltk.tree.Tree:
            keywords.append(entity.label())
            for leaf in entity:
                if type(leaf) == nltk.tree.Tree:
                    keywords.append(leaf.label())
                else:
                    keywords.append(leaf)
    
   

    return Query, keywords 

    

# creating Speak() function to giving Speaking power
# to our voice assistant 
def speak(audio):
    # initializing gtts module
    tts = gtts.gTTS(text=audio,tld='com', lang='en-gb', slow =False)
    tts.save('temp.mp3')
    os.system('mpg321 temp.mp3')
        

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is H:M:S", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(str(day))
    speak(str(month))
    speak(str(year))
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))
def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    if battery.power_plugged:
        status = "charging"
    else:
        status = "not charging"
    return percent, status

def check_internet():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        return False
    return False
def power():
    percent, status = check_battery()
    speak(f"Your power is at {percent} percent and it is currently {status}.")
    print(f"Power status: {percent}% ({status})")

def internet():
    if check_internet():
        speak("Internet connection is good, boss.")
        print("Internet connection is good.")
    else:
        speak("No internet connection detected.")
        print("No internet connection.")

    
   
def wishme():
    print("Welcome back, sir. Congratulations for the new update ...!")
    speak("Welcome back, sir. Congratulations for the new update...")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning ")
        print("Good Morning !!")
    
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon ")
        print("Good Afternoon ")
    elif hour >= 16 and hour < 24:
        speak("Good Evening ")
        print("Good Evening ")
    else:
        speak("Its Night")
        speak("Friday at your service Sir...")

    


# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    
    wishme()
    while True:
        command, keywords = take_commands()
        if "time" in command:
            time()
            
        elif "YouTube" in keywords:
            wb.open("https://www.youtube.com/")
            speak("Youtube is opened sir")
            speak("Have fun!")
        elif "power" in keywords:
            power()  
        elif "date" in keywords:
            date()
        elif "offline" in keywords:
            speak("Sure sir! ,Test complete. Preparing to power down and begin diagnostics")
            break
        elif "insta" in keywords:
            speak("sudhanshu.ojha.404")
        elif "name" in keywords:
            speak("I am Friday !, 'I am a virtual assistant' ")
        elif "code" in keywords:
            speak("Access denied !")
            print("Access denied!")
        elif "terminal" in keywords:
            os.system("gnome-terminal &")
            speak("terminal is opened")
        elif "online" in keywords:
            speak("At your service sir, How can I help you")

    
            

            

            
        

        
        
        



        
        
