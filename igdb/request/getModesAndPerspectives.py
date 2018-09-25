import json
from igdb_api_python.igdb import igdb as igdb
import time, os
import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gameDB
modes = db.modes
perspectives = db.perspectives
#ENTER YOUR KEY HERE
igdb = igdb('a5b58ad9a031a212726ac14390047c4f')
# id_list = []
# id_list.extend(range(1, 50))
# result = igdb.game_modes({
#     'fields':['id','name'],
#         'limit': 50,
#         'ids': id_list
# })
# modeList = []
# modeList.extend(result.body)
# print(modeList)
# modes.insert_many(modeList)

id_list = []
id_list.extend(range(1, 50))
result = igdb.player_perspectives({
    'fields':['id','name', 'games'],
        'limit': 50,
        'ids': id_list
})
pList = []
pList.extend(result.body)
perspectives.insert_many(pList)
