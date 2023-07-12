import os
from gtts import gTTS
from playsound import playsound
txt = str(input('Write the text you want to convert'))
speed = bool(input('Enter False if you want it fast and True if you want it slow'))
language = 'en'
speech = gTTS(text=txt, lang=language, slow=speed)
speech.save("speech.mp3")
playsound("speech.mp3")
os.remove("speech.mp3")
