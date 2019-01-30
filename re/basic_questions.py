import re
import sys
import pymongo
from pymongo import MongoClient
import datetime as dt
import time
TEST = [
    'juegos de 1990?',
    # 'obtener juegos de 2000?',
    # 'obtener juegos entre 2000 y 2018?',
    # 'listar juegos de 1990 a 1996?',
    # 'dame los juegos desde 2017 hasta 2018?'
    ]
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gameDB
games = db.games
print("Connected to DB")

LISTAR = '(traer|listar|dame|deme|obtener)?'
DE = '(de\s?|del\s?|del\s?anio\s?|entre\s?|desde\s?)?'
A = '(hasta\s?|al?\s?|y\s?)?'
"""
Regex for questions "listar juegos de 1980"
"""
JUEGOSXFECHA = LISTAR + '(\w\s)?juegos ' + DE + '(?P<date>\w+)\?'
"""
Regex for questions "listar juegos entre x y y"
"""
JUEGOSENTREFECHA = LISTAR + '(\w\s)?juegos ' + DE + '(?P<date1>\w+) ' + A + '(?P<date2>\w+)\?' 


# str = raw_input('>> ')
# str = 'obtener los juegos de 1990' 
def identify(string = ''):
    if string:
        out = re.search(JUEGOSXFECHA, string, re.I)
        if out:
            anio = out.group('date')
            ny = str(int(anio)+1)
            timedate = dt.datetime.strptime(anio, '%Y').date()
            epoch = int(timedate.strftime('%s'))
            epochyear = int(dt.datetime.strptime(ny, '%Y').date().strftime('%s'))
            data = games.find({'$and': [
                {'created_at': {'$gte': epoch}},
                {'created_at': {'$lte': epochyear}}
                ]})
            for doc in data:
                print doc['name']
            return;
        out = re.search(JUEGOSENTREFECHA, string, re.I)
        if out:
            print 'db.games.findAll({fecha: {mayorque: ' + out.group('date1') + ' menorque: ' + out.group('date2') + '})'
            return;
        print ":("    

if __name__ == "__main__":
    for i in TEST:
        identify(i)







