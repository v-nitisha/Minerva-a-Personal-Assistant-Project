# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:36:55 2020

@author: Vera J. Morgana
"""
# Imports
# from SpeechRecognition001 import SpeechRecognitionMain
import SpeechRecognition001 as SR001
import pyttsx3, time

# Menu Options
def print_menu():
    print ("1. Speech Recognition")
    print ("2. Enter Database (Upcoming)")
    print ("3. Speak you Command")

# Welcome Message based on Current Time
def welcome_message():
    
    currentTime = int(time.strftime('%H'))   
    
    if currentTime < 12 :
        message = 'Good morning, Vera!'
        speakMinerva (message)
        
        print(message)
        
    elif currentTime > 12 :
        message = 'Good afternoon, Vera!'
        speakMinerva (message)
        
        print(message)
        
    elif currentTime > 6 :
        message = 'Good evening, Vera!'
        speakMinerva (message)
        
        print(message)

def goodbye_message():
    currentTime = int(time.strftime('%H'))   
    
    if currentTime > 10 :
        message = 'Good night, Vera!'
        speakMinerva (message)
        
        print(message)
    else :
        message = 'Goodbye, Vera!'
        speakMinerva (message)
        
        print(message)
         
def speakMinerva (message):
    engine = pyttsx3.init()
    
    # Set voice to Female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    # Set voice rate (made slower)
    newVoiceRate = 145
    engine.setProperty('rate',newVoiceRate)
    
    engine.say(message)
    engine.runAndWait()

def main ():
    choice = "0"
    quitStatement = "Go to sleep"
    
    welcome_message ()
    
    while choice != "Go to sleep": 
        print_menu()
        
        choice = input("Enter your choice: ")
        
        if (choice=="1" or choice=="One" or choice=="one"):
            print ("Menu 1 has been selected")
            
            try:
                SR001.SpeechRecognitionMain.main()
                print("Done")
            except AttributeError: # Error due to this
                print ("module 'SpeechRecognition001' has no attribute 'SpeechRecognitionMain'")
    
        elif (choice=="2" or choice=="Two" or choice=="two"):
             print ("Menu 2 has been selected")
        elif (choice==quitStatement):
            try:
                exit ()
            except NameError:
                goodbye_message()
        else:
            print ("\nPut me to sleep or make me work\n")

main()