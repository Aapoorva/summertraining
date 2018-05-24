#!/usr/bin/env python3

#to recognize speech using Api or speech engine
import speech_recognition as sr

#recognizer instance
r=sr.Recognizer()

print("Reading audio file")
#creating audio file manager instance
jackhammer = sr.AudioFile('jackhammer.wav')
#content manager opens and reads file stores in source
with jackhammer as source :
#removing noice
	r.adjust_for_ambient_noise(source)
#recording data from source to audio
	audio = r.record(source)

print("Converting to text")
#passing audio to recongnizer
#recognizer method for recognizing speech from audio source
#using google web speech api - require internet
print(r.recognize_google(audio, show_all=True))