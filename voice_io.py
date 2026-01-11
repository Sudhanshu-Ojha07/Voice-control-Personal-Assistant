import gtts
from gtts import gTTS
import os

import speech_recognition as sr
import webbrowser as wb

import nltk
# import pyttsx3
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
from nltk.corpus import stopwords as s
from nltk.stem import WordNetLemmatizer
import subprocess


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

def speak(audio):
    # initializing gtts module
    tts = gtts.gTTS(text=audio,tld='com', lang='en-gb', slow =False)
    tts.save('temp.mp3')
    temp_audio_file= "temp.mp3"
    output_audio_file = "fast_audio.mp3"
    
    command = [
    "ffmpeg", "-i", temp_audio_file, 
    "-filter:a", "atempo=1.5", 
    "-y", output_audio_file  # -y overwrites the output if it exists
    ] 

    
    subprocess.run(command)
    os.system("mpg321 " + output_audio_file)
    os.remove('temp.mp3')

# engine = pyttsx3.init()
# engine.setProperty("rate", 200)  # speed (default ~200)
# engine.setProperty("volume", 1.0)
# engine.setProperty("voice", "com.apple.speech.synthesis.voice.Alex")  # voice
# engine. setProperty('pitch', 35)  # pitch

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
