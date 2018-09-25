from gtts import gTTS
import os
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

text = r.recognize_google(audio)

tts = gTTS(text=text, lang='es')
tts.save("hi_gtts1.mp3")
os.system("mpg321 hi_gtts1.mp3")
