#!/usr/bin/env python3

#to recognize speech using Api or speech engine
import speech_recognition as sr

#recognizer instance
r=sr.Recognizer()

#recognizer method for recognizing speech from audio source
#using google web speech api - require internet
r.recognize_google()

