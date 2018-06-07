#!/usr/bin/env python3
from gtts import gTTS
import talkey
import time
import os
textInput = input("Text : ")
tts = gTTS(text=textInput, lang='en')
tts.save("good.wav")
os.system("mpg321 good.wav")

time.sleep(1)

tts = talkey.Talkey(
	 engine_preference=['espeak'],

    # Here you segment the configuration by engine
    # Key is the engine SLUG, in this case ``espeak``
    espeak={
        # Specify the engine options:
        'options': {
            'enabled': True,
        },

        # Specify some default voice options
        'defaults': {
                'words_per_minute': 150,
                'variant': 'f4',
        },

        # Here you specify language-specific voice options
        # e.g. for english we prefer the mbrola en1 voice
        'languages': {
            'en': {
                'voice': 'english-mb-en1',
                'words_per_minute': 130
            },
        }
    }
 )
tts.say(textInput)