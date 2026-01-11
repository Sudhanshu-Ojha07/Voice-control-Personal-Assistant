import os
import speech_recognition as sr
import webbrowser as wb

from voice_io import take_commands, speak
from llm.llm_mode import start_llm_mode

import datetime
import psutil  # For battery status
import requests  # For internet connection check
import time
import subprocess

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

def interact_with_deepseekr(shell_process):
    """Interact with the Deepseekr shell using voice."""
    while True:
        # Take command via voice
        command = take_commands()
        if command is None:
            continue
        
        # Exit interaction on a specific command
        if "exit" in command.lower():
            speak("Exiting Deepseekr shell interaction.")
            break

        # Send command to the shell
        try:
            shell_process.stdin.write(command + "\n")
            shell_process.stdin.flush()
        except Exception as e:
            print(f"Error sending command: {e}")
            speak("There was an error sending the command.")
            continue


def wake():
    """Start a shell process and interact with it."""
    try:
        speak("Starting the deep seeker shell.")
        print("Starting the deep seeker shell.")
        shell_process = subprocess.Popen(
            ["usr/bin/ollama", "run", "deepseek-r1:1.5b"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Ensures inputs and outputs are strings
        )
        interact_with_deepseekr(shell_process)
        shell_process.terminate()

          # Terminate the process when done
    except Exception as e:
        print(f"Error: {e}")
        speak("There was an error starting the shell.")
    
   
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
        elif "internet" in keywords:
            internet()
        elif "wake" in keywords:
            speak("Yes boss, entering intelligent mode.")
            start_llm_mode()

    
            

            

            
        

        
        
        



        
        