import json
from igdb_api_python.igdb import igdb as igdb
import time, os
import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gameDB
companies = db.companies
#ENTER YOUR KEY HERE
igdb = igdb('f7274ba495a7897e39cc471d61b368aa')
data = {}
a = 0 ## La lista va en el #4899
company_list = []
for i in range():
        id_list = []
        b = a + 50
        id_list.extend(range(a, b))
        result = igdb.companies({
            'fields':['id','name', 'country', 'description', 'published', 'developed'],
                'limit': 50,
                'ids': id_list
        })
        company_list.extend(result.body)
        a += 50
companies.insert_many(company_list)
        
if len(company_list):
        companies.insert_many(company_list)
