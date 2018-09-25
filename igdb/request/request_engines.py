import json
from igdb_api_python.igdb import igdb as igdb
import time, os
import pymongo
from pymongo import MongoClient
import datetime
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gameDB
engines = db.engines
igdb = igdb('a5b58ad9a031a212726ac14390047c4f')
data = {}
a_1 = 33680 ## La lista va en el #4926
a_2 = 88399
a = 593
for i in range(12):
        id_list = []
        b = a + 50
        for j in range(a, b):
                id_list.append(j)
        result = igdb.game_engines({
            'fields':['id','name'],
                'limit': 50,
                'ids': id_list
        })
        print(result.body)
        for engine in result.body:
                print(engine)
                # engine['created_at'] =  datetime.datetime.fromtimestamp(engine['created_at']/1000)
                engines.insert(engine)        
        a += 50
        

# result = igdb.games({
#             'fields':['id','name', 'genres', 'created_at', 'popularity', 'total_rating', 'storyline', 'platforms', 'game_engines'],
#                 'limit': 1,
#                 'ids': '1'
#         })
# for game in result.body:
#         print(game)   
#         games.insert(game)