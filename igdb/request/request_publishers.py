import json
from igdb_api_python.igdb import igdb as igdb
import time, os
import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gameDB
games = db.platforms
#ENTER YOUR KEY HERE
igdb = igdb('a5b58ad9a031a212726ac14390047c4f')
data = {}
a = 149 ## La lista va en el #4899
for i in range(3):
        id_list = []
        b = a + 50
        for j in range(a, b):
                id_list.append(j)
        result = igdb.platforms({
            'fields':['name'], #no se incluyo el summary
                'limit': 50,
                'ids': id_list
        })
        print(result.body)
        for game in result.body:
                print(game)
                games.insert(game)        

        a += 50
        