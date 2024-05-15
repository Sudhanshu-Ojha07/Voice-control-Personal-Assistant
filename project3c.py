# Your import statements and NLTK downloads here...
import gtts
import os

import speech_recognition as sr
import webbrowser as wb
import pygame
import nltk
from nltk.corpus import stopwords as s
from nltk.stem import WordNetLemmatizer
import datetime
import threading

# Download NLTK resources if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

pygame.init()   # Initialize Pygame

# Set up the Pygame window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("J.A.R.V.I.S. Arc Reactor Animation")

# Load the Arc Reactor animation frames
arc_reactor_frames = []  
frame_directory = "/home/sudhanshu/Downloads/J.A.R.V.I.S"
frame_count = 135 

for i in range(frame_count):
    frame_path = os.path.join(frame_directory, f"frame_{i:03d}_delay-0.07s.jpg")
    frame = pygame.image.load(frame_path).convert()  
    arc_reactor_frames.append(frame)

# Main loop
running = True
current_frame_index = 0
clock = pygame.time.Clock()

# Lock for thread synchronization
lock = threading.Lock()

def take_commands():
    stopwords = set(s.words('english'))
 
    r = sr.Recognizer()    
    r.punctuation = False  
    
    with sr.Microphone() as source:
        print('Listening')
        r.adjust_for_ambient_noise(source, duration=0.5)  
        r.pause_threshold = 0.5
        print("Say something...")
        audio = r.listen(source, phrase_time_limit=5)  # Reduced time for faster response
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            Query = "None"
            keywords = []
            return Query, keywords

    tokens = nltk.word_tokenize(Query)
    tokens = [token for token in tokens if token.lower() not in stopwords]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    pos_tags = nltk.pos_tag(tokens)
    named_entities = nltk.ne_chunk(pos_tags)
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
    
    print("Keywords:")
    for keyword in keywords:
        print(keyword)

    return Query, keywords 

def speak(audio):
    tts = gtts.gTTS(text=audio, lang='en', slow=False)  # Simplified options
    tts.save('temp.mp3')
    os.system('mpg321 temp.mp3')

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is " + Time)
    print("The current time is:", Time)

def date():
    now = datetime.datetime.now()
    speak("the current date is " + now.strftime("%d %B %Y"))
    print("The current date is:", now.strftime("%d %B %Y"))

def wishme():
    print("Welcome back sir...!")
    speak("Welcome back sir...")
    
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning ")
        print("Good Morning !!")
    elif 12 <= hour < 16:
        speak("Good Afternoon ")
        print("Good Afternoon ")
    elif 16 <= hour < 24:
        speak("Good Evening ")
        print("Good Evening ")
    else:
        speak("Its Night")
        speak("Friday at your service Sir...")

if __name__ == '__main__':
    wishme()
    

    # Start the take_commands() function in a separate thread
    take_commands_thread = threading.Thread(target=take_commands)
    take_commands_thread.start()

    while running:
        command, keywords = take_commands()
        
        lock.acquire()  # Acquire lock before accessing shared resources
        window.fill((0, 0, 0))
        current_frame = arc_reactor_frames[current_frame_index]
        window.blit(current_frame, (0, 0))
        pygame.display.update()
        current_frame_index = (current_frame_index + 1) % len(arc_reactor_frames)
        lock.release()  # Release lock after updating the display

        clock.tick(60)  # Adjust frame rate to 60 frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if "time" in command:
            time()
            
        elif "YouTube" in command:
            wb.open("youtube.com") 

        elif "date" in keywords:
            date()
        elif "exit" in keywords:
            speak("Sure sir! as your wish, bai")
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

    pygame.quit()
    
