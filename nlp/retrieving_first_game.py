import json
import pymongo
from pymongo import MongoClient
from gtts import gTTS
import os
import datetime
import re
from gtts import gTTS
import os
import speech_recognition as sr
from googletrans import Translator


tr = Translator()
mic = sr.Microphone()
r = sr.Recognizer()

# text = 'Dime que juego quieres buscar.'
# tts = gTTS(text = text, lang='es')
# tts.save("first_game.mp3")
# os.system("mpg321 first_game.mp3")
print("Escuchando...")
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
game_name = r.recognize_google(audio)

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gameDB
games = db.games
print("Connected to DB")
data = games.find_one({"name": {'$regex': game_name, '$options': 'i'}, "storyline": {'$exists': True}})
if data:
	print("Game found")
	print(data["name"])
	text = 'Hola. He encontrado el juego ' + game_name + ', ahora voy a contar su historia: '
	print(data['storyline'])
	print(type(data['storyline']))
	translated = tr.translate(data['storyline'], dest='es')
	text += translated.text
else:
	text = 'Lo siento, no he podido encontrar tu juego'
tts = gTTS(text = text, lang='es')
tts.save("first_game.mp3")
os.system("mpg321 first_game.mp3")