import json
from igdb_api_python.igdb import igdb as igdb
import time, os
import pymongo
from pymongo import MongoClient
import datetime
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gameDB
games = db.games
pruebas = db.pruebas
igdb = igdb('f7274ba495a7897e39cc471d61b368aa')
data = {}
a_1 = 85116 ## La lista va en el #4926
a_2 = 88399
a = 85116
game_list = []
for i in range(2100):
        id_list = []
        b = a + 50
        id_list.extend(range(a, b))
        result = igdb.games({
            'fields':['id','name', 'genres', 'created_at', 'popularity', 'total_rating', 'storyline', 'platforms', 'game_engines', 'hypes', 'pegi', 'publishers', 'developers' ,'keywords', 'game_modes', 'player_perspectives'],
                'limit': 50,
                'ids': id_list
        })
        game_list.extend(result.body)
        if len(game_list) >= 1000:
                games.insert_many(game_list)
                game_list = []
        a += 50

if len(game_list):
        games.insert_many(game_list)


        # for game in result.body:
        #         print(game)
        #         game['created_at'] =  datetime.datetime.fromtimestamp(game['created_at']/1000)
        # games.insert_one(game)        
        

# result = igdb.games({
#             'fields':['id','name', 'genres', 'created_at', 'popularity', 'total_rating', 'storyline', 'platforms', 'game_engines'],
#                 'limit': 1,
#                 'ids': '1'
#         })
# for game in result.body:
#         print(game)   
#         games.insert(game)