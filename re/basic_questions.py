import re
import sys
from pruebas import test
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
            print 'db.games.findAll({fecha:' + out.group('date') + '})'
            return;
        out = re.search(JUEGOSENTREFECHA, string, re.I)
        if out:
            print 'db.games.findAll({fecha: {mayorque: ' + out.group('date1') + ' menorque: ' + out.group('date2') + '})'
            return;
        print ":("    

if __name__ == "__main__":
    if sys.argv[1] == 'test':
        for i in test:
            identify(i)







