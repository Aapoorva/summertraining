#!/usr/bin/env python3

#to recognize speech using Api or speech engine
import speech_recognition as sr
#to commuticate to microphone install pyaudio

#recognizer instance
r=sr.Recognizer()

#function to read audio file
def read_audio_file() :
	print("Reading audio file")
	#creating audio file manager instance
	jackhammer = sr.AudioFile('jackhammer.wav')
	#content manager opens and reads file stores in source
	with jackhammer as source :
	#removing noice
		r.adjust_for_ambient_noise(source)
	#recording data from source to audio
		audio = r.record(source)
	return audio

#function to get audio from microphone
def listen_from_microphone() :
	#fetching audio from microphone
	mic=sr.Microphone()
	print("Listening ....")
	#capturing microphone input
	with mic as source :
		#handling noise
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	return audio

options = '''
Select Input Method :
1.Audio File
2.Microphone
'''
print(options)

ch = input("Choice : ")

#cheching option entered
if ch=='1' :
	audio = read_audio_file()
elif ch=='2' :
	audio = listen_from_microphone()
else :
	print("Invalid Choice")
	exit()

print("Converting to text")
#passing audio to recongnizer
#recognizer method for recognizing speech from audio source
#using google web speech api - requires internet conn./
try :
	print("You said : ",r.recognize_google(audio))
except sr.RequestError :
#Api Unreachable
	print("API Unavailable")
except UnknownValueError :
#Audio Can Not be Detected
	print("Audio is Not Recognizable")