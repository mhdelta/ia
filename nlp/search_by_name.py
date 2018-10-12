import json
import pymongo
from pymongo import MongoClient
from gtts import gTTS
import os
import datetime
import re
#First approach for using speech recognition and the mongo client
#Regex expression is used to find the game in the database by its name
#however this method might be replaced when using nl2sql 
searched_name = raw_input("Game to look at: ");
#regx = re.compile(searched_name)
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gameDB
games = db.games
print("Connected to DB")
data = games.find_one({"name": {'$regex': searched_name}, "storyline": {'$exists': True}})
if data:
	print("Game found")
	print(data["name"])
	print("story: " + data["storyline"])
	text = 'Hi, I have succesfully retrieved the game, '
	text += data['name'] + '. '
	text += 'the game storyline goes like this. ' + data['storyline']
	tts = gTTS(text = text, lang='en')
	tts.save("first_game.mp3")
	print("Audio saved")
else:
	print("Not found")
#Audio is saved and then system can execute it with mpg321
#os.system("mpg321 first_game.mp3")
