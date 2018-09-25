import json
from igdb_api_python.igdb import igdb as igdb
import time, os
import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gameDB
keywords = db.keywords
#ENTER YOUR KEY HERE
igdb = igdb('f7274ba495a7897e39cc471d61b368aa')
data = {}
a = 1101
keyword_list = []
for i in range(450):
        id_list = []
        b = a + 50
        id_list.extend(range(a, b))
        result = igdb.keywords({
                'fields':['id','name','games'],
                'ids': id_list,
                'limit': 50
        })
        keyword_list.extend(result.body)
        a += 50
keywords.insert_many(keyword_list)
        
if len(keyword_list):
        keywords.insert_many(keyword_list)
        