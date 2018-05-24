#!/usr/bin/env python3

#to recognize speech using Api or speech engine
import speech_recognition as sr
#to commuticate to microphone install pyaudio

#recognizer instance
r=sr.Recognizer()

''''
print("Reading audio file")
#creating audio file manager instance
jackhammer = sr.AudioFile('jackhammer.wav')
#content manager opens and reads file stores in source
with jackhammer as source :
#removing noice
	r.adjust_for_ambient_noise(source)
#recording data from source to audio
	audio = r.record(source)
'''
#fetching audio from microphone
mic=sr.Microphone()
print("Listening ....")
#capturing microphone input
with mic as source :
	#handling noise
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source)

print("Converting to text")
#passing audio to recongnizer
#recognizer method for recognizing speech from audio source
#using google web speech api - require internet
print("You said : ",r.recognize_google(audio))