# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 15:49:55 2020

@author: Vera J. Morgana
"""
import os
from pydub import AudioSegment

def convertOne (file, name):
    
    mp3_sound = AudioSegment.from_mp3(file)
        
    #rename them using the old name + ".wav"
    mp3_sound.export("{0}.wav".format(name), format="wav")

    filename = name + ".wav"
    print (filename)
    
    return filename

def convertAll ():
    
    audio_files = os.listdir()
    
    # Iterate over all files directly using:
    for file in audio_files:
        
        # Split the file into Name and Extension
        name, ext = os.path.splitext(file)
        
        print ("file: " + file + " name: " + name)
        
        if ext == ".mp3":            
            mp3_sound = AudioSegment.from_mp3(file)
            
            #rename them using the old name + ".wav"
            mp3_sound.export("{0}.wav".format(name), format="wav")
        
            filename = name + ".wav"
            print (filename)
    
    print ("Success!")

# convertAll()
# convertOne("Afraid.mp3", "Afraid")